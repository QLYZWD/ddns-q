# -*- coding: utf-8 -*-
from DNS import dnspod, dynv6
import config_func
from time import sleep
from command import ipv6, reset
import os


def start(subdomain, time):
    try:
        file = open('conf/ddns.conf', 'r')
        file.close()
    except FileNotFoundError:
        try:
            os.mkdir('conf')
        except FileExistsError:
            pass
        finally:
            os.system('echo # ddns-conf>conf/ddns.conf')
            reset.reset()

    config = config_func.read_config('conf/ddns.conf')
    for key, value in config.items():
        if value == '':
            print("请完成配置 "+key)
            return 0

    value = ipv6.get_global_ipv6()
    recordid = 0
    if config['dns'] == 'dnspod':
        for record in dnspod.dnspod_get_record_list_noprint(config['domain'], config['secretid'], config['secretkey']).RecordList:
            if record.Name == subdomain and record.Type == 'AAAA':
                print('已存在该记录')
                recordid = record.RecordId
                dnspod.dnspod_change_record(config['domain'], config['secretid'], config['secretkey'], recordid, value, subdomain)
                break
            else:
                continue
        if recordid == 0:
            print('不存在该记录，创建新记录')
            recordid = dnspod.dnspod_add_record(config['domain'], config['secretid'], config['secretkey'], value, subdomain).RecordId
    elif config['dns'] == 'dynv6':
        dynv6.add_record(subdomain, config['api_token_dynv6'], config['domain'], value)


    while 1:
        value_tmp = ipv6.get_global_ipv6()
        if value != value_tmp:
            print('IPV6已改变')
            value = value_tmp
            if config['dns'] == 'dnspod':
                dnspod.dnspod_change_record(config['domain'], config['secretid'], config['secretkey'], recordid, value, subdomain)
            elif config['dns'] == 'dynv6':
                dynv6.add_record(subdomain, config['api_token_dynv6'], config['domain'], value)
        else:
            print("未改变")
        sleep(int(time))
