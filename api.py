import fastapi
from pydantic import BaseModel
import pickle
import json
import uvicorn

api = fastapi.FastAPI()

class model_input(BaseModel):
    
    pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int       

diabetes_model = pickle.load(open('diabetes_model.pickle', 'rb'))
@api.get("/")
def index():
    """
    Redirect index page to /docs
    """
    return fastapi.responses.RedirectResponse('/docs')

@api.post('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):
    """
    return the diabeties prediction for patient
    """
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

if __name__ == '__main__':
    uvicorn.run(api, host = '127.0.0.1', port=8000)