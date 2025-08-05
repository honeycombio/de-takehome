#!/usr/bin/env python3
"""
Entry point for the compiled Flask application.
This script imports and runs the compiled app from the compiled bytecode.
"""

import sys
import os
import shutil

# Copy the compiled app to the main directory for import
compiled_file = os.path.join('__pycache__', 'app.cpython-310.pyc')
if os.path.exists(compiled_file):
    shutil.copy(compiled_file, 'app.pyc')

# Import the compiled app module
import app

if __name__ == '__main__':
    # Run the Flask application
    app.app.run(host='0.0.0.0', port=5000, debug=False) 