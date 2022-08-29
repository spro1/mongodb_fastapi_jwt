from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import auth, user

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=['Auth'], prefix='/api/v1/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/v1/users')


@app.get("/api/v1/check")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}
