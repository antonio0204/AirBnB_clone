#!/usr/bin/python3
"""
Create unique instance of FileStorage class.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
