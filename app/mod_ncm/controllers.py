from flask import render_template
from app.utils.utils import *
from app import app

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
