#!/usr/bin/python3
"""Defines the BaseModel class, the parent of all other model classes."""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the base class for all AirBnB clone objects."""

    def __init__(self, *args, **kwargs):
    """Initialize a BaseModel, from kwargs if given or as a new instance."""
    if kwargs:
        for key, value in kwargs.items():
            if key == "__class__":
                ___
            elif key in ("created_at", "updated_at"):
                value = datetime.___(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            else:
                setattr(self, key, ___)
    else:
        self.id = ___
        self.created_at = ___
        self.updated_at = ___
