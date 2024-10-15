# from fastapi import FastAPI
# from mangum import Mangum

# app = FastAPI()

# # Your routes here
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# # Create the Mangum adapter
# lambda_handler = Mangum(app)
import json

def lambda_handler(event, context):
    name = event.get("queryStringParameters", {}).get("name", "World")
    message = f"Hello, {name}!"
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": message})
    }
