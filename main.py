import tkinter as tk
import scraper
from scraper import browse_subreddit

root = tk.Tk()
root.geometry("1200x650")

def select_subreddit(sub):
    results = browse_subreddit(sub)
    for n in range(len(results)+1):
        for i in results.values():
            show_content.insert(tk.INSERT,i[n])
            show_content.insert(tk.INSERT,"\n----------\n")
search_frame = tk.Frame(root,bg="#121212")
search_frame.place(relx=0.5,rely=0.05,relheight=0.05,relwidth=0.8,anchor="n")

search_entry = tk.Entry(search_frame,font=("Helvetica",12))
search_entry.place(relx = 0.05,relheight=1,relwidth=0.65)

sub_search_button = tk.Button(search_frame,bg="#4700b3",text = "choose this subreddit",command=lambda : select_subreddit(search_entry.get()) )
sub_search_button.place(relx=0.75,relheight=1,relwidth = 0.15)

show_frame = tk.Frame(root,bg = "#121212")
show_frame.place(relx = 0.07,rely=0.15,relwidth=0.85,relheight=0.8)

show_content = tk.Text(show_frame,bg="#121212",fg="#cccccc")
show_content.place(relheight=1,relwidth=1)

root.mainloop()