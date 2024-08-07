from pydantic import BaseModel, EmailStr, ValidationError, root_validator

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @root_validator
    def passwords_mathc(cls, values):
        password = values.get("password")
        password_confimation = values.get("password_confirmation")
        if password != password_confimation:
            raise ValueError("Password don't match")
        return values

# Passwords not matching
try:
    UserRegistration(
        email="jdoe@example.com", password="aa", password_confirmation="bb"
    )
except ValidationError as e:
    print(str(e))

# Valid
user_registration = UserRegistration(
    email="jdoe@example.com", password="aa", password_confirmation="aa"
)

print(user_registration)

# 1 validation error for UserRegistration
# __root__
#   Password don't match (type=value_error)
# email='jdoe@example.com' password='aa' password_confirmation='aa'
