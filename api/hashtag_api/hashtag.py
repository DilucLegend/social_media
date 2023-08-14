from api import app
from database.postservice import get_all_hashtags
from fastapi import Request

# Poluchit neskolko heshtegov
@app.get('/api/hashtag')
async def get_some_hashtags(size: int = 20, page: int = 1):
    pass

# poluchit foto iz opredelennogo heshtega
@app.get('/api/hashtag/<str:hashtag_name>')
async def get_exact_hashtag(hashtag_name: str):
    pass