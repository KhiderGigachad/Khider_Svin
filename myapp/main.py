from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def main_page()-> str:
    return "Это главная страница"

