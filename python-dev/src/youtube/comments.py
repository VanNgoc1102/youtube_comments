import json

import requests

def get_api():
    with open('youtube_comments/api_file.json', 'r') as openfile:
    # Reading from json file
        json_object = json.load(openfile)
        return json_object

API_KEY = get_api().get('API_KEY')
VIDEO_ID=input("VIDEO_ID : ")
URL="https://www.googleapis.com/youtube/v3/commentThreads"

#VIDEO_ID="tlcWiP7OLFI&list=PLhBgTdAWkxeCL3bUv6NLGrg2248ryIUAD"

response=requests.get(f"{URL}?key={API_KEY}&videoId={VIDEO_ID}&part=snippet&part=replies")# add replies
data=json.loads(response.text)
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
       
        #comments.append((Kinds,Etags, id,author,authorChannelUrl,content,published_at,authorChannelUrl,))
        comments.append({
        "Kinds": Kinds,
        "Etags": Etags, 
        "id": id,
        "author": author,  
        "authorChannelUrl": authorChannelUrl,  
        "content": content,  
        "published_at":  published_at,  
 #"replies": replies,  
  })
    
      
    if "nextPageToken" in data:
        page_token=data["nextPageToken"]
        response=requests.get(f"{URL}?key={API_KEY}&videoId={VIDEO_ID}&part=snippet&part=replies&pageToken={page_token}")
        data=response.json()
    else:
        break
print()
print("Count CommentsThreads:",len(comments),"comments")
print(comments)


    