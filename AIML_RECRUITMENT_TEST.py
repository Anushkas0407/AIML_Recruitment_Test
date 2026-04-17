Scenario 1:Data ValidationTask
def validate_data(data):
        " " " 
        Validates a list of dictionaries to ensure 'age' is in integer.
        Returns a list of invalid entries. 
        " " "
       invalid _entries = [ ]
       for entry in data: 
         if "age" not in entry or not isinstance(entry["age"] , int):                 
             invalid_entries.append(entry)
       return invalid_entries 
data=[
      {"name": "Alice", "age": 30},
      {"name": "Bob", "age": 25},
      {"name": "Charlie", "age": 35},
      {"name": "David"},
      {"name": "Eve","age":20.5},

]
invalid_data=validate_data(data)
print(invalid_data)

Scenario 2: Logging DecoratorTask
import time
from functools import wraps

def log_execution_time(func):
    """Decorator that logs the time taken to execute a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  
        result = func(*args, **kwargs)   
        end_time = time.perf_counter()    
        
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.6f} seconds to execute.")
        return result
    return wrapper

@log_execution_time
def calculate_sum(n):
    """Returns the sum of numbers from 1 to n."""
    return sum(range(1, n + 1))

if __name__ == "__main__":
    result = calculate_sum(1000000)
    print(f"Sum: {result}")

Scenario 3:Missing Value Handling
import pandas as pd

# Assuming 'df' is your DataFrame
# 1. Calculate the skewness of the income column
skewness = df['income'].skew()

# 2. Check the skewness threshold
if abs(skewness) < 0.5:
    # Normally distributed: Replace with Median
    fill_value = df['income'].median()
else:
    # Skewed: Replace with Mode 
    # (Mode returns a Series, so we take the first value [0])
    fill_value = df['income'].mode()[0]

# 3. Apply the imputation
df['income'] = df['income'].fillna(fill_value)

Scenario 4:Text Pre-processing 
import pandas as pd
import re

df = pd.DataFrame({'text_column': ['Hello World!', 'Data Science @ NLP #2024']})

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    return text.split()

df['cleaned_tokens'] = df['text_column'].apply(clean_text)

print(df)

Scenario 5: Hyperparameter Tuning
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 5, 7],
    'n_estimators': [50, 100]
}
rf = RandomForestClassifier(random_state=42)

# cv=5 indicates 5-fold cross-validation
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)

grid_search.fit(X_train, y_train)

print("Best parameters found:", grid_search.best_params_)
best_rf_model = grid_search.best_estimator_

Scenario 6: Custom Evaluation Metric
import tensorflow as tf
from tensorflow.keras import backend as K

def weighted_accuracy(y_true, y_pred):
    """
    Weighted accuracy metric for binary classification.
    Class 0: Weight 1
    Class 1: Weight 2
    """
    y_pred = K.round(y_pred)
    y_true = K.cast(y_true, 'float32')
   
    correct = K.cast(K.equal(y_true, y_pred), 'float32')
   
    # Logic: if y_true is 0, (1.0-0)*1 + (0)*2 = 1.0
    #        if y_true is 1, (1.0-1)*1 + (1)*2 = 2.0
    weights = (1.0 - y_true) * 1.0 + (y_true) * 2.0
    

    weighted_correct = correct * weights
    return K.sum(weighted_correct) / K.sum(weights)

# Usage Example:
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[weighted_accuracy])


Scenario 7: Image Augmentation
import tensorflow as tf
from tensorflow.keras import layers, Sequential

data_augmentation = Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(20/360), # ±20 degrees
    layers.RandomZoom(0.2),         # 0.2x zoom
])

model = Sequential([
    # Add input shape layer (e.g., 224x224 RGB)
    layers.Input(shape=(224, 224, 3)),
    
    # Preprocessing layers are active during training only
    data_augmentation,
    
    layers.Rescaling(1./255),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
 
])

Scenario 8: Model Callbacks
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(
    monitor='val_loss',      
    patience=3,              
    restore_best_weights=True 
)

model.fit(
    x_train, y_train,
    epochs=100,
    validation_data=(x_val, y_val),
    callbacks=[early_stopping]
)

Scenario 9: Structured Response Generation
import google.generativeai as genai
import json

model = genai.GenerativeModel('gemini-pro')

prompt = """
List 3 benefits of Python for data science. 
Return the response strictly in JSON format with the following structure:
{
  "benefits": ["benefit 1", "benefit 2", "benefit 3"]
}
"""

response = model.generate_content(prompt)

try:
    clean_json = response.text.strip().replace('json', '').replace('', '')
    data = json.loads(clean_json)
    print("Valid JSON received:")
    print(data)

except (json.JSONDecodeError, ValueError) as e:
    print("Error: The response from Gemini was not valid JSON.")
    print(f"Raw response: {response.text}")

Scenario 10: Summarization with Constraints
Summarize the following news article into exactly two sentences. The total length must not exceed 50 words. If the summary is longer than 50 words, truncate it so that it ends at the last complete sentence within that limit.
Article: [Insert Article Text Here]
