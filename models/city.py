#!/usr/bin/python3
""" contains a class City which inherits from BaseModel"""


from models.base_model import BaseModel


class City(BaseModel):
    """inherits from Bsemodel"""

    state_id = ""
    name = ""
