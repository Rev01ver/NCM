from app import db_session
from app.mod_ncm.models import User, Configuration, Host


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
    configuration = Configuration('type', '12.12.2016', 'some configs', 1)
    db_session.add(configuration)
    db_session.commit()
    print('ok')


if __name__ == '__main__':
    add_user()
    add_host()
    add_config()
