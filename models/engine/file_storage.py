#!/usr/bin/python3
"""Defines the FileStorage class that saves objects to a JSON file."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        classes = {
            "BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review}
        for key, value in data.items():
            cls = classes[value["__class__"]]
            FileStorage.__objects[key] = cls(**value)
