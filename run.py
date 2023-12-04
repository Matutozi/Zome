#!/usr/bin/env python3
"""module that runs the other script"""
from zome import app, db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
