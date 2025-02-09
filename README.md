# Amazon Products Reviews Classification

# Overview
This project focuses on classifying Amazon product reviews as positive or negative using various machine learning and deep learning techniques. The dataset contains tens of thousands of Amazon reviews, labeled as positive or negative based on user ratings. The goal is to build a classification model that can accurately predict the sentiment of a review, helping Amazon improve its products and services based on customer feedback.

# Dataset
The dataset is collected from Kaggle and can be accessed here:
https://www.kaggle.com/kritanjalijain/amazon-reviews?select=train.csv

# Goal
The primary objective is to develop a classification model that can accurately classify product reviews on Amazon. This will help the company identify areas for improvement and enhance customer satisfaction.

# Preparation

Packages
The following Python packages are used in this project:
- seaborn
- numpy
- pandas
- collections
- sklearn
- spacy
- langid
- plotly
- cufflinks
- fastai
- opendatasets
- pymongo
- streamlit

Data
The dataset is downloaded and extracted using the opendatasets library. The data is then loaded into Pandas DataFrames for further processing.

Text Features

# Models
1. CountVectorizer + MultinomialNB
2. TfidfVectorizer + MultinomialNB
3. CountVectorizer + MultinomialNB w/o stopwords
4. TfidfVectorizer + MultinomialNB w/o stopwords
5. CountVectorizer + MultinomialNB lemmatized

# Model Comparison
| Models                                | Accuracy Score |
|----------------------------------------|----------------|
| CountVectorizer + MultinomialNB        | 88.60          |
| TfidfVectorizer + MultinomialNB        | 88.20          |
| CountVectorizer + MultinomialNB w/o stopwords | 86.49       |
| TfidfVectorizer + MultinomialNB w/o stopwords | 86.28       |
| CountVectorizer + MultinomialNB lemmatized  | 87.53        |

# Observation
Lemmatizing provides better results than removing stopwords and reduces the number of features. However, the accuracy is still not as good as using the original text.

# Deep Learning

LSTM
The Long Short-Term Memory (LSTM) model is implemented using the AWD-LSTM architecture. The language model is finetuned on the corpus before building the classifier. The model is trained using the 1cycle policy and gradually unfreezing the layers.

Observation from LSTM
The LSTM model achieved an accuracy of 90%, significantly higher than the baseline models. The validation dataset contains some wrongly labeled samples, as observed from the top losses.

Overall Comparison
The LSTM model outperforms the text feature-based models, providing a more accurate and robust classification of Amazon product reviews.

# Conclusion
The project demonstrates the effectiveness of deep learning models, particularly LSTM, in sentiment analysis tasks. The LSTM model provides a significant improvement over traditional machine learning models based on text features.

# Streamlit App
A Streamlit app is developed to provide a user-friendly interface for sentiment analysis of Amazon product reviews. The app allows users to input a review and get the sentiment prediction along with the probability scores.

Running the Streamlit App
1. Install the required packages:
   pip install streamlit fastai
2. Save the LSTM model to a .pkl file:
   import pickle
   with open('lstm_model.pkl', 'wb') as f:
       pickle.dump(clas_learn, f)
3. Run the Streamlit app:
   streamlit run app.py

# Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Contact
For any questions or suggestions, please contact [Vinod Kumar] at [msd23022@iiitl.ac.in].

---

Feel free to explore the code and datasets to understand the implementation details and contribute to the project.

# Reference
chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://norma.ncirl.ie/6263/1/priyanka.pdf
