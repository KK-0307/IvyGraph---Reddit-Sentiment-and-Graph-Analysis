import praw
import config


def open_reddit(sub, num):
    '''
    Using information in config to retrive information from subreddit. (Works like API)
    '''
    reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)
    print(reddit.user.me())

    submissions = reddit.subreddit(sub).top(limit=num)

    # submissions = reddit.subreddit(sub).top('week', limit=num)
    top1000 = ["{} {}".format(submission.title, submission.selftext).replace('\n', ' ') for submission in submissions]
    return top1000


def main():
    open_reddit('UPenn', 1000)

if __name__ == '__main__':
    main()