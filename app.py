from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI deployed successfully on AWS Lambda "}

handler = Mangum(app)
