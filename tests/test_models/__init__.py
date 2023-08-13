#!/usr/bin/python3
"""Initialize a unique instance of FileStorage for your application."""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage
file_storage_instance = FileStorage()

# Reload data into the storage instance
file_storage_instance.reload()

