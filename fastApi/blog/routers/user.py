from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List
from .. import models, schemas,database, oauth2
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["users"]
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # new_user = models.User(**request.dict(exclude = {"password"}))
    # new_user.password = Hash.bcrypt(request.password)
    # db.add(new_user)
    # db.commit() 
    # db.refresh(new_user)
    # return new_user
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
async def get_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    # return user
    return user.get_user(id, db)