from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bai2 import query_bai2


# Create FastAPI instance

app = FastAPI()


# Add CORS middleware

origins = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


# API endpoint

@app.get('/query/')
async def query(question: str = None):
    result = query_bai2(question)
    return result