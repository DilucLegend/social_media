from api import app
from fastapi import Request
from database.postservice import get_all_or_exact_post_db, change_post_text_db, delete_exact_post_db

# poluchit vse posts
@app.get('/api/post')
async def get_all_or_exact_post(post_id: int = 0):
    if post_id:
        get_post = get_all_or_exact_post_db(post_id)
        return {'status': 1, 'message': get_post}
    return {'status': 0, 'message': 'неверный ввод данных'}

# izmenit post
@app.put('/api/post')
async def change_user_post(request: Request):
    # Poluchit json so vsemi dannimi kotorie prishli iz front
    data = await request.json()

    # poluchit klyuch post_id iz dati
    post_id = data.get('post_id')
    new_post = data.get('new_post')

    if post_id and new_post:
        change_post = change_post_text_db(post_id, new_post)
        return {'status': 1, 'message': change_post}
    return {'status': 0, 'message': 'неверный ввод данных'}


# udalenie posta
@app.delete('/api/post')
async def delete_user_post(request: Request):
    # Poluchit json so vsemi dannimi kotorie prishli iz front
    data = await request.json()

    # poluchit klyuch post_id iz dati
    post_id = data.get('post_id')

    if post_id:
        delete_post = delete_exact_post_db(post_id)
        return {'status': 1, 'message': delete_post}
    return {'status': 0, 'message': 'неверный ввод данных'}
