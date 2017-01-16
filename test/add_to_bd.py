from app import db_session
from app.mod_ncm.models import User, Configuration, Host
import datetime


def add_user():
    user = User('Vasya', '12345', 1)
    db_session.add(user)
    db_session.commit()
    print('ok')


def add_host():
    host = Host('cisco01', '192.168.0.23', 'cisco', 1)
    db_session.add(host)
    db_session.commit()
    print('ok')


def add_config():
    configuration = Configuration(config_type='type', datetime=datetime.date(2007, 12, 5),
                                  data='some configs', host_id=1)
    db_session.add(configuration)
    db_session.commit()
    print('ok')


if __name__ == '__main__':
    add_user()
    add_host()
    add_config()
