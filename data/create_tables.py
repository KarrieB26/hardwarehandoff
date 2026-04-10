import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.models import Base
from app.database import engine

Base.metadata.create_all(bind=engine)
print("Tables created!")