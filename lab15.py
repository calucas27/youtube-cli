import requests
from bs4 import BeautifulSoup

target_url="https://www.youtube.com"
target_search="/results?search_query="

count = 1

print(" ")

print("=============")
print("Welcome to youtube-cli!")
print("You can get started by entering a video you want to search for.")
print("==============")

print(" ")

target_video = input("Search for a video: ")

print(" ")

target_video = target_video.replace(" ","+")

search_url = target_url + target_search + target_video
search_get = requests.get(search_url)

#use bs4 to parse the data from requests
soup = BeautifulSoup(search_get.content,"html.parser")
videos = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})

for video in videos:
	video_href = video.get("href")
	video_title = video.get("title")
	video_fullurl = target_url + video_href
	print(" ")
	print("Result #" + str(count) + ":" + " " +  video_title)
	print(video_fullurl)
	count = count + 1
print(" ")
