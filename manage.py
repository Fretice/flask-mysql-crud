import os
from app import create_app
from flask.ext.script import Manager


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


if __name__ == '__main__':
    manager.run()
