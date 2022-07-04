
import json

import requests
VIDEO_ID=input("Enter ID: ")
URL="https://www.googleapis.com/youtube/v3/commentThreads"
API_KEY="AIzaSyBZnBVHK5L57k4cwbEVPN7GXMKHOlmnW3U"
#VIDEO_ID="tlcWiP7OLFI&list=PLhBgTdAWkxeCL3bUv6NLGrg2248ryIUAD"
response=requests.get(f"{URL}?key={API_KEY}&videoId={VIDEO_ID}&part=snippet&part=replies")# add replies
data=json.loads(response.text)
#print(data)
print()
comments=[]
while True:    
   
    for item in data["items"]:
        author=item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        content=item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        published_at=item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
        
        comments.append({
            "author": author,
            "content": content,
            "published_at":published_at,       

        })
      
    if "nextPageToken" in data:
        page_token=data["nextPageToken"]
        response=requests.get(f"{URL}?key={API_KEY}&videoId={VIDEO_ID}&part=snippet&part=replies&pageToken={page_token}")
        data=response.json()
    else:
        break

print(comments)

with open('new_comments.json','w',encoding='utf-8') as f:
    json.dump(comments,f,indent=4)
print("Count CommentsThreads:",len(comments),"comments")

print("END!")