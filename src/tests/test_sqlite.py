#!/usr/bin/env python3
# Tests for database handling
from db_handling import connect_database, load_json, \
DatabaseError, sqlite_handle, Status
import sqlite3
import ast
import pytest

LOCAL_DB = sqlite_handle()

# Check if function return object of sqlite3
def test_sqlite_object():
    assert isinstance(LOCAL_DB, sqlite_handle)

def test_connect_database():
    assert isinstance(connect_database(), sqlite3.Connection)

# Check if we return list of parameters from json config
def test_json_loader():
    assert isinstance(load_json(), list)

def test_create_database():
    create_database = LOCAL_DB.create_db()
    connection = connect_database()
    with connection:
        assert isinstance(connection.execute(
            'SELECT * from control').fetchall(), list)
        assert isinstance(connection.execute(
            'SELECT * from control').fetchall(), list)
    connection.close()

def test_add_control_good():
    connection = connect_database()
    with connection:
        control_func = LOCAL_DB.add_control(0, 'name', 'transport', 5)
        LOCAL_DB.add_scan_info(1337)
        value_from_db = ast.literal_eval(
            connection.execute("SELECT * FROM scandata \
            WHERE id = (SELECT MAX(ID) FROM scandata)").fetchone()[1])[0][3]
        value_from_enum = Status(5).name
        assert (value_from_db == value_from_enum)
    connection.close()