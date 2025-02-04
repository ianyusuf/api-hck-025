from fastapi import FastAPI
import pandas as pd

# Create API object
app = FastAPI()

# Read data
data = pd.read_csv('data.csv')

# Coba root home API (get)
@app.get("/")
def root():
    return {'message': 'Hello World'}

# Endpoint sapaan
@app.get("/name/{name}")
def greet(name):
    return {'message': f'Hi {name}, how are you?'}
    
# http://127.0.0.1:8000/name/ian

# Endpoint return data
@app.get("/data")
def get_data():
    return data.to_dict(orient='records')

# http://127.0.0.1:8000/data

# Get data by id
@app.get("/data/{id}")
def search_data(id:int):
    result = data[data['id']==id]
    return {'result': result.to_dict(orient='records')}

# http://127.0.0.1:8000/data

# Menambahkan data
# @app.post("/data/{new_data}")
# def add_data(data:dict):
#     new_data = new_data.string('-')
#     new_row = {'id':new_data[0],
#         'nama':new_data[1],
#         'age':new_data[2],
#         'job':new_data[3]}
#     new_row = pd.DataFrame([new_row])
#     data = pd.concat([data, new_row],ignore_index=True)
#     return {'message':'data id updated !'}