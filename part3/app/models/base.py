from app import db
import uuid
from datetime import datetime, timezone
from abc import abstractmethod


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def save(self, commit: bool = True):
        self.updated_at = datetime.now(timezone.utc)
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def update(self, data: dict, commit: bool = True):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self.save(commit=commit)

    def delete(self, commit: bool = True):
        db.session.delete(self)
        if commit:
            db.session.commit()

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    def __repr__(self):
        return "<{} id={}>".format(self.__class__.__name__, self.id)
