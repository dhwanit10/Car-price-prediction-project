# scripts/generate_feature_importance.py

import pandas as pd
import numpy as np
import joblib
import json

# Load model
pipeline = joblib.load('../models/full_pipeline.pkl')

# Get feature names from preprocessor
preprocessor = pipeline.named_steps['preprocessor']
feature_names = preprocessor.get_feature_names_out()

# Get feature importances
model = pipeline.named_steps['model']
importances = model.feature_importances_

# Create mapping
feature_importance = dict(zip(feature_names, importances))

print(feature_importance)
# Save to JSON
# with open('../app/data/feature_importance.json', 'w') as f:
#     json.dump(feature_importance, f, indent=2)

print("✅ Feature importance saved!")