from config_func import modify_config


def set(key, value):
    modify_config('conf/ddns.conf', key, value)
