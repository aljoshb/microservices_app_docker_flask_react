# manage.py is used to the configure Flask CLI to run
# and manage the app from the command line.
import unittest

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

# Make the `recreate_db` command accessible from the command line
@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

# Make the `test` command accessible from the command line
@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

# Make the `seed_db` command accessible from the command line
@cli.command()
def seed_db():
    """Seeds the database (i.e. adds some initial data)"""
    db.session.add(User(username='josh', email="bolualawode@gmail.com"))
    db.session.add(User(username='jondoe', email="jon@doe.com"))
    db.session.commit()

if __name__ == '__main__':
    cli()