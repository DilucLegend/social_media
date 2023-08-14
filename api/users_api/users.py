from fastapi import Request
from pydantic import BaseModel
from typing import List, Dict

from database.userservice import (register_user_db,
                                  check_user_data_db,
                                  check_user_password_db,
                                  change_user_data,
                                  profile_info_db)
from api import app


# Proverka pochti
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False


# model polzovatelya
class User(BaseModel):
    name: str
    email: str
    phone_number: str
    password: str
    user_city: str


# registratsiya polzovately
@app.post('/api/registration')
async def register_user(user_model: User):
    user_data = dict(user_model)
    # Validatsiya peredennoy pochti
    mail_validation = mail_checker(user_model.email)

    # Yesli net oshibok
    if mail_validation:
        try:
            reg_user =register_user_db(**user_data)

            return {'status': 1, 'user_id': reg_user}
        except Exception as e:
            return {'status': 0, 'message': e}
    # Yesli oshibka v pochte
    return {'status': 1, 'message': 'Invalid email'}

# Poluchit dannie polzovatelya po user_id
@app.get('/api/user')
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id)

    return {'status': 1, 'message': exact_user}

# Vhod v akkaunt
@app.post('/api/login')
async def login_user(email: str, password: str):
    # Validatsiya peredennoy pochti
    mail_validation = mail_checker(email)

    if mail_validation:
        login_checker = str(check_user_password_db(email, password))

        # Yesli vse dannie verni
        if login_checker.isdigit():
            return {'status': 1, 'user_id': int(login_checker)}

        return {'status': 1, 'message': login_checker}
    return {'status': 1, 'message': 'Invalid email'}
# Izmenenie dannix o polzovatele
@app.put('/api/change-profile')
async def change_user_profile(user_id: int, change_info: str, new_data: str):
    data = change_user_data(user_id, change_info, new_data)

    return {'status': 1, 'message': data}