#!/usr/bin/env python3
# Tests for database handling
from db_handling import connect_database, load_json, create_db, DatabaseError, add_control, Status
import sqlite3
import pytest

database = 'database.db'

# Check if function return object of sqlite3
def test_connect_database():
    create_connection = connect_database()
    is_obj_instance = isinstance(create_connection, sqlite3.Connection)
    assert is_obj_instance is True

# Check if we return list of parameters from json config
def test_json_loader():
    json_base = load_json()
    is_obj_list = isinstance(json_base, list)
    assert is_obj_list is True

def test_create_database():
    create_database = create_db()
    assert create_database is None

def test_add_control_good():
    for i in range(1,5):
        control_func = add_control(0, i)
        assert control_func is None