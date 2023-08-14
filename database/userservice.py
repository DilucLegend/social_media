from database.models import User
from datetime import datetime

from database import get_db

# registratsiya pozovatelya
def register_user_db(name, email, phone_number, password, user_city):
    db = next(get_db())

    #sozdayom klass novogo polzovatelya
    new_user = User(name=name, email=email, phone_number=phone_number, password=password, user_city=user_city, reg_date=datetime.now())

    # Dobavlyayem v bazu
    db.add(new_user)

    # Sohranyayem v bazu
    db.commit()

    return new_user.id

# proverka na nalichie v baze polzovatelya
def check_user_data_db(phone_number, email):
    db = next(get_db())

    # proverka dannix na nalichie zapisi v baze
    checker = db.query(User).filter_by(phone_number=phone_number, email=email).first()

    # yesli yest sovpadenie
    if checker:
        return False

    # yesli net sovpadeniy
    return True

# proverka parolya polzovatelya pri vhode v akkaunt
def check_user_password_db(email, password):
    db = next(get_db())

    # poprobuyem nayti polzovatelya
    checker = db.query(User).filter_by(email=email).first()

    # yesli nashel takoy meyl, proveryayem pravilnost parolya
    if checker:
        # Nachinayem sverku parolya
        if checker.password == password:
            return checker.id

        else:
            return 'Неверный пароль'

    # yesli ne nahodit dannie v baze
    return 'Неверные данные'

# poluchit informatsiyu o polzovatele
def profile_info_db(user_id):
    db = next(get_db())

    # nahodim polzovatelya cherez id
    exact_user = db.query(User).filter_by(id=user_id).first()

    # yesli nashel polzovatelya, peredayu informatsiyu pro nego
    if exact_user:
        return exact_user.email, exact_user.phone_number, exact_user.user_city, exact_user.id, exact_user.name, exact_user.reg_date

    return "Пользователь не найден"

# izmenenie dannix polzovatelya
def change_user_data(user_id, change_info, new_data):
    db = next(get_db())

    # Nahodim polzovatelya v baze
    exact_user = db.query(User).filter_by(id=user_id).first()

    # Yesli yest polzovatel v baze
    if exact_user:
        # proverka togo, kakuyu informatsiyu hochet izmenit polzovatel
        if change_info == 'email':
            exact_user.email == new_data

        elif change_info == 'number':
            exact_user.phone_number == new_data

        elif change_info == 'name':
            exact_user.name == new_data

        elif change_info == 'city':
            exact_user.user_city == new_data

        elif change_info == 'password':
            exact_user.password == new_data

        # Sohranyayem izmenenie v baze
        db.commit()

        return 'Данные успешно изменены'

    # a yesli ne nahodim polzovatelya
    return