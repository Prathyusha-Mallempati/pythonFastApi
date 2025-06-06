from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from datetime import datetime, timedelta
from ..token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
   tags=['Authentication'] 
)

@router.post('/login')
async def login(request: OAuth2PasswordRequestForm  = Depends(), db: Session = Depends(database.get_db)):
   user = db.query(models.User).filter(models.User.email == request.username).first()
   if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with email {request.username} not found")
   if not Hash.verify(user.password, request.password):
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
   # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)    
   access_token = create_access_token(
        data={"sub": user.email}
   )
   return {"access_token":access_token, "token_type" : "bearer"}
   # return user 

