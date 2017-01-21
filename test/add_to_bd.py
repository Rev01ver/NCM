from app import db_session
from app.mod_ncm.models import User, Configuration, Host
import datetime


def add_user():
    user = User('serg', '', 1)
    db_session.add(user)
    db_session.commit()
    print('add user ok')


def add_host():
    host = Host('cisco01', '87.228.74.62', 'cisco', 1)
    db_session.add(host)
    db_session.commit()
    print('add host ok')


def add_config():
    configuration = Configuration(config_type='type', datetime=datetime.date(2007, 12, 5),
                                  data='some configs', host_id=1)
    db_session.add(configuration)
    db_session.commit()
    print('add conf ok')


if __name__ == '__main__':
    add_user()
    add_host()
    # add_config()
