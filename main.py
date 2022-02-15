import pytube
from tkinter import *
import tkinter.filedialog
import os

# Program to download a youtube video/playlist
root = Tk()
root.withdraw()

urls = ["https://youtu.be/6mbwJ2xhgzM?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg", "https://youtu.be/WonrDQAABMY?list=PLu0W_9lII9agrsRZjFECeFuWY5ev2pQlk", 
        'https://youtu.be/sSLGP-_2gOI?list=PLu0W_9lII9aiQiOwthuSvinxoflmhRxM3', 'https://youtu.be/evknSAkUIvs?list=PLu0W_9lII9agwhy658ZPA0MTStKUJTWPi', 
        'https://youtu.be/5BDgKJFZMl8?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9', 'https://youtu.be/JqS6BcgeUMw?list=PLu0W_9lII9agAiWp6Y41ueUKx1VcTRxmf']

for url in urls:
    file_path = tkinter.filedialog.askdirectory()
    # playlist_url = input("Enter URL of youtube video/playlist to download: ")
    playlist_url = url
    p = pytube.Playlist(playlist_url)
    print(f'Downloading: {p.title}')
    s = pytube.streams
    dest_path = ""
    for index, video in enumerate(p.videos):
        s = video.streams.get_by_resolution("720p")
        print(f'Downloading ---## {s.title} ##---')
        dest_path = s.download(file_path, filename_prefix=f'{index + 1}. ', max_retries=5)
        if os.path.isfile(dest_path):
            print("File downloaded successfully\n")
        else:
            print("Error downloading file\n")

# # CWH Tutorials
# Web dev playlist https://youtu.be/6mbwJ2xhgzM?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg
# Cheatsheet playlist https://youtu.be/WonrDQAABMY?list=PLu0W_9lII9agrsRZjFECeFuWY5ev2pQlk
# Projects using HTML, CSS, JS https://youtu.be/sSLGP-_2gOI?list=PLu0W_9lII9aiQiOwthuSvinxoflmhRxM3
# Git playlist https://youtu.be/evknSAkUIvs?list=PLu0W_9lII9agwhy658ZPA0MTStKUJTWPi
# Django playlist https://youtu.be/5BDgKJFZMl8?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9
# Flask playlist https://youtu.be/JqS6BcgeUMw?list=PLu0W_9lII9agAiWp6Y41ueUKx1VcTRxmf

# # Apna College
# Web dev playlist https://youtu.be/l1EssrLxt7E?list=PLfqMhTWNBTe3H6c9OGXb5_6wcc1Mca52n


'''Downloading a video with highest resolution

video = pytube.YouTube("https://www.youtube.com/watch?v=JFF2vJaN0Cw&list=PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_")
print(f'Downloading video "{video.streams.get_highest_resolution().title}" with '
      f'resolution: {video.streams.get_highest_resolution().resolution}')
video.streams.get_highest_resolution().download()'''
