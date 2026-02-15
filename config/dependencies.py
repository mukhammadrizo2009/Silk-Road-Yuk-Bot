from .database import LocalSession
from .models import User

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
        
        