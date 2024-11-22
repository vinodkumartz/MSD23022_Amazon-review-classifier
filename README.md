# Amazon Products Reviews Classification
# 1) Goal
The primary objective of this project is to develop a classification model to analyze product reviews from Amazon. The model aims to determine whether a review conveys a positive or negative sentiment. This analysis helps Amazon improve customer satisfaction by addressing faults and enhancing the customer experience.


Objectives
Explore text-based features and deep learning methodologies for sentiment classification.
Compare various models' performance to identify the most effective approach.
Provide actionable insights for improving customer experience on Amazon's platform.
Methodology

1. Data Preparation
Dataset: Amazon reviews dataset sourced from Kaggle, containing labeled reviews classified as positive or negative.
Preprocessing: Data cleaning, tokenization, and text preparation techniques (e.g., stopword removal, lemmatization).

3. Text Features
Applied text vectorization techniques:
CountVectorizer with Multinomial Naive Bayes.
TFIDFVectorizer with Multinomial Naive Bayes.
Examined variations, such as with/without stopwords and lemmatization.

5. Deep Learning
Implemented an LSTM (Long Short-Term Memory) neural network for sentiment analysis.

7. Evaluation
Compared the performance of models based on accuracy and other metrics.
Conducted an overall comparison to highlight the best-performing model.
Dataset
Source: Kaggle: Amazon Reviews
Features:
label: Target variable (1 for negative, 2 for positive reviews).
title: Review title.
text: Review body.
Results
The notebook showcases model comparisons and insights derived from text-based and deep learning models, with recommendations for improving customer engagement based on sentiment analysis outcomes.

Conclusion
The project demonstrates the efficacy of various text classification techniques for sentiment analysis. It provides insights into improving customer feedback systems, contributing to better product offerings and overall customer satisfaction.

