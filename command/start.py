from DNS import dnspod
import config_func
from time import sleep
from command import ipv6

def start(subdomain, time):
    config = config_func.read_config('conf/ddns.conf')
    value = ipv6.get_global_ipv6()
    recordid = 0
    if config['dns'] == 'dnspod':
        dnspod.dnspod_add_record(config['domain'], config['secretid'], config['secretkey'], value, subdomain)
        for record in dnspod.dnspod_get_record_list_noprint(config['domain'], config['secretid'], config['secretkey']).RecordList:
            if record.Name == subdomain and record.Type == 'AAAA':
                recordid = record.RecordId
                dnspod.dnspod_change_record(config['domain'], config['secretid'], config['secretkey'], recordid, value, subdomain)
    while 1:
        value_tmp = ipv6.get_global_ipv6()
        if value != value_tmp:
            value = value_tmp
            if config['dns'] == 'dnspod':
                dnspod.dnspod_change_record(config['domain'], config['secretid'], config['secretkey'], recordid, value, subdomain)
        else:
            print("未改变")
        sleep(int(time))
