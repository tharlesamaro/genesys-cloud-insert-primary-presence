from sqlalchemy import Column, DateTime, Integer, String

from app.db import Base


class PrimaryPresence(Base):
    __tablename__ = "primary_presence"

    primary_presence_id = Column(
        String, nullable=False, primary_key=True, index=True, autoincrement=False
    )
    user_id = Column(String, index=True)
    start_time = Column(String, nullable=True)
    end_time = Column(String, nullable=True)
    system_presence = Column(String, nullable=True)
    organization_presence_id = Column(String, nullable=True)
