import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    second_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: list[str]
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str
