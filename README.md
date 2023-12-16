# Clustering-based Movie recommendation_system

**Note: To run the Python file please download the pickle file from [here](https://drive.google.com/drive/folders/1zdq2SVW5gykZSJ_EDU_k3_q8WrnY_qre?usp=sharing)**

 
__Problem Statement:__

The traditional collaborative filtering approach faces several challenges that hinder its effectiveness in recommendation systems:

1. overreliance on user ratings

2. The cold start problem for new users or items

3. Dependency on a large user community

4. Sparsity issues in user-item interaction matrices

5. Limited control over recommendations

To overcome these challenges, a clustering-based recommendation system is proposed.

__Objective:__

🔹Develop a clustering-based recommendation system to address the limitations of traditional collaborative filtering. The system aims to provide accurate and relevant movie recommendations by clustering movies based on their content features, such as overview, genres, keywords, cast, and crew.

🔹The goal is to enhance recommendation accuracy, especially for new users, items with limited rating data, and in scenarios where there is a lack of a substantial user community.

__Proposed Solution:__

🔹Utilizing a dataset containing movie information, the recommendation system employs a clustering approach based on textual content features.

🔹The content features are preprocessed, including cleaning, transformation, and vectorization. The Porter stemming technique is applied to handle variations in words.

🔹The Bag of Words (BOW) technique with CountVectorizer is used to convert text to vectors, capturing the essence of movie content.

__Word Cloud__

![image](https://github.com/shivamjha2705/Clustering_based_recommendation_system/assets/69563640/d4356f20-9c28-4a6a-84b2-5a9e90a57976)

__Similarity Heatmap__

![image](https://github.com/shivamjha2705/Clustering_based_recommendation_system/assets/69563640/4c5d05f9-f984-448f-925f-1d987875a4b5)

__Final User Interface__

![Screenshot 2023-12-01 010351](https://github.com/shivamjha2705/Clustering_based_recommendation_system/assets/69563640/94b164ed-378d-4a6f-bf10-101e57221817)

__Outcome:__

🔶The outcome is a clustering-based movie recommendation system that provides recommendations based on content similarity.

🔶Users can input a movie title, and the system will cluster similar movies, offering personalized recommendations.

🔶This approach mitigates the limitations of traditional collaborative filtering, particularly in scenarios involving new users, sparse interaction matrices, and limited control over recommendations.

🔶The system empowers recommendation engines to deliver more accurate and relevant suggestions, contributing to an enhanced user experience in movie recommendation platforms.
