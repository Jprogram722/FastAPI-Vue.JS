# this file will contain the api links for users

import sys

sys.path.append("../")

from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
import models, shemas, crud
from database import get_db

router = APIRouter()