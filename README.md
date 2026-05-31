# AI Product Discovery Engine | NLP Recommendation System, Semantic Search & E-Commerce Analytics

## Executive Summary
Traditional e-commerce search engines rely heavily on keyword matching, often failing to understand customer intent when users describe products in natural language. To address this challenge, I developed an AI-powered Product Discovery Engine that leverages Natural Language Processing (NLP), semantic search, and vector embeddings to deliver more relevant product recommendations. Using Sentence Transformers, cosine similarity, and over 10,000 product listings, the system enables users to discover products through conversational queries rather than exact keywords. The solution was deployed as an interactive Streamlit web application, demonstrating an end-to-end machine learning workflow from data engineering and model development to cloud deployment.

## Application Preview
🔗 Streamlit App: https://ai-shopping-assistant-prerana.streamlit.app 

Live Demo: 
<img width="1440" height="745" alt="app-demo" src="https://github.com/user-attachments/assets/9575a3ff-32c5-4b3e-9d24-2c4f63601a72" />

## Business Problem
Online retailers often struggle to connect customers with relevant products when search queries do not exactly match product titles or descriptions. This can result in poor user experiences, lower conversion rates, and lost revenue opportunities.
This project addresses that challenge by building an AI-powered recommendation system capable of understanding user intent through semantic similarity rather than traditional keyword matching.


## Methodology
Data Preparation:
- Processed and cleaned Amazon product catalog data
- Handled missing values across product descriptions and attributes
- Combined multiple text features into a unified representation
  
Feature Engineering:
- Created enriched product representations using:
- Product Titles
- Product Descriptions
- Product Bullet Points
  
Machine Learning & NLP:
- Generated semantic embeddings using Sentence Transformers (all-MiniLM-L6-v2)
- Calculated product similarity using cosine similarity
- Built a recommendation engine that ranks products based on semantic relevance

Deployment:
- Developed an interactive Streamlit web application
- Integrated model inference into a user-facing recommendation workflow
- Deployed the application to the cloud using GitHub and Streamlit Community Cloud

## Skills 
Machine Learning: Recommendation Systems, Vector Embeddings, Similarity Search, Model Deployment, Natural Language Processing (NLP), Sentence Transformers, Semantic Search, Text Feature Engineering, Embedding Generation

Data Science & Analytics: Exploratory Data Analysis (EDA), Data Cleaning, Feature Engineering, Performance Evaluation

Software Engineering: Python, Object-Oriented Programming, Git & GitHub, Streamlit Application Development

## Results & Recommendations 
Results:
- Built a semantic recommendation engine capable of understanding natural language product requests
- Generated personalized product recommendations using vector similarity search
- Successfully deployed an interactive AI application accessible through a web browser
- Demonstrated a complete end-to-end machine learning pipeline from raw data to production deployment
  
Business Recommendations:
- Integrate customer clickstream and purchase history for personalized recommendations
- Implement hybrid recommendation models combining content-based and collaborative filtering techniques
- Incorporate product ratings and customer reviews to improve recommendation quality
- Add explainable AI features to increase user trust and engagement

## Next Steps
- Add product image retrieval and display
- Integrate price filtering and category-based recommendations
- Implement user personalization using behavioral data
- Build a hybrid recommendation engine combining NLP and collaborative filtering
- Deploy model monitoring and recommendation performance tracking
- Expand to a Retrieval-Augmented Generation (RAG) shopping assistant powered by large language models
