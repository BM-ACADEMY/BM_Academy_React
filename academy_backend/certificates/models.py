# certificates/models.py
from mongoengine import Document, StringField, DateTimeField
import datetime

class Certificate(Document):
    user_id = StringField(required=True)  # MongoDB ObjectId as string
    course_id = StringField(required=True)  # MongoDB ObjectId as string
    certificate_id = StringField(required=True, unique=True)
    issue_date = DateTimeField(default=datetime.datetime.utcnow)
    file_url = StringField()

    # Optional fields (your MongoDB documents contain these)
    manual_name = StringField()
    manual_course = StringField()
    certificate_type = StringField()

    meta = {
        "collection": "certificates",
        "strict": False   # <-- IMPORTANT: Allow unknown fields
    }
