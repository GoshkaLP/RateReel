from enum import Enum


class Role(str, Enum):
    user = "User"
    admin = "Admin"
