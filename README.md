# IvyGraph---Reddit-Sentiment-and-Graph-Analysis
This project aims to explore interaction dynamics and sentiment trends across Ivy League subreddits, with a specific focus on the Penn subreddit. By analyzing the top 1000 posts from each Ivy League subreddit, the goal is to uncover distinct patterns in engagement and sentiment, comparing how the Penn community interacts versus other Ivy League schools.

Please note that **this code should not be copied or reused**, as it is part of a group project and may contain proprietary work from all team members. Reuse or replication of the code may violate academic integrity guidelines.

## Research Question

**"How do interaction dynamics and sentiment trends in the Penn subreddit compare with those in other Ivy League subreddits, based on the analysis of the top 1000 posts from each?"**

## Hypothesis

The Penn subreddit exhibits distinct interaction dynamics characterized by higher engagement but more negative sentiment in discussions, compared to other Ivy League subreddits. This suggests a more active yet critically vocal community within Penn’s online Reddit presence.

## Features

- **Sentiment Analysis**: Measures the overall sentiment (positive, neutral, or negative) in the top 1000 posts from each Ivy League subreddit.
- **Interaction Dynamics**: Analyzes user engagement metrics such as comments, upvotes, and user participation to gauge community activity.
- **Graph Visualization**: Visualizes the relationships between users, topics, and interactions within the Ivy League subreddits using graphs.
- **Textual Similarity**: Compares the content of posts between subreddits to explore topic overlap and textual patterns.
- **Summary Generation**: Summarizes long Reddit threads for a quick overview of key topics and sentiments.

## Key Scripts

- **ivyGraph.py**: Generates graphs that visualize user interactions and discussions across subreddits.
- **reddit_bot.py**: Scrapes the top 1000 posts from each Ivy League subreddit using the Reddit API.
- **sentiment_analysis.py**: Analyzes sentiment trends in the collected Reddit data using natural language processing (NLP).
- **summary.py**: Summarizes long Reddit threads into brief, easy-to-understand content.
- **textual_similarity.py**: Compares the content between posts to measure how similar they are, allowing for the exploration of common topics.

## Technologies Used

- **Python**: Core language for data processing and analysis.
- **PRAW (Python Reddit API Wrapper)**: For accessing Reddit's API and retrieving subreddit data.
- **NLTK (Natural Language Toolkit)**: For sentiment analysis and text processing.
- **NetworkX**: For generating graphs and visualizing social networks.
- **Matplotlib**: For data visualization, including sentiment trends and interaction graphs.
- **Scikit-learn**: For textual similarity calculations.
