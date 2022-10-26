import bentoml
from bentoml.io import JSON
from pydantic import BaseModel
from bentoml.io import NumpyNdarray

class UserProfile(BaseModel):
    name: str 
    age: int 
    country: str  
    rating: float


# model_ref = bentoml.xgboost.get("credit_risk_model:yl55uxcvk6elnml3")

# model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5") # 1
model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5") # 2

# dv = model_ref.custom_objects['dictVectorizer']  
model_runner = model_ref.to_runner()    #scale the model separately from the rest of the service

svc = bentoml.Service("credit_risk_model", runners=[model_runner])

# @svc.api(input=JSON(pydantic_model=UserProfile), output=JSON())
@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(vector):
    # application_data = credit_application.dict()
    # vector = dv.transform(application_data)
    prediction = model_runner.predict.run(vector)
    print(prediction)
    return prediction
    # print(prediction, "-----------------------------")
    # result = prediction[0]

    # if result > 0.5:
    #     return {
    #         "status": "DECLINED"
    #     }
    # elif result > 0.25:
    #     return {
    #         "status": "MAYBE"
    #     }
    # else:
    #     return {
    #         "status": "APPROVED"
    #     }