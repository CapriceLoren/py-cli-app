from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('notes', user='caprice', password='password', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Note(BaseModel):
  title = CharField()
  body = CharField()

db.connect()
db.drop_tables([Note])
db.create_tables([Note])

Note(title='to do', body='code, learn python').save()
Note(title='shopping list', body='chick peas, lemons, tahini').save()
Note(title = input("Note Title: "), body = input("Note Body: ")).save()
result1 = [model_to_dict(note) for note in Note.select()]
print(f"all notes: {result1}")