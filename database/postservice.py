from database.models import Comment, UserPost, Hashtag
from database import get_db
from datetime import datetime

### USERPOST ###
# Функция получения определенного или всех постов function(post_id)
# проверка post_id
def get_all_or_exact_post_db(post_id):
    db = next(get_db())

    # proverka
    if post_id == 0:
        return db.query(UserPost).all()

    return db.query(UserPost).filter_by(id=post_id).first()

# функция изменения текста к посту function(post_id, new_text)
def change_post_text_db(post_id, new_post):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()

    if exact_post:
        exact_post.main_text == new_post

        db.commit()
        return 'Данные успешно изменены'
    return 'Ошибка в данных'

# функция удаления определенного поста function(post_id)
def delete_exact_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    db.delete(exact_post)
    db.commit()

    return 'Данные успешно удалены'



############

### COMMENT ###

# функция получения комментариев определенного поста function(post_id)
def get_all_comments_exact_post_db(post_id):
    db = next(get_db())

    all_comments = db.query(Comment).filter_by(id=post_id).all()

    return all_comments

# функция публикации коментария function(post_id, user_id, text, reg_date)
def add_comment_db(post_id, user_id, text):
    db = next(get_db())

    new_post = Comment(post_id=post_id, user_id=user_id, text=text, reg_date=datetime.now())
    db.add(new_post)
    db.commit()

    return 'Комментарий опубликован'

# функция изменения определенного комментария function(comment_id, new_comment_text)
def change_exact_comment_db(comment_id, new_comment_text):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()

    if exact_comment:
        exact_comment.text == new_comment_text
        db.commit()

        return 'Данные успешно изменены'

    return 'Ошибка в данных'

# Удалить определенный комментарий function(comment_id)
def delete_exact_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    db.delete(exact_comment)
    db.commit()

    return 'Данные успешно удалены'
############

### HASHTAGS ###

# функция получения доступных в базе хештегов function(size) list[:size]
def get_all_hashtags(size):
    db = next(get_db())
    all_hastags = db.query(Hashtag).all()
    return all_hastags[:size]

# функция получения определенного хештега function(hashtag_name)
def get_exact_hashtag(hashtag_name):
    db = next(get_db())

    exact_hashtag = db.query(Hashtag).filter_by(hashtag_name=hashtag_name).first()

    if exact_hashtag:
        return exact_hashtag

    return []