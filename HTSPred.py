from joblib import load
import numpy as np

# Load the model and label encoder from saved files
pipeline = load('hts_pipeline.joblib')
label_encoder = load('hts_label_encoder.joblib')


proba = pipeline.predict_proba(["Roasted  coffee beans, reduced caffeine, for beverage preparation"])
    
# Get the indices of the top 3 predictions
top_3_indices = np.argsort(-proba, axis=1)[0, :3]
    
# Decode the indices to HTS codes
top_3_codes = label_encoder.inverse_transform(top_3_indices)


print(top_3_codes)