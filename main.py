import uvicorn
from fastapi import FastAPI
from api.api import api_router
from db.session import init_db

app = FastAPI()

app.include_router(api_router, prefix='/api')

init_db()

@app.get("/")
def root():
    return {"message": "API is running. Go to /docs for Swagger UI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)