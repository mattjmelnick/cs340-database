# cs340-database

The Jinja syntax in the template files is based on the syntax used in the CS 340 Flask Starter App located at https://github.com/osu-cs340-ecampus/flask-starter-app/tree/master/bsg_people_app/templates.

The JavaScript functions that take in the database values as parameters are original implementations to keep the edit and delete forms on the same page.

The db_connector file is taken from the CS 340 Flask Starter App located at https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/database/db_connector.py. The code has been slightly modified to remove the "if __name__ == '__main__':" code block.

Blueprints have been added to introduce modularization and reduce the size of the app.py file. Each blueprint is based on the starter app.py file located at https://github.com/osu-cs340-ecampus/flask-starter-app/blob/master/bsg_people_app/app.py, and an additional resource located at https://realpython.com/flask-blueprint/