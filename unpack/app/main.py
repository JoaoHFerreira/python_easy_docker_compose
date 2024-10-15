from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# Your routes here
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Create the Mangum adapter
lambda_handler = Mangum(app)
