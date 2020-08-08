import praw
import re
import os
import requests

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

def create_img_file(num):
    img = open("img"+str(num)+".png","w")
    return "img"+str(num)+".png"
def write_img(file,link):
    img = requests.get(link)
    open(file,'wb').write(img.content)



def download_png():
    img_link = []
    if os.stat("latest_search.txt").st_size > 0 :
        with open("latest_search.txt","r") as r:
            for line in r.readlines():
                res = re.findall(r'(https?://\S+\.png)',line)
                if len(res)>0:
                    img_link.append(res[0])
    else:
        print("this file is empty")
    for num,img_file in enumerate(img_link) :
        write_img(create_img_file(num),img_file)

