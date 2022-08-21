#from click import echo
from sqlalchemy import create_engine

DB_URL= 'mysql://root:110202@localhost/comments'
ENGINE=create_engine(DB_URL)

conn=ENGINE.connect()
try:
    print('-> Your connection ok !\n-> Connection object is :{}'.format(conn) )
except:
    print(' -> Your connec not connected !!')
result = conn.execute("SELECT * FROM yt_comments")

for data in result:
    print(data)
