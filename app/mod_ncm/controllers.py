from flask import Blueprint
from flask import Flask, render_template

from app.utils.utils import *
from app.mod_ncm.models import Host

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_ncm = Blueprint('ncm', __name__, url_prefix='/')
mod_test = Blueprint('test', __name__, url_prefix='/test')


# Set the route and accepted methods
@mod_ncm.route('/', methods=['GET', 'POST'])
def index():
    print("im in index")
    context = {
        "hosts": get_all_hosts()
    }
    return render_template('index.html', **context)


@mod_ncm.route('/hostconfigs')
def show_configurations():
    print("im in configs")
    # context = {
    #     "configs": get_all_configs(host_id)
    # }
    # return render_template("hostconfigs.html", **context)
    return render_template('hotsconfigs.html')


@mod_test.route('/test', methods=['GET', 'POST'])
def test():
    print("im in test")
    # context = {
    #     "configs": get_all_configs(host_id)
    # }
    # return render_template("hostconfigs.html", **context)
    return '<p>test</p>'
