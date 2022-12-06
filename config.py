
from dotenv import load_dotenv
import os


load_dotenv()
SQLALCHEMY_DATABASE = os.getenv('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.getenv('SECRET_KEY')
UPLOADED_PHOTOS_DEST = os.getenv('UPLOADED_PHOTOS_DEST')