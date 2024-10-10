import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique = True)
    password = Column(String(256), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,

        }

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    post_media = Column(String(512), nullable=False)
    post_text = Column(String(250), nullable=True)
    post_user_id = Column(Integer,ForeignKey('user.id'))
    comments = relationship("Comment", backref= "post")
    likes =relationship("PostLike", backref= "post")

class PostLike(Base):
    __tablename__ = "post_like"
    id = Column(Integer, primary_key=True)
    user_post_like_id = Column(Integer,ForeignKey('user.id'))
    post_id = Column(Integer,ForeignKey('post.id'))
    
class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    post_comment = Column(String(500), nullable=False)
    user_comment_id = Column(Integer,ForeignKey('user.id'))
    post_id = Column(Integer,ForeignKey('post.id'))
    likes =relationship("CommentLike", backref= "comment")
    dislikes =relationship("CommentDislike", backref= "comment")

class CommentLike(Base):
    __tablename__ = "comment_like"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    comment_id = Column(Integer,ForeignKey('comment.id'))

class CommentDislike(Base):
    __tablename__ = "comment_dislike"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    comment_id = Column(Integer,ForeignKey('comment.id'))
    
    
    
    





    

   #POST , Post like ,comment table , comment like, comment distlike.

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
