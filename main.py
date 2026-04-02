from fastapi import FastAPI, routing


app = FastAPI()

@app.get('/')
def index():
    return {'hello': 'world'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}