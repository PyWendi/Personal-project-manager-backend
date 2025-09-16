from ninja import NinjaAPI, Router
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.core.cache import cache
from ..Middleware.AuthenticationClass import JWTAuth
from ..Schemas.AuthenticationSchema import (
    UserSchema,
    ResponseSchema,
    CodeSchema
)
from ...utils.email_utils import send_verification_email

router = Router()

@router.get("forgot_password/{email}/", response={
    200: ResponseSchema,
    404: ResponseSchema,
    500: ResponseSchema
})
def forgot_password(request: HttpRequest, email: str):
    user_model = get_user_model()
    user_exists = user_model.objects.filter(email=email).exists()
    if not user_exists:
        return 404, {
            "result": False,
            "message": "This email does not exist in our database, please verify the email.",
            "data": None
        }
    # Send the email
    status_code, response = send_verification_email(email)
    if status_code == 200:
        return 200, {
            "result": True,
            "message": "Verification code sent successfully.",
            "data": {"code": response}
        }
    else:
        return 500, {
            "result": False,
            "message": response, # ici response contient l'erreur
            "data": None
        }


@router.post("verify_code/", response={200: ResponseSchema, 400: ResponseSchema})
def verify_code(request:HttpRequest, data:CodeSchema):
    code = data.code
    email = data.email

    cached_code = cache.get(f"verify_{email}")
    if not cached_code:
        return 400, {"result": False, "message": "Code expired or not found", "data": None}

    if cached_code != code:
        return 400, {"result": False, "message": "Invalid code", "data": None}

    return 200, {"result": True, "message": "Code verified successfully", "data": None}


@router.get("authtest/", auth=JWTAuth(), response={200: UserSchema})
def authTest(request: HttpRequest):
    user = request.auth
    return {"user": user}