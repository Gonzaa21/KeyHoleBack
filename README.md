# KeyHole Backend
The principal idea for the backend was that this must be connected to MySQL database and in that way the data can be saved locally. Due to various circumstances, this idea can't be possible.

# Content
* app/__init__.py: start Flask.
* app/routes.py: Determine routes (endpoints).
* app/models.py: Determine classes and logic of database.
* app/db.py: Configure connection to MySQL.
* app/config.py: Contain configurations of Flask.
* run.py: Entry point for run server.
* .env: Environment Variables (Credentials, configurations).