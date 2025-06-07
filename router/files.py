from fastapi import APIRouter
from minio import Minio
from dotenv import load_dotenv
from starlette import status
import os

load_dotenv()

ACCESS_KEY=os.environ.get('ACCESS_KEY')
SECRET_KEY=os.environ.get('SECRET_KEY')

MINIO_CLIENT = Minio(
    "localhost:9000",
    access_key='minioadmin',
    secret_key='minioadmin',
    secure=False
    )

bucket_name='fastapi'

router=APIRouter(
    prefix='/files',
    tags=['Files']
)

@router.post('/upload_file',status_code=status.HTTP_200_OK)
def upload_file():
    file_path='/home/ai/Documents/img.png'
    MINIO_CLIENT.fput_object(bucket_name,'img3.png',file_path)
 

