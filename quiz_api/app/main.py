from fastapi import FastAPI
from . import models, routes, database
from .utils import logger

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="AI Quiz Generator API",
    description="A simple API to generate and store quizzes using rule-based 'AI'.",
    version="1.0.0"
)

# Include routers
app.include_router(routes.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up the AI Quiz Generator API...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the AI Quiz Generator API...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
