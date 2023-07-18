from config_func import modify_config, read_config, read_config_value

path = 'conf/ddns.conf'


def init():
    config = {}
    dns = ["dnspod"]  # dns服务商列表
    config = read_config(path)
    for value in config.values():
        if value != '':
            print("已有部分或完全配置，不需要初始化(可使用reset重置)")
            return 0

        # 用户初始化值
    while True:
        try:
            num = int(input("选择DNS服务商:\n1.腾讯云(DNSPod)\n"))
            modify_config(path, 'dns', dns[num - 1])
            break
        except ValueError:
            print("请输入数字选项\n")

    while True:
        try:
            domain = input("设置域名:")
            modify_config(path, 'domain', domain)
            break
        except ValueError:
            print("请输入域名\n")

    if read_config_value(path, 'dns') == 'dnspod':
        while True:
            try:
                secretid = input("输入secretId:")
                modify_config(path, 'secretid', secretid)
                break
            except ValueError:
                print("请输入secretId\n")

        while True:
            try:
                secretkey = input("输入secretKey:")
                modify_config(path, 'secretkey', secretkey)
                break
            except ValueError:
                print("请输入secretKey\n")
# 使用dotenv来修改配置文件

