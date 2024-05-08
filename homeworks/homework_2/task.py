from pydantic import BaseModel, field_validator, Field, EmailStr, model_validator


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)


class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator("name")
    def check_name(cls, value: str):
        if not value.isalpha():
            raise ValueError("Name should contains only chars")

        return value

    @model_validator(mode="after")
    def check_age_employed_relation(self):
        if self.age < 18 and self.is_employed is True:
            raise ValueError("User with age less than 18 cannot be employed")
        return self


def create_user(user_data: str):
    try:
        user = User.parse_raw(user_data)
        return user.json()
    except ValueError as err:
        print(err)


valid_user_data = """
{
    "name": "Alex",
    "age": 18,
    "email": "test.alex@gmail.com",
    "is_employed": true,
    "address": {
        "city": "London",
        "street": "Cambridge Str.",
        "house_number": 26
    }
}
"""
print(create_user(valid_user_data))


# ======================================================================================================================
# invalid_name_data_1 = """
# {
#     "name": "A",
#     "age": 31,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_name_data_1))


# ======================================================================================================================
# invalid_name_data_2 = """
# {
#     "name": "Alex123",
#     "age": 31,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_name_data_2))


# ======================================================================================================================
# invalid_age_data_1 = """
# {
#     "name": "Alex",
#     "age": 0,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_age_data_1))


# ======================================================================================================================
# invalid_age_data_2 = """
# {
#     "name": "Alex",
#     "age": 120,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_age_data_2))


# ======================================================================================================================
# invalid_age_data_3 = """
# {
#     "name": "Alex",
#     "age": "test",
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_age_data_3))


# ======================================================================================================================
# invalid_email_data = """
# {
#     "name": "Alex",
#     "age": 12,
#     "email": "test.alex.gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_email_data))


# ======================================================================================================================
# invalid_age_employed_data = """
# {
#     "name": "Alex",
#     "age": 12,
#     "email": "test.alex@gmail.com",
#     "is_employed": true,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_age_employed_data))


# ======================================================================================================================
# invalid_employed_data = """
# {
#     "name": "Alex",
#     "age": 18,
#     "email": "test.alex@gmail.com",
#     "is_employed": 12,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_employed_data))


# ======================================================================================================================
# invalid_city_data_1 = """
# {
#     "name": "Alex",
#     "age": 18,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "L",
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_city_data_1))


# ======================================================================================================================
# invalid_city_data_2 = """
# {
#     "name": "Alex",
#     "age": 18,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": 2234,
#         "street": "Cambridge Str.",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_city_data_2))


# ======================================================================================================================
# invalid_street_data_1 = """
# {
#     "name": "Alex",
#     "age": 18,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Ca",
#         "house_number": 26
#     }
# }
# """
# print(create_user(invalid_street_data_1))


# ======================================================================================================================
# invalid_house_number_data_1 = """
# {
#     "name": "Alex",
#     "age": 18,
#     "email": "test.alex@gmail.com",
#     "is_employed": false,
#     "address": {
#         "city": "London",
#         "street": "Cambridge Str.",
#         "house_number": 0
#     }
# }
# """
# print(create_user(invalid_house_number_data_1))
