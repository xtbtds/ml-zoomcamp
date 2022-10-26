1. 1.0.7

2. `bentoml models list`   
 Answer: 197.77 KiB



3. 
```
class UserProfile(BaseModel):
    name: str 
    age: int 
    country: str  
    rating: float
```
4. `cat ~/bentoml/models/mlzoomcamp_homework/qtzdz3slg6mwwdu5/model.yaml`  
Answer: 1.1.1

5.  *What did we change for this question:*
    1. `model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")`
    2. `@svc.api(input=NumpyNdarray(), output=NumpyNdarray())`
    3. `prediction = model_runner.predict.run(vector)  `

    Answer: 1  

6. *Test for 10000 users, 1000 user per second; look at notebook "Question7_statistics"*  
    Answer: 1
