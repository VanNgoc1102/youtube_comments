import json
import requests
#VIDEO_ID=input("Enter ID: ")
URL="https://www.googleapis.com/youtube/v3/commentThreads"
API_KEY="AIzaSyBZnBVHK5L57k4cwbEVPN7GXMKHOlmnW3U"

VIDEO_ID="tlcWiP7OLFI&list=PLhBgTdAWkxeCL3bUv6NLGrg2248ryIUAD"


response=requests.get(f"{URL}?key={API_KEY}&videoId={VIDEO_ID}&part=snippet&part=replies")# add replies
data=json.loads(response.text)
#print(data)
print()
comments=[]
while True:    
   
    for item in data["items"]:
        Kinds=item["snippet"]["topLevelComment"]["kind"]
        Etags=item["snippet"]["topLevelComment"]["etag"]
        id=item["snippet"]["topLevelComment"]["id"]
        author=item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        authorChannelUrl=item["snippet"]["topLevelComment"]["snippet"]["authorChannelUrl"]
        content=item["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        published_at=item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
       
        comments.append((Kinds,Etags, id,author,authorChannelUrl,content,published_at,))
      
    if "nextPageToken" in data:
        page_token=data["nextPageToken"]
        response=requests.get(f"{URL}?key={API_KEY}&videoId={VIDEO_ID}&part=snippet&part=replies&pageToken={page_token}")
        data=response.json()
    else:
        break
n=len(comments)

print(comments[2])
for i in comments:
    print(i)