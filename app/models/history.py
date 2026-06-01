from sqlalchemy import Column, String , DateTime
from datetime import datetime, timezone
from app.db.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class History(Base):
    __tablename__ = "history"

    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)

    mood = Column(String)
    language = Column(String)

    song_id = Column(String)
    title = Column(String)
    artist = Column(String)

    created_at = Column(DateTime(timezone=True), default= lambda: datetime.now(timezone.utc))