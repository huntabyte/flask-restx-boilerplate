# Model schemas
from app import ma

from .user import User


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("email", "name", "username", "joined_date")
