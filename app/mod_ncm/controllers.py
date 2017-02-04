from flask import render_template
from app.utils.bd_utils import *
from app.utils.cisco_utils import *
from app import app
from app.mod_ncm.models import User, Configuration
from app import db_session

from flask_wtf import FlaskForm
from wtforms import StringField


class MyForm(FlaskForm):
    name = StringField('name')
    host = StringField('host')
    address = StringField('address')


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
    context = {
        'configs': get_all_configs_by_host_id(host_id)
    }
    return render_template('hostconfigs.html', **context)


@app.route('/showconf/<int:host_id>')
def show_conf(host_id):
    host = get_host_by_id(host_id)
    user = get_user_by_id(host.user_id)
    conf = {
        'config': get_cisco_run_conf(host.address, host_id, user.username, user.password),
        'host': host_id
    }
    return render_template('showconf.html', **conf)


@app.route('/showconf/save/<int:host_id>/')
def save_conf(host_id):
    host = get_host_by_id(host_id)
    print(host)
    user = get_user_by_id(host.user_id)
    print(user)
    conf = get_cisco_run_conf(host.address, host_id, user.username, user.password)
    print(conf)
    db_session.add(conf)
    db_session.commit()
    host = {
        'host_id': host_id
    }
    return render_template('save.html', **host)


@app.route("/compareconf/<int:host_id>/")
def compare_conf(host_id):
    if do_wr('87.228.74.62', 'serg', 'pyTh0n22'):
        print('running config has changed')
        host = get_host_by_id(host_id)
        user = get_user_by_id(host.user_id)
        run_conf = get_cisco_run_conf(host.address, user.username, user.password)
        db_session.add(run_conf)
        db_session.commit()
        return '<p>running conf has changed and saved to db</p>'
    else:
        print('running config the same')
        return '<p>running config the same</p>'


@app.route('/addhost/') #wtforms
def add_host():
    form = MyForm()
    return render_template("addhost.html", form=form)
    # host = Host()


@app.route('/ajax/<int:host_id>/<int:config1_id>/<int:config2_id>/')
def ajax(host_id):
    host = get_host_by_id(host_id)
    config1 = get_cisco_run_conf()





