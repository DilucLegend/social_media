from api import app
from fastapi import Request, Body, UploadFile
from database.photoservice import change_photo_db, delete_photo_db, get_all_or_exact_photo_db

# poluchit vse fotografii
@app.get('/api/photo')
async def get_all_or_exact_photo(photo_id: int = 0, user_id:int = 0):
    pass

# izmenit foto profilya
@app.put('/api/photo')
async def change_profile_photo(photo_id: int = Body(...), photo_file: UploadFile = Body(...)):
    if photo_file:
        # Sohranit foto v papku
        with open(f'{photo_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)

        change_photo_db(photo_id, f'/api/photo_api/photos/{photo_id}.jpg')

    return {'status': 1, 'message': 'Фото успешно изменено'}

# udalit opredelennuyu fotografiyu
@app.delete('/api/photo')
async def delete_user_photo():
    pass

