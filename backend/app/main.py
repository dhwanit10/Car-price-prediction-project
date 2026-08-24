# app/main.py

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd

from app.config import API_TITLE, API_VERSION, API_DESCRIPTION
from app.schemas import CarFeatures, PriceResponse, DealAnalysisResponse, HealthResponse
from app.utils import engineer_features, get_price_category, get_deal_status
from app.models import PricePredictor

# Initialize FastAPI app
app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize predictor
predictor = PricePredictor()

# ============================================
# Health Check Endpoint
# ============================================
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Check if the API and model are healthy"""
    return HealthResponse(
        status="OK",
        model_loaded=predictor.is_loaded,
        api_version=API_VERSION
    )

# ============================================
# Prediction Endpoints
# ============================================
@app.post("/predict", response_model=PriceResponse)
async def predict_price(car: CarFeatures):
    """
    Predict the fair market price of a used car.
    
    Send car features in the request body and get back the predicted price.
    """
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([car.model_dump()])
        
        # Engineer features
        input_df_engineered = engineer_features(input_df)
        
        # Get prediction
        prediction = predictor.predict(input_df_engineered)
        
        # Prepare response
        return PriceResponse(
            predicted_price=round(prediction, 2),
            predicted_price_lakhs=round(prediction / 100000, 2),
            price_category=get_price_category(prediction)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Prediction failed: {str(e)}"
        )

@app.post("/predict-with-asking", response_model=DealAnalysisResponse)
async def predict_with_asking(car: CarFeatures, asking_price: float):
    """
    Predict price and analyze the deal based on seller's asking price.
    """
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([car.model_dump()])
        
        # Engineer features
        input_df_engineered = engineer_features(input_df)
        
        # Get prediction
        prediction = predictor.predict(input_df_engineered)
        
        # Analyze deal
        deal_status, difference = get_deal_status(prediction, asking_price)
        
        # Prepare response
        return DealAnalysisResponse(
            predicted_price=round(prediction, 2),
            predicted_price_lakhs=round(prediction / 100000, 2),
            price_category=get_price_category(prediction),
            asking_price=asking_price,
            price_difference=round(difference, 2),
            deal_status=deal_status
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Prediction failed: {str(e)}"
        )

# ============================================
# Bulk Prediction Endpoint
# ============================================
@app.post("/predict-bulk")
async def predict_bulk(cars: list[CarFeatures]):
    """
    Predict prices for multiple cars in one request.
    Useful for batch processing.
    """
    try:
        # Convert list to DataFrame
        input_df = pd.DataFrame([car.model_dump() for car in cars])
        
        # Engineer features
        input_df_engineered = engineer_features(input_df)
        
        # Get predictions
        predictions = predictor._pipeline.predict(input_df_engineered)
        
        # Prepare response
        results = []
        for i, pred in enumerate(predictions):
            results.append({
                "car_index": i,
                "predicted_price": round(pred, 2),
                "predicted_price_lakhs": round(pred / 100000, 2),
                "price_category": get_price_category(pred)
            })
        
        return JSONResponse({
            "count": len(results),
            "results": results
        })
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Bulk prediction failed: {str(e)}"
        )

# ============================================
# Model Info Endpoint
# ============================================
@app.get("/model-info")
async def get_model_info():
    """Get information about the model"""
    return {
        "model_type": "XGBoost Regressor",
        "is_loaded": predictor.is_loaded,
        "features_used": {
            "categorical": [
                "brand", "model", "seller_type", "fuel_type", 
                "transmission_type", "engine_category", "brand_group", "brand_model"
            ],
            "numerical": [
                "vehicle_age", "km_driven", "mileage", "engine", "max_power", "seats",
                "age_squared", "km_per_year", "power_per_cc", "mileage_per_hp",
                "age_km_interaction", "engine_power_interaction"
            ]
        }
    }

# ============================================
# Error Handlers
# ============================================
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "message": exc.detail,
            "path": request.url.path
        }
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status": "error",
            "message": "An unexpected error occurred",
            "detail": str(exc)
        }
    )

# ============================================
# Root Endpoint
# ============================================
@app.get("/")
async def root():
    return {
        "message": "Used Car Price Prediction API",
        "version": API_VERSION,
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )