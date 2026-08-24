# app/utils.py

import pandas as pd
import numpy as np
from app.config import LUXURY_BRANDS, ENGINE_BINS, ENGINE_LABELS

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features to the input dataframe.
    This must match the feature engineering done during training.
    """
    df = df.copy()
    
    # 1. Age squared (non-linear depreciation)
    df['age_squared'] = df['vehicle_age'] ** 2
    
    # 2. KM per year (usage intensity)
    df['km_per_year'] = df['km_driven'] / (df['vehicle_age'] + 1)
    
    # 3. Power per CC (engine efficiency)
    df['power_per_cc'] = df['max_power'] / (df['engine'] + 1)
    
    # 4. Mileage per HP (fuel efficiency context)
    df['mileage_per_hp'] = df['mileage'] / (df['max_power'] + 1)
    
    # 5. Age-KM interaction
    df['age_km_interaction'] = df['vehicle_age'] * df['km_driven']
    
    # 6. Engine-Power interaction
    df['engine_power_interaction'] = df['engine'] * df['max_power']
    
    # 7. Engine category (categorical)
    df['engine_category'] = pd.cut(
        df['engine'],
        bins=ENGINE_BINS,
        labels=ENGINE_LABELS,
        right=False
    )
    
    # 8. Brand group (categorical)
    df['brand_group'] = df['brand'].apply(
        lambda x: 'Luxury' if x in LUXURY_BRANDS else 'Mass Market'
    )
    
    # 9. Brand-Model combination (categorical)
    df['brand_model'] = df['brand'] + '_' + df['model']
    
    return df

def get_price_category(price: float) -> str:
    """Categorize price into meaningful ranges"""
    if price < 300000:
        return "Budget"
    elif price < 800000:
        return "Entry"
    elif price < 1500000:
        return "Mid-Range"
    elif price < 3000000:
        return "Premium"
    elif price < 5000000:
        return "Luxury"
    else:
        return "Ultra-Luxury"

def get_deal_status(predicted_price: float, asking_price: float) -> tuple:
    """Analyze the deal and return status and difference"""
    difference = asking_price - predicted_price
    diff_percentage = (difference / predicted_price) * 100
    
    if diff_percentage < -10:
        return "🟢 Good Deal", difference
    elif diff_percentage < 10:
        return "🟡 Fair Price", difference
    else:
        return "🔴 Overpriced", difference