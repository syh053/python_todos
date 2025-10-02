from db import db
from sqlalchemy import text

class Todos(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'), nullable=False)

    def __repr__(self):
        return f'<Todo: {self.name!r}>'

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }