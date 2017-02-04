from app.mod_ncm.models import Host, Configuration, User


def get_all_hosts():
    hosts = Host.query.all()
    return hosts


def get_host_by_id(host_id):
    return Host.query.filter(Host.id == host_id).first()


def get_user_by_id(user_id):
    return User.query.filter(User.id == user_id).first()


def get_all_configs_by_host_id(host_id):
    return Configuration.query.filter(Configuration.host_id == host_id).all()


def get_all_configs():
    configs = Configuration.query.all()
    return configs


def get_config_by_id(config_id):
    return Configuration.query.filter(Configuration.id == config_id).first()

