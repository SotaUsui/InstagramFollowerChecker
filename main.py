# Get Instagram user data as a JSON file


import json
import tkinter as tk

def load_file(file):
    following = file + "/connections/followers_and_following/following.json"
    followers = file + "/connections/followers_and_following/followers_1.json"
    with open(following, "r", encoding="utf-8") as f:
        following_data = json.load(f)       # should be dict?

    with open(followers, "r", encoding="utf-8") as f:
        followers_data = json.load(f)       # should be dict?

    return following_data, followers_data
def load_file2(file):
    following = file + "/followers_and_following/following.json"
    followers = file + "/followers_and_following/followers_1.json"
    with open(following, "r", encoding="utf-8") as f:
        following_data = json.load(f)       # should be dict?

    with open(followers, "r", encoding="utf-8") as f:
        followers_data = json.load(f)       # should be dict?

    return following_data, followers_data


def get_following(data):
    usernames = [u['value'] for item in data['relationships_following'] for u in item['string_list_data']]
    return usernames

def get_followers(data):
    usernames = [u['value'] for item in data for u in item['string_list_data']]
    return usernames

def get_notFollowingBack(a, b):
    return set(a) - set(b)

def showing(usernames):
    root = tk.Tk()
    root.title("Not Following Back")

    # Use Listbox
    listbox = tk.Listbox(root, width=30, height=75)
    listbox.pack(padx=10, pady=10)

    for user in usernames:
        listbox.insert(tk.END, user)

    root.mainloop()
    pass


file_path = input("Enter path to the file: ").strip()
file_type = int(input("1. has whole contents\n2. has only connections\n -:"))

if file_type == 1:
    following_data, followers_data = load_file(file_path)
else:
    following_data, followers_data = load_file2(file_path)

# get list of usernames
list_following = get_following(following_data)
list_followers = get_followers(followers_data)

# get usernames that not following back
ass = get_notFollowingBack(list_following, list_followers)
showing(ass)