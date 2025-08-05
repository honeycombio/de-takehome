#!/usr/bin/env python3
"""
Entry point for the compiled Flask application.
This script imports and runs the compiled app from the compiled bytecode.
Cross-platform compatible version.
"""

import sys
import os
import shutil
import glob

def find_compiled_app():
    """Find the compiled app file regardless of Python version."""
    pycache_dir = '__pycache__'
    if not os.path.exists(pycache_dir):
        raise FileNotFoundError(f"Directory {pycache_dir} not found")
    
    # Look for any compiled app file (handles different Python versions)
    pattern = os.path.join(pycache_dir, 'app.cpython-*.pyc')
    compiled_files = glob.glob(pattern)
    
    if not compiled_files:
        raise FileNotFoundError(f"No compiled app files found in {pycache_dir}")
    
    # Use the first (and should be only) compiled file
    return compiled_files[0]

def main():
    try:
        # Find and copy the compiled app
        compiled_file = find_compiled_app()
        target_file = 'app.pyc'
        
        print(f"Found compiled app: {compiled_file}")
        shutil.copy(compiled_file, target_file)
        print(f"Copied to: {target_file}")
        
        # Import the compiled app module
        import app
        print("Successfully imported compiled app")
        
        # Run the Flask application
        print("Starting Flask application...")
        app.app.run(host='0.0.0.0', port=5000, debug=False)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 