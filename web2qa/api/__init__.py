from fastapi import FastAPI
import uvicorn


from .routers import status, crawler

app = FastAPI(
    title="Web2QA API",
    description="Answere queries with your web content",
    version="0.1.0",
)


app.include_router(status.router)
app.include_router(crawler.router)

@app.get("/")
async def root():
    return {"message": "Web2QA API"}

def start_dev():
    uvicorn.run("web2qa.api:app", host="0.0.0.0", port=8000, reload=True)