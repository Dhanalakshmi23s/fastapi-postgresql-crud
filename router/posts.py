from typing import List
from fastapi import HTTPException,Depends
from sqlalchemy.orm import Session
from starlette import status
import post
import schema
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)

@router.get('/', response_model=List[schema.CreatePost]) #read all the data from the DB
def test_posts(db: Session =  Depends(get_db)):
    
    post1 = db.query(post.Post).all()
    print("post",post1)

    return post1

@router.post('/',status_code=status.HTTP_201_CREATED,response_model=List[schema.CreatePost])#create
def test_posts_sent(post_post:schema.CreatePost, db:Session = Depends(get_db)):
 
    new_post = post.Post(**post_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return [new_post]


@router.get('/{id}', response_model=schema.CreatePost, status_code=status.HTTP_200_OK)#read
def get_test_one_post(id:int ,db:Session = Depends(get_db)):

    idv_post = db.query(post.Post).filter(post.Post.id == id).first()

    if idv_post is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"The id: {id} you requested for does not exist")
    return idv_post

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)#delete
def delete_test_post(id:int, db:Session = Depends(get_db)):

    deleted_post = db.query(post.Post).filter(post.Post.id == id)


    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {id} you requested for does not exist")
    deleted_post.delete(synchronize_session=False)
    db.commit()



@router.put('/posts/{id}', response_model=schema.CreatePost)#update 
def update_test_post(update_post:schema.PostBase, id:int, db:Session = Depends(get_db)):

    updated_post =  db.query(post.Post).filter(post.Post.id == id)

    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{id} does not exist")
    updated_post.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return  updated_post.first()