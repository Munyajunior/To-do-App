from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from model.sql_model import BASE

load_dotenv()

db_user: str = os.getenv("USER")
db_port: int = os.getenv("PORT")
db_host: str = os.getenv("HOST")
db_password: str = os.getenv("PASS")
db_domain: str = os.getenv("DOMAIN")
db_name: str = os.getenv("DB_NAME")

uri: str = f'{db_domain}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(uri)

BASE.metadata.create_all(bind=engine)


# session
session = sessionmaker(
    bind=engine,
    autoflush=True
)
db_session = session()

try:
    connection = engine.connect()
    connection.close()
    print('Ping Connection')
except Exception as e:
    print(f'Error: {str(e)}')