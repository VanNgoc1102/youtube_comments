
import json
with open("yt_comments.json","r") as f:
    data=json.load(f)
n=len(data)

for item in range(0,n):
    print(data[item])
#for i in data:
    #print(i)
