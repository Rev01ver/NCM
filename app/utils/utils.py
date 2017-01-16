from app.mod_ncm.models import Host
from app.mod_ncm.models import Configuration


def get_all_hosts():
    hosts = Host.query.all()
    # output_hosts = ''
    # for host in hosts:
    #     output_hosts += '<tr><td>' + host.name + '</td>' + \
    #                     '<td>' + host.host_type + '</td>' + \
    #                     '<td>' + host.address + '</td></tr>'
    # output = '''<table>
    #         <tr>
    #             <th>Имя</th>
    #             <th>Тип</th>
    #             <th>Адресс</th>
    #         </tr>''' + output_hosts + \
    #          '</table>'
    return hosts


def get_all_configs(host_id):
    config = Configuration
    configs = Configuration.query.filter(config.id == host_id).all()
    print(configs + " Config")
    return configs


def get_last_rev():
    return None


def get_rev_by_id():
    return None


def save_rev():
    return None

