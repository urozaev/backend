from peewee import *
from datetime import date

psql_db = PostgresqlDatabase(
    'usersdb',
    user ='urozaev',
    password ='postgres',
    host ='127.0.0.1')


def init_tables():
    psql_db.create_tables([urozaevModel], safe = True)
    
    
class BaseModel(Model):
    class Meta:
        database = psql_db


class urozaevModel(BaseModel):
    name = CharField()
    birthday = DateField()
    phone = CharField()
    role = CharField()
    isArchive = BooleanField()

    
def create_user(user_name, user_birthday, user_phone, user_role, user_isArchive):
    urozaevModel.create (
        name = user_name,
        birthday = user_birthday,
        phone = user_phone, 
        role = user_role, 
        isArchive = user_isArchive
    )

def get_user(user_id):
    user = urozaevModel.get(urozaevModel.id == user_id)
    return user

def update_user(user_id):
    user = urozaevModel.select().where(urozaevModel.id == user_id).get()
    return user

def delete_user(user_id):
    user = urozaevModel.get(urozaevModel.id == user_id)
    user.delete_instance()