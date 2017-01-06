from app import db, Base


class Host(Base):
    __tablename__ = 'host'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    host_type = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name=None, address=None, host_type=None, user_id=None):
        self.name = name
        self.address = address
        self.host_type = host_type
        self.user_id = user_id

    def __repr__(self):
        return '<Cisco {} {} {}>'.format(self.name, self.address, self.host_type)


class Users(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))  # TODO: How to keep passwords?
    host_id = db.Column(db.Integer, db.ForeignKey('host.id'))

    def __init__(self, username=None, password=None, host_id=None):
        self.username = username
        self.password = password
        self.host_id =host_id

    def __repr__(self):
        return '<User {}'.format(self.username)


class Config(Base):
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True)
    config_type = db.Column(db.String(50))
    datetime = db.Column(db.DateTime)
    data = db.Column(db.Text)
    host_id = db.Column(db.Integer, db.ForeignKey('host.id'))

    def __init__(self, config_type=None,  datetime=None, data=None, host_id=None):
        self.config_type = config_type
        self.datetime = datetime
        self.data = data
        self.host_id = host_id

    def __repr__(self):
        return '<Config {} {}'.format(self.config_type, self.datetime)


# if __name__ == "__main__":
#     Base.metadata.create_all(bind=engine)





