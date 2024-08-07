from pydantic import BaseModel, Field, ValidationError

class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: int | None = Field(None, ge=0, le=120)


# Invalid first name
try:
    Person(first_name="J", last_name="Doe", age=30)
except ValidationError as e:
    print(str(e))


# Invalid age
try:
    Person(first_name="John", last_name="Doe", age=2000)
except ValidationError as e:
    print(str(e))

# Valid
person = Person(first_name="John", last_name="Doe", age=30)
print(person)

# 1 validation error for Person
# first_name
#   ensure this value has at least 3 characters (type=value_error.any_str.min_length; limit_value=3)
# 1 validation error for Person
# age
#   ensure this value is less than or equal to 120 (type=value_error.number.not_le; limit_value=120)
# first_name='John' last_name='Doe' age=30
