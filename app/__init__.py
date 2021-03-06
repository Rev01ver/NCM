from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.mod_ncm.models import Base
from config import *

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(sessionmaker(bind=engine))
Base.query = db_session.query_property()


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Build the database:
Base.metadata.create_all(bind=engine)

