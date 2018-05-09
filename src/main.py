#!/usr/bin/env python3
# Main module for scripts calling
from pathlib import Path
from transports import SSHtransport
from db_handling import sqlite_handle
from report import make_report
from time import gmtime, strftime
import importlib
import time

SCRIPT_DIR = 'scripts'
LOCAL_DB = sqlite_handle()


# Import all scripts from folder
def import_scripts():
    script_dir = Path('.').joinpath(SCRIPT_DIR)
    for file in script_dir.glob('**/*.py'):
        if file.name == '__init__.py':
            continue
        else:
            script_id = int(''.join(filter(str.isdigit, file.name)))
            script_name = file.name[:-3]
            status = importlib.import_module('.' + script_name, 
                                             package=SCRIPT_DIR).main()
            LOCAL_DB.add_control(script_id, script_name, status[0], status[1])


def main():
    start_time = strftime("%H:%M:%S", gmtime())
    start_time_diff = time.time()
    LOCAL_DB.create_db()
    LOCAL_DB.initial_scan()
    import_scripts()
    end_time = strftime("%H:%M:%S", gmtime())
    end_time_diff = time.time()
    duration = end_time_diff - start_time_diff
    LOCAL_DB.add_time(start_time, end_time, duration)
    make_report()

if __name__ == "__main__":
    main()
