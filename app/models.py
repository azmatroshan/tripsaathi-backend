from odmantic import Model


class User(Model):
    name: str
    email: str
    password_hash: str