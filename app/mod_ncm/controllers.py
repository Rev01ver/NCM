from flask import render_template
from app.utils.utils import *
from app import app
from app.mod_ncm.models import User

print(111)
# Set the route and accepted methods
@app.route('/')
def index():
    print("im in index")
    context = {
        "hosts": get_all_hosts()
    }
    return render_template('index.html', **context)


@app.route('/hostconfigs/<int:host_id>')
def hostconfigs(host_id):
    print(host_id)
    context = {
        'configs': get_all_configs_by_host_id(host_id)
    }
    return render_template('hostconfigs.html', **context)


@app.route('/showconf/<int:host_id>')
def show_conf(host_id):
    host = get_host_by_id(host_id)
    user = get_user_by_id(host.user_id)
    print(host.address, user.username, user.password)
    conf = get_cisco_run_conf(host.address, user.username, user.password)
    return '<p>'+''.join(conf)+'</p>'

