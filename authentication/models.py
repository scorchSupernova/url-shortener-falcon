from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model_config.model_con import Base
from user_info.models import User
from datetime import datetime

class Authentication(Base):
    __tablename__ = "authentications"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), default=None)
    token = Column(String, default=None)
    created_at = Column(DateTime, default=datetime.now().utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now().utcnow(), nullable=False)

    user = relationship("User", backref="authentications")