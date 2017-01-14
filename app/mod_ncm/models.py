from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey

# вавав
Base = declarative_base()

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    address = Column(String(50))
    host_type = Column(String(50))
    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, name, address=None, host_type=None, user_id=None):
        self.name = name
        self.address = address
        self.host_type = host_type
        self.user_id = user_id

    def __repr__(self):
        return '<Host {} {} {}>'.format(self.name, self.address, self.host_type)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))  # TODO: How to keep passwords?
    host_id = Column(Integer, ForeignKey('host.id'))

    def __init__(self, username=None, password=None, host_id=None):
        self.username = username
        self.password = password
        self.host_id = host_id

    def __repr__(self):
        return '<User {}'.format(self.username)


class Configuration(Base):
    __tablename__ = 'configuration'
    id = Column(Integer, primary_key=True)
    config_type = Column(String(50))
    datetime = Column(String(50))
    data = Column(String(50))
    host_id = Column(Integer, ForeignKey('host.id'))

    def __init__(self, config_type=None, datetime=None, data=None, host_id=None):
        self.config_type = config_type
        self.datetime = datetime
        self.data = data
        self.host_id = host_id

    def __repr__(self):
        return '<Configuration {} {}'.format(self.config_type, self.datetime)




# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)





