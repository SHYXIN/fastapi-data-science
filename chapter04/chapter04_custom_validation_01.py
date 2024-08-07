from datetime import date

from pydantic import BaseModel, ValidationError, validator

class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @validator("birthdate")
    def valid_birthdate(cls, v: date):
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValueError("You seem a bit too old!")
        return v


# Invalid birthdate
try:
    Person(first_name="John", last_name="Doe", birthdate="1800-01-01")
except ValidationError as e:
    print(str(e))

# Valid
person = Person(first_name="John", last_name="Doe", birthdate="1991-01-01")
print(person)

# 1 validation error for Person
# birthdate
#   You seem a bit too old! (type=value_error)
# first_name='John' last_name='Doe' birthdate=datetime.date(1991, 1, 1)
