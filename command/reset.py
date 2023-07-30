# -*- coding: utf-8 -*-
from config_func import modify_config
import os

def reset():
    config = ['dns', 'domain', 'secretid', 'secretkey', 'api_token_dynv6']
    try:
        file = open('conf/ddns.conf', 'r')
        file.close()
    except FileNotFoundError:
        os.mkdir('conf')
        os.system('touch ddns.conf')

    for option in config:
        modify_config('conf/ddns.conf', option, '')