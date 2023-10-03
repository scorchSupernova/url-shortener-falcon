from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from model_config.model_con import Base
from datetime import datetime
from db_config.db_con import get_session

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, default=None)
    email = Column(String, default=None)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now().utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now().utcnow(), nullable=False)


    def get_user_id(self, username:str, email:str):
        return get_session().query(User).filter_by(username=username, email=email).first()

