#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import json
import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Back up file.json and start each test with empty storage."""
        if os.path.exists("file.json"):
            os.rename("file.json", "backup_test.json")
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Restore file.json and empty storage after each test."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("backup_test.json"):
            os.rename("backup_test.json", "file.json")
        FileStorage._FileStorage__objects = {}

    def test_private_attributes_exist(self):
        """Test that the private class attributes exist."""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_all_returns_dict(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(FileStorage().all(), dict)

    def test_all_starts_empty(self):
        """Test that all returns an empty dictionary with no objects."""
        self.assertEqual(FileStorage().all(), {})

    def test_new_adds_object(self):
        """Test that new stores the object under its key."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        self.assertIs(storage.all()["BaseModel." + obj.id], obj)

    def test_new_key_uses_class_name_and_id(self):
        """Test that the key is <class name>.<id>."""
        user = User()
        self.assertIn("User." + user.id, FileStorage().all())

    def test_save_creates_file(self):
        """Test that save creates the JSON file."""
        BaseModel()
        FileStorage().save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_writes_valid_json(self):
        """Test that save writes the dictionary form of each object."""
        obj = BaseModel()
        FileStorage().save()
        with open("file.json", "r") as f:
            data = json.load(f)
        self.assertEqual(data["BaseModel." + obj.id], obj.to_dict())

    def test_reload_restores_objects(self):
        """Test that reload rebuilds saved objects."""
        storage = FileStorage()
        obj = BaseModel()
        obj.name = "Test"
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        restored = storage.all()["BaseModel." + obj.id]
        self.assertEqual(restored.to_dict(), obj.to_dict())
        self.assertIsNot(restored, obj)

    def test_reload_restores_correct_class(self):
        """Test that reload rebuilds each object as its own class."""
        storage = FileStorage()
        user = User()
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertIsInstance(storage.all()["User." + user.id], User)

    def test_reload_without_file_does_nothing(self):
        """Test that reload does not fail when the file is missing."""
        storage = FileStorage()
        storage.reload()
        self.assertEqual(storage.all(), {})


if __name__ == "__main__":
    unittest.main()
