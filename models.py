from app import db
from datetime import datetime
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

class Post(db.Model):
    __tablename__ = 'example'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    slub = db.Column(db.String, unique=True)
    body = db.Column(db.Text)
    created =db.Column(db.DateTime, default=datetime.now())


    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)


    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

