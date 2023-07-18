from config_func import modify_config

def reset():
    config = ['dns', 'domain', 'secretid', 'secretkey']
    for option in config:
        modify_config('conf/ddns.conf', option, '')
