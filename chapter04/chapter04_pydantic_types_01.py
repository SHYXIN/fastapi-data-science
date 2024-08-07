from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError

class User(BaseModel):
    email: EmailStr
    website: HttpUrl


# Invalid email
try:
    User(email="jdoe", website="http://www.example.com")
except ValidationError as e:
    print(str(e))

# Invalid URL
try:
    User(email="jdoe@example.com", website="jdoe")
except ValidationError as e:
    print(str(e))

# Valid
user= User(email="jdoe@example.com", website="https://www.example.com")
print(user) # email='jdoe@example.com' website=HttpUrl('https://www.example.com', )
