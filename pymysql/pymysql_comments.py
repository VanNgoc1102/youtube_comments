import json

import requests
import pymysql
#create db 
'''
conn = pymysql.connect(host='localhost',user='root',password='110202',db='')
cursor=conn.cursor()

query = "CREATE DATABASE comments"
cursor.execute(query)
'''
#connect mysql

conn=pymysql.connect(host='localhost',user='root',password='110202',db='comments')
cursor=conn.cursor()
try:
    print('-> Your connection successfully ' )
except:
    print(' -> Your connec not connected !!')

#drop table comment_yt 
cursor.execute("DROP TABLE IF EXISTS comment_yt")
#creat comment_yt new
mySql_Create_Table_Query ='''CREATE TABLE comment_yt(
                        Kinnds longtext,
                        Etags longtext,
                        id longtext,
                        author longtext,
                        authorChannelUrl longtext,
                        content longtext,
                        published_at longtext)'''
                    
cursor.execute(mySql_Create_Table_Query)

#get comment youtube
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

n=len(comments)
#print(n)
#rint(comments[1])

#insert comment youtube vào table comment_yt
for i in range(0,n):
   sql="INSERT INTO comment_yt(Kinnds,Etags,id,author,authorChannelUrl,content,published_at) VALUES(%s,%s,%s,%s,%s,%s,%s)"
   cursor.execute(sql,comments[i])
   conn.commit()
conn.close()
