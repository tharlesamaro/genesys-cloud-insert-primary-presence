from sqlalchemy import Column, DateTime, Integer, String

from app.db import Base


class PrimaryPresence(Base):
    __tablename__ = "primary_presence"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    primary_presence_id = Column(String, nullable=True)
    user_id = Column(String, index=True)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    system_presence = Column(String, nullable=True)
    organization_presence_id = Column(String, nullable=True)
