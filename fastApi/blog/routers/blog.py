from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List
from .. import models, schemas,database, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)


@router.get('/', response_model=list[schemas.ShowBlog])
async def get_blogs(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blogs = db.query(models.Blog).all()
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_blog(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog,
    return blog.create(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
async def get_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # return blog
    return blog.get(id, db)
 
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # db.delete(blog)
    # db.commit()
    # return Response(status_code=status.HTTP_204_NO_CONTENT, content="Blog deleted successfully")
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # existing_blog = blog.first()
    # existing_blog.title = request.title
    # existing_blog.body = request.body
    # db.commit()
    # return "Blog updated successfully"
    return blog.update(id, request, db)


