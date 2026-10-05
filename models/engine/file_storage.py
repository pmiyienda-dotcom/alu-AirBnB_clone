#!/usr/bin/python3
"""Defines the FileStorage class that saves objects to a JSON file."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and back."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Store obj in __objects under the key <class name>.<id>."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f)

    def reload(self):
        """Deserialize the JSON file to __objects, if the file exists."""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        for key, value in data.items():
            FileStorage.__objects[key] = BaseModel(**value)
