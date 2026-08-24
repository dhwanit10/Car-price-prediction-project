# app/models.py

import joblib
import pandas as pd
from app.config import MODEL_PATH

class PricePredictor:
    """Singleton class for loading and using the prediction model"""
    
    _instance = None
    _pipeline = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PricePredictor, cls).__new__(cls)
            cls._instance._load_model()
        return cls._instance
    
    def _load_model(self):
        """Load the trained pipeline"""
        try:
            self._pipeline = joblib.load(MODEL_PATH)
            print("✅ Model loaded successfully!")
        except FileNotFoundError:
            print(f"❌ Model not found at {MODEL_PATH}")
            raise
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            raise
    
    def predict(self, features: pd.DataFrame) -> float:
        """Make a prediction"""
        if self._pipeline is None:
            raise ValueError("Model not loaded")
        
        # Make prediction
        prediction = self._pipeline.predict(features)[0]
        
        # Ensure prediction is not negative
        return max(0, prediction)
    
    @property
    def is_loaded(self) -> bool:
        return self._pipeline is not None