# 调用腾讯云API Explorer
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.dnspod.v20210323 import dnspod_client, models
import json


def dnspod_get_record_list(domain, secretId, secretKey):
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

        # 输出记录列表
        print('%-4s%-6s%-4s%-6s%-40s%-15s' % ("记录", "类型", "线路", "TTL", "记录值", "最后更新时间"))
        for record in resp.RecordList:
            if record.Type != "NS":
                print('%-5s%-8s%-4s%-6s%-40s%-15s' % (record.Name, record.Type, record.Line, record.TTL, record.Value, record.UpdatedOn))
        return resp
    except TencentCloudSDKException as err:
        print(err)


def dnspod_get_record_list_noprint(domain, secretId, secretKey):
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

        return resp
    except TencentCloudSDKException as err:
        print(err)


# 增加记录
def dnspod_add_record(Domain, SecretId, SecretKey, Value, SubDomain='@', RecordType='AAAA', RecordLine='默认'):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密 代码泄露可能会导致 SecretId 和 SecretKey
        # 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = dnspod_client.DnspodClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.CreateRecordRequest()
        params = {
            "Domain": Domain,
            "RecordType": RecordType,
            "Value": Value,
            "RecordLine": RecordLine,
            "SubDomain": SubDomain
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个CreateRecordResponse的实例，与请求对象对应
        resp = client.CreateRecord(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())
        return resp
    except TencentCloudSDKException as err:
        print(err)


def dnspod_change_record(Domain, SecretId, SecretKey, RecordId, Value, SubDomain='@', RecordType='AAAA', RecordLine='默认'):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密 代码泄露可能会导致 SecretId 和 SecretKey
        # 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "dnspod.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = dnspod_client.DnspodClient(cred, "", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ModifyRecordRequest()
        params = {
            "Domain": Domain,
            "SubDomain": SubDomain,
            "RecordType": RecordType,
            "RecordLine": RecordLine,
            "Value": Value,
            "RecordId": RecordId
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个ModifyRecordResponse的实例，与请求对象对应
        resp = client.ModifyRecord(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)