import socket
import netifaces
import ipaddress
import requests
import json
import flask
# 调用腾讯云API Explorer
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models


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
        print("检测本机IPv6地址:")
        for address in ipv6_addresses:
            print(address)
    else:
        print("No IPv6 addresses found.")

    # 筛选公网ip
    for address in ipv6_addresses:
        if is_global_ipv6(address) and global_ipv6_api(address) == address:
            print("\n" + address + "为公网IP\n")
            return address


# 请求记录列表
def get_record_list(domain, secretId, secretKey):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密 代码泄露可能会导致 SecretId 和 SecretKey
        # 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(secretId, secretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = dnspod_client.DnspodClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.DescribeRecordListRequest()
        params = {
            "Domain": domain
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个DescribeRecordListResponse的实例，与请求对象对应
        resp = client.DescribeRecordList(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)






if __name__ == "__main__":
    ipv6_global = get_global_ipv6()
    get_record_list()
