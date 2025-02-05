from sklearn.feature_extraction.text import CountVectorizer
import joblib

# Load the trained model
model = joblib.load('model.pkl')
print(model)

def detect_query_type(query: str):
    """
    Uses the trained Naive Bayes model to predict whether the query is related to stock or sales.
    """
    # Predict using the Naive Bayes model (the pipeline includes the vectorizer)
    prediction = model.predict([query])  # Query should be passed as a list

    # Return the predicted class (can be 'stock' or 'sales' depending on the model)
    return prediction # Extract the first prediction

while True:
        query = input('Write a prompt for search :  ')
        prediction = detect_query_type(query)
        print(prediction)

        if query == 'End':
              break