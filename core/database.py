from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine(settings.DATABASE_URL,echo=True)


session = sessionmaker(bind=engine,autoflush=False)


def get_db():
    db = session()
    
    try:
        yield db
    finally:
        db.close()
    
    
    

