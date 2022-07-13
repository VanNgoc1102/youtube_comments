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

'''from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo=True)
meta=MetaData()
students = Table('students', meta, Column('id', Integer, primary_key=True), 
Column('name', String), Column('lastname', String), )
meta.create_all(engine)
'''






