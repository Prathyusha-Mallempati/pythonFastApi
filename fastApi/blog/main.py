from fastapi import FastAPI, HTTPException, Depends, Response, status
from . import schemas, models
from .database import engine, SessionLocal, get_db
from sqlalchemy.orm import Session
from .hashing import Hash
from .routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)





# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()



# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=["blogs"])
# async def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog,

# @app.get('/blog', response_model=list[schemas.ShowBlog], tags=["blogs"])
# async def get_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog, tags=["blogs"])
# async def get_blog(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     return blog
 
# @app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
# async def delete_blog(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     db.delete(blog)
#     db.commit()
#     return Response(status_code=status.HTTP_204_NO_CONTENT, content="Blog deleted successfully")


# @app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
# async def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
#     existing_blog = blog.first()
#     existing_blog.title = request.title
#     existing_blog.body = request.body
#     db.commit()
#     return "Blog updated successfully"



# @app.post('/user', response_model=schemas.ShowUser, tags=["users"])
# async def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user = models.User(**request.dict(exclude = {"password"}))
#     new_user.password = Hash.bcrypt(request.password)
#     db.add(new_user)
#     db.commit() 
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', response_model=schemas.ShowUser, tags=["users"])
# async def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
#     return user