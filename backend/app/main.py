from fastapi import FastAPI
from . import __init__
from .routers import auth, products

app = __init__.app
app.include_router(auth.router)
app.include_router(products.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Product RecSys Backend Ready. Docs: /docs, API: /api/products"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

