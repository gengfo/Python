# encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlktqa import app
from exts import db
from models import User
import MySQLdb

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

db.init_app(app)


if __name__ == "__main__":
    manager.run()
