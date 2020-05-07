 
import requests,webbrowser 
from bs4 import BeautifulSoup
from bs4 import *

search = input(" -------   ENTER ------------- \n \t ")
new_search=''
for sec in search:
	if se!=' ':
		new_search+=sec
	else:
		new_search+='+'
## url of searced 
url=f'https://www.youtube.com/results?search_query={new_search}'
req=requests.get(url)
soup=BeautifulSoup(req.text,'html.parser')



## link of videos  
a_tags = soup.find_all('a',class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link')
vid_link=[]
for vid in a_tags:
	vid_link.append('https://www.youtube.com'+vid['href'])

### durition and title  
title_list = []
duration_list = []
video_title=soup.find_all('h3',class_='yt-lockup-title')
for i in video_title:
	p=(i).text.split('Duration')
	title_list.append(p[0])
	try:
		duration_list.append('Duration   :  '+p[1][1:])
	except IndexError:
		duration_list.append("----")



count = 1
for num in range(len(video_title)):
	print(count,".","\n \t",title_list[num])
	print("\t\t",duration_list[num])
	print("_______"*10)

	count+=1
#####  choose of video you want toplay

user_input=int(input("enter no. of video u want to play"))
play=webbrowser.open(vid_link[user_input-1])
print('enjoy your song ThaNk yOu')