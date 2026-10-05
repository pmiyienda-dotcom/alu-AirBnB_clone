#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city, linked to a State by state_id."""

    state_id = ""
    name = ""
