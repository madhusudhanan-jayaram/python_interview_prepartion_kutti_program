from pydantic import BaseModel, ValidationError, field_validator, model_validator


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

    @field_validator("email")
    @classmethod
    def email_must_have_at(cls, v):
        if "@" not in v:
            raise ValueError("Invalid email address")
        return v.lower()  # normalise to lowercase

    @field_validator("age")
    @classmethod
    def age_must_be_adult(cls, v):
        if v < 18:
            raise ValueError("User must be at least 18 years old")
        return v

    @model_validator(mode="after")
    def name_cannot_contain_numbers(self):
        if any(char.isdigit() for char in self.name):
            raise ValueError("name must not contain numbers")
        return self


# Valid user
user = User(id=1, name="Madhu Sudhanan", email="MADHU@Example.com", age=25)
print(user)
print()

# Invalid email
try:
    User(id=2, name="Alice", email="not-an-email", age=30)
except ValidationError as e:
    print("Email error:", e.errors()[0]["msg"])

# Under 18
try:
    User(id=3, name="Bob", email="bob@example.com", age=16)
except ValidationError as e:
    print("Age error:", e.errors()[0]["msg"])

# Name with numbers
try:
    User(id=4, name="Bob123", email="bob@example.com", age=20)
except ValidationError as e:
    print("Name error:", e.errors()[0]["msg"])
