from fastapi import FastAPI
from database import Base, engine

# Sozdanie tablits v baze dannih
Base.metadata.create_all(bind=engine)
app = FastAPI()

from api.comments_api import comments
from api.hashtag_api import hashtag
from api.photo_api import photo
from api.users_api import users
from api.posts_api import posts