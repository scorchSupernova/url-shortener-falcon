from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from model_config.model_con import Base

class UrlShortener(Base):
    __tablename__ = "url_histories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, unique=True)
    actual_url = Column(String(255), nullable=False, unique=True)
    short_url = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now().utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now().utcnow(), nullable=False)

