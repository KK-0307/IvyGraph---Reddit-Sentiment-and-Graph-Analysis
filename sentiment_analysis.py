import reddit_bot
import string
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment(subreddit):
    posts = reddit_bot.open_reddit(subreddit, 1000)
    analyzer = SentimentIntensityAnalyzer()  # Instantiate the analyzer once

    neg_score, pos_score, neu_score, comp_score = [], [], [], []

    for post in posts:
        text = " ".join(post)  # Combine title and selftext
        text = text.translate(str.maketrans('', '', string.punctuation + string.whitespace))
        score = analyzer.polarity_scores(text)
        
        if score['neg'] > 0.0 or score['neu'] > 0 or score['pos'] > 0 and score['compound'] > 0:
            neg_score.append(score['neg'])
            pos_score.append(score['pos'])
            neu_score.append(score['neu'])
            comp_score.append(score['compound'])

    return {
        'Average Negativity': round(average_lst(neg_score), 3),
        'Average Neutrality': round(average_lst(neu_score), 3),
        'Average Positivity': round(average_lst(pos_score), 3),
        'Average Compound': round(average_lst(comp_score), 3)
    }

def average_lst(lst):
    return sum(lst) / len(lst) if lst else 0

def main():
    subreddit = 'upenn'  # Example subreddit
    result = sentiment(subreddit)
    print(f"Result of sentiment analysis on {subreddit}: {result}")

if __name__ == '__main__':
    main()
