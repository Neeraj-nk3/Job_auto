from fastapi import FastAPI

app=FastAPI(title="job_auto")

@app.get("/", tags=["Root"])
def read_root():
    return {"message":"Welcone to job auto"}