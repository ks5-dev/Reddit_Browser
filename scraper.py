import praw

def browse_subreddit(sub):
    reddit = praw.Reddit(client_id='', 
                     client_secret='', 
                     user_agent='Reddit_Browser', 
                     username='', 
                     password='')
    subreddit = reddit.subreddit(sub)
    submissions = subreddit.hot(limit=5)
    submission_data = {"title":[],"url":[],"score":[],"body":[]}
    for submission in submissions:
        submission_data["title"].append(submission.title)
        submission_data["url"].append(submission.url)
        submission_data["score"].append(submission.score)
        submission_data["body"].append(submission.selftext)
    return submission_data
