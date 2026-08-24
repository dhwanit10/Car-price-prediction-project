# app/config.py

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model paths
MODEL_PATH = BASE_DIR / "models" / "full_pipeline.pkl"

# Luxury brands list (must match what was used in training)
LUXURY_BRANDS = [
    'Mercedes-Benz', 'BMW', 'Audi', 'Land Rover',
    'Jaguar', 'Porsche', 'Lexus', 'Volvo', 'Mini',
    'Mercedes-AMG', 'Maserati', 'Bentley', 'Rolls-Royce'
]

# Engine category bins
ENGINE_BINS = [0, 1500, 2500, 3500, 6000]
ENGINE_LABELS = ['Small', 'Mid', 'Large', 'Luxury']

# API settings
API_TITLE = "Used Car Price Prediction API"
API_VERSION = "1.0.0"
API_DESCRIPTION = """
## Used Car Price Prediction API

This API predicts the fair market price of used cars based on their characteristics.

### Features used:
- **Brand & Model**: The make and specific model of the car
- **Vehicle Age**: How old the car is (in years)
- **KM Driven**: Total kilometers driven
- **Fuel Type**: Petrol, Diesel, CNG, LPG, Electric
- **Transmission**: Manual or Automatic
- **Engine**: Engine capacity in CC
- **Max Power**: Maximum horsepower
- **Mileage**: Fuel efficiency (km/l)
- **Seats**: Number of seats
- **Seller Type**: Individual, Dealer, or Trustmark Dealer

### Engineered Features:
The model uses additional engineered features derived from the inputs:
- Age squared (for non-linear depreciation)
- KM driven per year (usage intensity)
- Power per CC (engine efficiency)
- Mileage per HP (fuel efficiency context)
- Age-KM interaction
- Engine-Power interaction
- Engine category (Small, Mid, Large, Luxury)
- Brand group (Luxury vs Mass Market)
- Brand-Model combination

### Response:
- `predicted_price`: The predicted price in rupees
- `predicted_price_lakhs`: The predicted price in lakhs
- `price_category`: The price range category
"""