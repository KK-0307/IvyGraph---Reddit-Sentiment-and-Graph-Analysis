import string
import reddit_bot
import sentiment_analysis
import text_similarity
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#loading NLTK's list of English stopwords
nltk_stop_words = set(stopwords.words('english'))

def load_unimportant_words(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    unimportant_words = set() 
    for line in lines:
        unimportant_words.update(line.strip().lower().split())
    return unimportant_words

def process_information(sub, unimportant_words):
    '''
    Read the top 1000 reddit submissions from r/subreddit, and return the dictionary of word with word frequencies,  ignoring words in the unimportant_words set
    '''
    h = dict()
    
    for item in reddit_bot.open_reddit(sub, 1000):
        for line in item:
            # Strip they're in string and split they're in lists
            #line = line.strip(string.punctuation + string.whitespace)
            # Split them into individual words
            #word = line.split()
            #for i in word:
                #i = i.strip(string.punctuation + string.whitespace) # We do not want punctuation and whitespace in our strings
                #i = i.lower()

                #h[i] = h.get(i, 0) + 1
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.lower().split()
            for word in words:
                if word not in unimportant_words:
                    h[word] = h.get(word, 0) + 1
    return h


def total_words(hist):
    '''
    Return the total number in frequencies of histogram.
    '''
    return sum(hist.values())


def different_words(hist):
    '''
    Return the number of different words in the histogram.
    '''
    return len(hist.keys())


#def most_common_words(hist, num, unimportant_words):
   #'''
   # Retun a list of given number of most common words in the histogram by using the histogram and excluding the given list of unimportant words.
    #'''
    #lst = []
    #for word, freq in hist.items():
        #if word not in unimportant_words:
            #lst.append((freq, word))
    #lst.sort(reverse=True)
    #return lst[0:num]

def most_common_words(hist, num):
    lst = sorted(hist.items(), key=lambda item: item[1], reverse=True)
    return lst[:num]



def main():
    unimportant_words = nltk_stop_words.union(load_unimportant_words('data/unimportant_words.txt'))


    histogram_upenn = process_information('upenn', unimportant_words)    # Print a histogram of frequency of words in r/upenn
    histogram_harvard = process_information('harvard', unimportant_words)    # Print a histogram of frequency of words in r/harvard
    histogram_stanford = process_information('yale', unimportant_words)    # Print a histogram of frequency of words in r/stanford
    histogram_yale = process_information('stanford', unimportant_words)    # Print a histogram of frequency of words in r/yale
    histogram_princeton = process_information('princeton', unimportant_words)
    histogram_columbia = process_information('columbia', unimportant_words)
    histogram_brown = process_information('brownU', unimportant_words)
    histogram_cornell = process_information('cornell', unimportant_words)
    histogram_dartmouth = process_information('dartmouth', unimportant_words)
    
    print(f'The total number of words in the top 1000 post of r/upenn is: {total_words(histogram_upenn)}')
    print(f'The total number of words in the top 1000 post of r/harvard is: {total_words(histogram_harvard)}')
    print(f'The total number of words in the top 1000 post of r/yale is: {total_words(histogram_yale)}')
    print(f'The total number of words in the top 1000 post of r/stanford is: {total_words(histogram_stanford)}')
    print(f'The total number of words in the top 1000 post of r/princeton is: {total_words(histogram_princeton)}')
    print(f'The total number of words in the top 1000 post of r/columbia is: {total_words(histogram_columbia)}')
    print(f'The total number of words in the top 1000 post of r/brownU is: {total_words(histogram_brown)}')
    print(f'The total number of words in the top 1000 post of r/cornell is: {total_words(histogram_cornell)}')
    print(f'The total number of words in the top 1000 post of r/dartmouth is: {total_words(histogram_dartmouth)}')
    
    print(f'The number of different words is: {different_words(histogram_upenn)}')

    print(f'The most common words for r/upenn are: {most_common_words(histogram_upenn, 10)}')
    print(f'The most common words for r/harvard are: {most_common_words(histogram_harvard, 10)}')
    print(f'The most common words for r/yale are: {most_common_words(histogram_yale, 10)}')
    print(f'The most common words for r/stanford are: {most_common_words(histogram_stanford, 10)}')
    print(f'The most common words for r/princeton are: {most_common_words(histogram_princeton, 10)}')
    print(f'The most common words for r/columbia are: {most_common_words(histogram_columbia, 10)}')
    print(f'The most common words for r/brownU are: {most_common_words(histogram_brown, 10)}')
    print(f'The most common words for r/cornell are: {most_common_words(histogram_cornell, 10)}')
    print(f'The most common words for r/dartmouth are: {most_common_words(histogram_dartmouth, 10)}')

    print(f'Result of UPenn sentiment analysis: {sentiment_analysis.sentiment("upenn")}')
    print(f'Result of Harvard sentiment analysis: {sentiment_analysis.sentiment("harvard")}')
    print(f'Result of Yale sentiment analysis: {sentiment_analysis.sentiment("yale")}')
    print(f'Result of Stanford sentiment analysis: {sentiment_analysis.sentiment("stanford")}')
    print(f'Result of Princeton sentiment analysis: {sentiment_analysis.sentiment("princeton")}')
    print(f'Result of Columbia sentiment analysis: {sentiment_analysis.sentiment("columbia")}')
    print(f'Result of Brown sentiment analysis: {sentiment_analysis.sentiment("brownU")}')
    print(f'Result of Cornell sentiment analysis: {sentiment_analysis.sentiment("cornell")}')
    print(f'Result of Dartmouth sentiment analysis: {sentiment_analysis.sentiment("dartmouth")}')

    print(text_similarity.compare_subreddit('upenn', 'harvard'))
    print(text_similarity.compare_subreddit('upenn', 'yale'))
    print(text_similarity.compare_subreddit('upenn', 'stanford'))
    print(text_similarity.compare_subreddit('upenn', 'princeton'))
    print(text_similarity.compare_subreddit('upenn', 'columbia'))
    print(text_similarity.compare_subreddit('upenn', 'brownU'))
    print(text_similarity.compare_subreddit('upenn', 'cornell'))
    print(text_similarity.compare_subreddit('upenn', 'dartmouth'))


if __name__ == "__main__":
    main()