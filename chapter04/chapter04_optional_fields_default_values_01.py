from pydantic import BaseModel

class UserProfile(BaseModel):
    nickname: str
    location: str | None = None
    subscribed_newsletters: bool = True


user = UserProfile(nickname="jode")
print(user)

# python chapter04_optional_fields_default_values_01.py
# nickname='jode' location=None subscribed_newsletters=True
