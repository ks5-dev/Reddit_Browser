import praw
import re
import os
import requests

reddit = praw.Reddit(client_id='', 
                     client_secret='', 
                     user_agent='Reddit_Browser', 
                     username='', 
                     password='')

submission_data = {"title":[],"url":[],"score":[],"body":[]}
def browse_subreddit(sub):
    subreddit = reddit.subreddit(sub)
    submissions = subreddit.hot(limit=5)
    for submission in submissions:
        submission_data["title"].append(submission.title)
        submission_data["url"].append(submission.url)
        submission_data["score"].append(submission.score)
        submission_data["body"].append(submission.selftext)
        for comment in submission.comments:
            with open("read_comment.txt","a") as f:
                f.write(comment.body)
                f.write("\n")
                f.write(str(comment.author))
                f.write("\n")
                f.write(str(comment.score))
                f.write("\n")
        
    return submission_data

def create_png_file(num):
    img = open("img"+str(num)+".png","w")
    return "img"+str(num)+".png"
def write_png(file,link):
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
    for num,png_file in enumerate(img_link) :
        write_png(create_png_file(num),png_file)

def create_jpg_file(num):
    img = open("img"+str(num)+".jpg","w")
    return "img"+str(num)+".jpg"
def write_jpg(file,link):
    img = requests.get(link)
    open(file,'wb').write(img.content)

def download_jpg():
    img_link = []
    if os.stat("latest_search.txt").st_size > 0 :
        with open("latest_search.txt","r") as r:
            for line in r.readlines():
                res = re.findall(r'(https?://\S+\.jpg)',line)
                if len(res)>0:
                    img_link.append(res[0])
    else:
        print("this file is empty")
    for num,jpg_file in enumerate(img_link) :
        write_jpg(create_jpg_file(num),jpg_file)

