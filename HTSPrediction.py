import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load the data
data = pd.read_csv('htsdata.csv')
data_clean = data.dropna(subset=['HTS Number', 'Description'])

# Prepare the data
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data_clean['HTS Number'])
X = data_clean['Description']

# Check class distribution
class_counts = np.bincount(y)
print("Class counts:", class_counts)

# Filter classes with enough instances
min_class_count = 3  # Adjusted threshold to accommodate smaller dataset
valid_classes = np.where(class_counts >= min_class_count)[0]
valid_indices = np.isin(y, valid_classes)
X_filtered, y_filtered = X[valid_indices], y[valid_indices]

# Check if there are any valid samples left
if len(X_filtered) == 0:
    raise ValueError("No valid samples left after filtering. Consider lowering the min_class_count.")

# Define a pipeline with advanced text processing and a more complex classifier
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', ngram_range=(1,2))),
    ('svd', TruncatedSVD(n_components=200)),  # Increase dimensionality reduction
    ('clf', RandomForestClassifier(random_state=42))
])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_filtered, y_filtered, test_size=0.2, random_state=42)

# Hyperparameter tuning
param_grid = {
    'tfidf__max_features': [1000, 2000],
    'svd__n_components': [100, 200],
    'clf__n_estimators': [100, 200],
    'clf__max_depth': [10, 20]
}
grid_search = GridSearchCV(pipeline, param_grid, cv=3, verbose=2, n_jobs=-1)  # Reduced CV splits to 3
grid_search.fit(X_train, y_train)

# Best model evaluation
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=label_encoder.inverse_transform(np.unique(y_filtered))))

# Save the best model and label encoder
from joblib import dump
dump(best_model, 'best_hts_pipeline.joblib')
dump(label_encoder, 'best_hts_label_encoder.joblib')
