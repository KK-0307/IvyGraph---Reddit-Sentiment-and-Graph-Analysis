from fuzzywuzzy import fuzz

import reddit_bot
import sentiment_analysis
import string
import nltk
from nltk.corpus import stopwords

#Set of english stopwords
stop_words = set(stopwords.words('english'))


def compare_subreddit(sub1, sub2):
    '''
    Compares the similarity (simple ratio, partial ratio, and token sort ratio) of r/Upenn and other ivy league unis and returns the ratio of each.
    '''
    upenn_lst = add_to_list(sub1)
    other_ivies = add_to_list(sub2)

    simple_ratio = []
    partial_ratio = []
    token_sort_ratio = []

    for upenn_item, ivy_item in zip(upenn_lst, other_ivies):
        simple_ratio.append(fuzz.ratio(upenn_item, ivy_item))
        partial_ratio.append(fuzz.partial_ratio(upenn_item, ivy_item))
        token_sort_ratio.append(fuzz.token_sort_ratio(upenn_item, ivy_item))
    
    return f'On average, \nThe simple ratio is: {sentiment_analysis.average_lst(simple_ratio)}\n The partial ratio is: {sentiment_analysis.average_lst(partial_ratio)}\n The tokern sort ratio is: {sentiment_analysis.average_lst(token_sort_ratio)}'


def add_to_list(sub):
    '''
    Return a list of top 1000 post from a given subreddit.
    '''
    lst = []
    for item in reddit_bot.open_reddit(sub, 1000):
        for line in item:
            #line = line.strip(string.punctuation + string.whitespace)
            #lst.append(line)
            line = line.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
            cleaned_line = ' '.join(word for word in line.split() if word.lower() not in stop_words) #split into words and remove stopwords
            lst.append(cleaned_line)
    return lst


def main():
    # Comparing UPenn subreddit to three other ivy league subreddits
    print(compare_subreddit('upenn', 'harvard'))
    print(compare_subreddit('upenn', 'yale'))
    print(compare_subreddit('upenn', 'columbia'))
    print(compare_subreddit('upenn', 'cornell'))
    print(compare_subreddit('upenn', 'brown'))
    print(compare_subreddit('upenn', 'princeton'))
    print(compare_subreddit('upenn', 'dartmouth'))


if __name__ == '__main__':
    main()