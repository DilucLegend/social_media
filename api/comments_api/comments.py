from api import app
from fastapi import Request
from database.postservice import get_all_comments_exact_post_db, change_exact_comment_db, \
    delete_exact_comment_db, add_comment_db


# poluchit kommentarii opredelenngo posta
@app.get('/api/comment')
async def get_exact_post_comments(request: Request):
    # Poluchit json so vsemi dannimi kotorie prishli iz front
    data = await request.json()

    # poluchit klyuch post_id iz dati
    post_id = data.get('post_id')

    if post_id:
        # Poluchayem dannie iz bazi
        exact_post_comments = get_all_comments_exact_post_db(post_id)

        return {'status': 1, 'message': exact_post_comments}
    return {'status': 0, 'message': 'неверный ввод данных'}

# Opublikovat komentariy k postu
@app.post('/api/comment')
async def public_comment():
    pass

# izmenit tekst komentariy
@app.put('app/comment')
async def change_exact_user_comment():
    pass

# udalit tekst komentariy
@app.put('app/comment')
async def delete_exact_user_comment():
    pass