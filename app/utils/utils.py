from app.mod_ncm.models import Host
from app.mod_ncm.models import Configuration

from app.mod_getconf import get_conf


def get_all_hosts():
    hosts = Host.query.all()
    return hosts


def get_all_configs_by_host_id(host_id):
    print(type(host_id))
    print("in get_all")
    config = Configuration
    configs = Configuration.query.filter(config.id == host_id).all()
    # print(configs + " Config")
    return configs


def get_all_configs():
    configs = Configuration.query.all()
    return configs


def get_last_rev():
    return get_conf


def get_rev_by_id():
    return None


def save_rev():
    return None

