import requests
import pandas as pd


def get_detail_zone(zone, api_token):
    headers = {
        "Authorization": 'Bearer ' + api_token,
        "Accept": "application/json",
    }

    try:
        response = requests.get(f"http://dynv6.com/api/v2/zones/by-name/{zone}", None, headers=headers, timeout=10)
        if response.status_code == 200:
            # 请求成功，可以处理响应数据
            data = response.json()
            for key, value in data.items():
                print(f"{key}:{value}")
            return data['id']
        else:
            # 请求失败，处理错误信息
            print(f"GET请求失败。HTTP响应代码：{response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"发生异常：{e}")


def get_list_record(zone, api_token):
    print(f"获取dvynv6 {zone} 信息")
    zoneID = get_detail_zone(zone, api_token)
    headers = {
        "Authorization": 'Bearer ' + api_token,
        "Accept": "application/json",
    }

    try:
        response = requests.get(f"https://dynv6.com/api/v2/zones/{zoneID}/records", None, headers=headers, timeout=10)
        if response.status_code == 200:
            # 请求成功，可以处理响应数据
            data = response.json()
            print(pd.DataFrame(data))
        else:
            # 请求失败，处理错误信息
            print(f"GET请求失败。HTTP响应代码：{response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"发生异常：{e}")


# 创建或更新动态DNS记录
def create_or_update_dns_record(subdomain, api_token, hostname, ipv6):
    if subdomain == '@':
        url = f"https://dynv6.com/api/update/?token={api_token}&ipv6={ipv6}&zone={hostname}"
    else:
        url = f"https://dynv6.com/api/update/?token={api_token}&ipv6={ipv6}&zone={subdomain}.{hostname}"

    try:
        response = requests.get(url,timeout=10)
        if response.status_code == 200:
            print("动态DNS记录已成功创建或更新！")
        else:
            print(f"无法创建或更新动态DNS记录。HTTP响应代码：{response.status_code}")
            print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"发生异常：{e}")


def add_record(subdomain, api_token, zone, ipv6):
    zoneID = get_detail_zone(zone, api_token)
    headers = {
        "Authorization": 'Bearer ' + api_token,
        "Accept": "application/json",
    }

    data = {
        "name": subdomain,
        "type": "AAAA",
        "data":  ipv6,
    }

    try:
        response = requests.post(f"http://dynv6.com/api/v2/zones/{zoneID}/records", json=data, headers=headers, timeout=10)
        if response.status_code == 200:
            # 请求成功，可以处理响应数据
            data=[response.json()]
            print(pd.DataFrame(data))
        else:
            # 请求失败，处理错误信息
            print(f"GET请求失败。HTTP响应代码：{response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"发生异常：{e}")