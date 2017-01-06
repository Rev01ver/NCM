from flask import Blueprint

from app.mod_ncm.models import Host
from app.mod_ncm.models import Config
from app.mod_ncm.models import Users

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_ncm = Blueprint('ncm', __name__, url_prefix='/index')


# Set the route and accepted methods
@mod_ncm.route('/index/', methods=['GET', 'POST'])
def index():
    pass
