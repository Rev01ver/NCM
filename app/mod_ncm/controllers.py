from flask import Blueprint

from app.mod_ncm.models import Host
from app.mod_ncm.models import Configuration
from app.mod_ncm.models import User

from app import db_session

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_ncm = Blueprint('ncm', __name__, url_prefix='/')


# Set the route and accepted methods
@mod_ncm.route('/', methods=['GET', 'POST'])
def index():
    hosts = Host.query.all()
    output_hosts = ''
    for host in hosts:
        output_hosts += '<tr><td>' + host.name + '</td>' + \
                        '<td>' + host.host_type + '</td>' + \
                        '<td>' + host.address + '</td></tr>'
    output = '''<table>
        <tr>
            <th>Имя</th>
            <th>Тип</th>
            <th>Адресс</th>
        </tr>''' + output_hosts + \
             '</table>'
    return output
