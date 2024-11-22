import streamlit as st
import pickle

# Load the saved LSTM model from the .pkl file
with open('lstm_model.pkl', 'rb') as f:
    loaded_lstm_model = pickle.load(f)

# Function to predict sentiment
def predict_review(review_text):
    prediction, class_idx, probabilities = loaded_lstm_model.predict(review_text)
    return  "Positive review" if prediction == "2" else "Negative review",probabilities


# Streamlit app

def main():
    st.title("Amazon Customer Feedback Classifier")
    st.write("Analyze the sentiment of your reviews. Please enter a review below to get started.")

    # Input text area for review
    review_text = st.text_area("Enter your review", height=200)

    if st.button("Analyze Sentiment"):
        if review_text.strip():
            # Get sentiment analysis

            with st.spinner("Analyzing..."):
                sentiment, probabilities = predict_review(review_text)
            st.success(f"Sentiment: {sentiment}")
            st.success(f"Probabilities:{probabilities}")
            #st.json(probabilities)
        else:
            st.error("Please enter a valid review.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
