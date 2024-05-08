import os
import pandas as pd
import pickle
from fastapi import FastAPI, HTTPException
import uvicorn
import sqlite3

app = FastAPI()

conn = sqlite3.connect('Advertising.db')
cursor = conn.cursor()

@app.get('/')
async def home():
    return "Bienvenido a la API del modelo Advertising"

@app.get('/predict')
async def predict(data:dict):
    model = pickle.load(open('../data/advertising_model.pkl','rb'))

    prediction = model.predict([[data['data'][0][0],data['data'][0][1],data['data'][0][2]]])

    return {'prediction' : round(prediction[0], 2)}


@app.post('/ingest')
async def ingest_data(data:dict):
    for x in data['data']:
        cursor.execute('''INSERT INTO Ventas (TV, radio, newspaper, sales)
                       VALUES (?,?,?,?)''', (x[0],x[1],x[2],x[3]))
        conn.commit()
    return {'message': 'Datos ingresados correctamente'}
    
@app.post ('/retrain')
async def retrain():
    model = pickle.load(open('../data/advertising_model.pkl','rb'))
    def sql_query(query):

        cursor.execute(query)

        ans = cursor.fetchall()

        names = ["TV","radio", "newspaper", "sales"]

        return pd.DataFrame(ans,columns=names)
    
    query='''SELECT * FROM Ventas;'''
    df= sql_query(query)

    X_train = df[['TV','radio','newspaper']]
    y_train= df['sales']
    model.fit(X_train,y_train)
    
    return {'message': 'Modelo reentrenado correctamente.'}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



