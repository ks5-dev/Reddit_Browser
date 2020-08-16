import tkinter as tk
import scraper
from scraper import browse_subreddit,download_png,download_jpg
import os

def make_menu(w):
    global the_menu
    the_menu = tk.Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


root = tk.Tk()
root.geometry("1200x700")

'''
Handling the select subreddit button, write the content found to a file, then display it on the show content frame
'''
def select_subreddit(sub):
    show_content.delete('1.0', tk.END)
    with open("latest_search.txt","w") as f:
        f.close()
    with open("read_comments.txt","w") as f:
        f.close()
    results = browse_subreddit(sub)
    for n in range(len(results)+1):
        for i in results.values():
            with open("latest_search.txt","a") as f:
                f.write(str(i[n]))
                f.write("\n")
    with open("latest_search.txt","r") as f: 
        show_content.insert(tk.INSERT,f.read())

# --search bar--
search_frame = tk.Frame(root,bg="#121212")
search_frame.place(relx=0.5,rely=0.05,relheight=0.05,relwidth=0.8,anchor="n")

search_entry = tk.Entry(search_frame,font=("Helvetica",12))
search_entry.place(relx = 0.05,relheight=1,relwidth=0.65)

sub_search_button = tk.Button(search_frame,bg="#4700b3",text = "choose this subreddit",command=lambda : select_subreddit(search_entry.get()) )
sub_search_button.place(relx=0.75,relheight=1,relwidth = 0.15)

# --content--
show_frame = tk.Frame(root,bg = "#121212")
show_frame.place(relx = 0.07,rely=0.15,relwidth=0.85,relheight=0.7)

show_content = tk.Text(show_frame,bg="#121212",fg="#cccccc")
show_content.place(relheight=1,relwidth=1)

get_png_resource = tk.Button(root,bg="#4700b3",text="get png images",command=download_png)
get_png_resource.place(relx= 0.15, rely=0.9,relwidth=0.15,relheight=0.05)

get_png_resource = tk.Button(root,bg="#4700b3",text="get jpg images",command=download_jpg)
get_png_resource.place(relx= 0.3, rely=0.9,relwidth=0.15,relheight=0.05)

make_menu(root)
e1 = tk.Entry()

e1.place(relx=0.3,relwidth=0.4)
e1.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)

root.mainloop()