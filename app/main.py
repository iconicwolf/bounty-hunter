from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import profile, applications, filters, agents
from app.db import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BountyHunter API",
    description="Agentic Career Application Tracker & Automator",
    version="0.1.0"
)

# Mount static files for evidence capture
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(profile.router)
app.include_router(applications.router)
app.include_router(filters.router)
app.include_router(agents.router)

@app.get("/")
async def root():
    return {"message": "Welcome to BountyHunter API. Visit /docs for documentation."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
