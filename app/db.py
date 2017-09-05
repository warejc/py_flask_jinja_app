from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import INTERVAL, TIMESTAMP, TSTZRANGE, UUID

db = SQLAlchemy()

db.INTERVAL = INTERVAL()
db.TIMESTAMP = TIMESTAMP()
db.TSTZRANGE = TSTZRANGE()
db.UUID = UUID()


class Profile(db.Model):
    __tablename__ = 'profile'
    __table_args__ = {'schema': 'account'}

    id = db.Column(UUID(as_uuid=False), primary_key=True)
    user_name = db.Column(db.Text)
    employee_id = db.Column(UUID())
