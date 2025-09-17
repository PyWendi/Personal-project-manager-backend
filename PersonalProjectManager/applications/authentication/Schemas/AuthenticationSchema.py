from ninja import Schema, ModelSchema
from typing import Optional, Dict, Any
from django.contrib.auth import get_user_model

class UserSchemaModel(ModelSchema):
    class Meta:
        model = get_user_model()
        exclude = [
            "date_joined",
            "is_staff",
            "is_superuser",
            "is_active",
            "groups",
            "user_permissions"
        ]

class UserSchema(Schema):
    user: UserSchemaModel

class ResponseSchema(Schema):
    result: bool
    message: str
    data: Optional[Dict[str, Any]]  # data peut contenir n'importe quel dict

class  CodeSchema(Schema):
    code: str
    email: str

class ResetPasswordSchema(Schema):
    password: str
    email: str