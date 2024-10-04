import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from reddit_bot import open_reddit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def calculate_textual_similarities(subreddits):
    posts = {sub: ' '.join(preprocess_text(post) for post in open_reddit(sub, 1000)) for sub in subreddits}
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(posts.values())
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    sns.heatmap(similarity_matrix, annot=True, xticklabels=subreddits, yticklabels=subreddits, cmap='coolwarm')
    plt.title('Textual Similarity Heatmap')
    plt.show()

if __name__ == "__main__":
    subreddits = ['upenn', 'harvard', 'yale', 'princeton', 'columbia', 'dartmouth', 'cornell', 'brown']
    calculate_textual_similarities(subreddits)
