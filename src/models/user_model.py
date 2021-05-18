from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    identification: str
    phone: str

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'identification': self.identification,
            'phone': self.phone
        }
