from datetime import datetime
from typing import Optional, List

import pydantic
from fastapi import Form
from pydantic import BaseModel, Json
from fastapi import FastAPI,APIRouter, Depends, File, Form, UploadFile, Query


    
class EventSchema(BaseModel):
    name: str
    date: datetime
    location: str
    available_tickets: int



class CreateBookingSchema(BaseModel):
    num_tickets: int

