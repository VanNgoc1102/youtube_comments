import json
from typing import Text
from sqlalchemy import create_engine
from sqlalchemy import  MetaData, Table, Column, Integer, String,Text
#from sqlalchemy.orm import mapper
DB_URL= 'mysql+mysqldb://root:110202@localhost/comments'
ENGINE=create_engine(DB_URL)
conn=ENGINE.connect()
try:
    print('-> Your connection ok !\n-> Connection object is :{}'.format(conn) )
except:
    print(' -> Your connec not connected !!')

meta=MetaData()
yt_comment = Table('yt_comment', meta, Column('Kinds',Text),Column('Etags',Text),Column('id',Text), Column('author',Text),
Column('authorChannelUrl',Text), Column('content',Text),Column('published_at',Text), )

meta.create_all(ENGINE)

import json
with open("yt_comments.json","r") as f:
    data=json.load(f)
n=len(data)
for i in range(0,n): 
    conn.execute(yt_comment.insert(), data[i])

#{'Kinds': 'youtube#comment', 'Etags': 'O7obk4RgGXPokkuCXGhIURRSJJI', 'id': 'Ugi1PP2dW44ELHgCoAEC', 'author': 'Николай', 'authorChannelUrl': 'http://www.youtube.com/channel/UC454PYEpMR-fr5OtXFw-BYQ', 'content': 'зверский голос', 'published_at': '2013-12-13T12:18:28Z'}
