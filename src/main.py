#!/usr/bin/env python3
# Main module for scripts calling
from pathlib import Path
from transports import SSHtransport
from db_handling import add_control, create_db
from report import scan_info, make_report
import importlib
import time
import os

_scriptdir = 'scripts'

# Import all scripts from folder
def import_scripts():
    script_dir = Path('./' + _scriptdir)
    for file in script_dir.glob('**/*.py'):
        if file.name != '__init__.py':
            status = importlib.import_module('.' + file.name[:-3], package = _scriptdir).main()
            script_id = int(file.name[0:3])
            add_control(script_id, status)

def main():
    start_time = time.time()
    create_db()
    import_scripts()
    end_time = time.time() - start_time
    scan_info(end_time)
    make_report()

if __name__ == "__main__":
    main()