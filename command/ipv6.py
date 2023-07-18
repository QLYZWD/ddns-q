import ipaddress
import socket

import netifaces
import requests


def get_ipv6_addresses():
    ipv6_addresses = []

    # 获取本机所有网络接口信息
    interfaces = netifaces.interfaces()

    # 遍历网络接口，查找IPv6地址
    for interface in interfaces:
        if_addresses = netifaces.ifaddresses(interface).get(socket.AF_INET6)
        if if_addresses:
            for if_address in if_addresses:
                ipv6_address = if_address['addr']
                if '%' in ipv6_address:
                    # 去除接口标识符
                    ipv6_address = ipv6_address.split('%')[0]
                ipv6_addresses.append(ipv6_address)

    return ipv6_addresses


# 检测是否为公网ipv6
def is_global_ipv6(ipv6_address):
    ipv6 = ipaddress.ip_address(ipv6_address)
    return ipv6.is_global


def global_ipv6_api(ipv6_address):
    return requests.get("https://v6.ident.me").text


def get_global_ipv6():
    # 列出本机ipv6
    ipv6_addresses = get_ipv6_addresses()
    if ipv6_addresses:
        print("检测本机IPv6地址:", end='')
    else:
        print("未找到IPV6地址")

    # 筛选公网ip
    for address in ipv6_addresses:
        if is_global_ipv6(address) and global_ipv6_api(address) == address:
            print(address + "为公网IP")
            return address
