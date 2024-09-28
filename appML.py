import pickle
from fastapi import FastAPI
from asignatura import asignatura
from DiabetesData import DiabetesData
import numpy as np

app = FastAPI()

pkl_filename = "RFDiabetesv102.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ["Sano","Posible diabetes"]

@app.get("/")
async def root():
    return{
        "message":"AI Services"
    }

@app.post("/predict")
def predict_diabetes(data:DiabetesData):
    data = data.model_dump()
    Pregnancies = data['Pregnancies']
    Glucose = data['Glucose']
    BloodPressure = data['BloodPressure']
    SkinThickness = data['SkinThickness']
    Insulin = data['Insulin']
    BMI = data['BMI']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
    Age = data['Age']

    xin = np.array([Pregnancies,
                    Glucose,
                    BloodPressure,
                    SkinThickness,
                    Insulin,
                    BMI, 
                    DiabetesPedigreeFunction,
                    Age]).reshape(1,8)
    
    prediction = model.predict(xin)
    yout = labels[prediction[0]]


    return{
        'prediction': yout
    }