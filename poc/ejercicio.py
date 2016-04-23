from mongokit import Connection
from mongokit import Connection, Document
import datetime

connection = Connection(host='localhost', port=27017)
DB_NAME = 'blog'

db = connection[DB_NAME]

@connection.register
class BlogPost(Document):
    __collection__ = 'blog_posts'
    __database__ = DB_NAME
    structure = {
        'title': basestring,
        'body': basestring,
        'author': basestring,
        'date_creation': datetime.datetime,
        'rank': int,
        'tags': [basestring],
    }
    required_fields = ['title', 'author', 'date_creation']
    default_values = {
        'rank': 0,
        'date_creation': datetime.datetime.utcnow
    }