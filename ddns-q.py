

import argparse

import config_func
from DNS import dnspod, dynv6
from command import init, reset, start, set, startup, ipv6

config_path = 'conf/ddns.conf'


# 解析命令

# 创建解析器
parser = argparse.ArgumentParser(description='ddns-q help')
# 创建子命令解析器
subparsers = parser.add_subparsers(dest='command', help='可用的命令')
# init初始化命令
init_parser = subparsers.add_parser("init", help="初始化ddns-q")

# reset重置命令
reset_parser = subparsers.add_parser("reset", help="重置ddns-q")

# list展示记录列表命令
list_parser = subparsers.add_parser("list", help="列出当前域名的记录")

# 启动命令
start_parser = subparsers.add_parser("start", help="开始运行脚本")
start_parser.add_argument("--subdomain", "-s", default="@", help="主机记录(例如@,www,默认为@)")
start_parser.add_argument("--time", "-t", default="30", help="检查ipv6间隔，默认为30s")

# set设定命令
set_parser = subparsers.add_parser("set", help="设置配置(例如ddns-q set dns dnspod)")
set_parser.add_argument("key", help="配置项")
set_parser.add_argument("value", help="配置值")

# startup开机自启命令
startup_parser = subparsers.add_parser("startup", help="设置开机自启")
startup_parser.add_argument("--subdomain", "-s", default="@", help="主机记录(例如@,www,默认为@)")
startup_parser.add_argument("--time", "-t", default="30", help="检查ipv6间隔，默认为30s")

# ipv6获取命令
ipv6_parser = subparsers.add_parser("ipv6", help="获取本机ipv6")

# 解析命令行参数
args = parser.parse_args()


# 处理命令
if args.command == 'init':
    print("开始初始化ddns-q")
    init.init()
elif args.command == 'reset':
    reset.reset()
    print("已重置ddns-q")
elif args.command == 'list':
    config = config_func.read_config(config_path)
    if config['dns'] == 'dnspod':
        dnspod.dnspod_get_record_list(config['domain'], config['secretid'], config['secretkey'])
    elif config['dns'] == 'dynv6':
        dynv6.get_list_record(config['domain'], config['api_token_dynv6'])

elif args.command == 'start':
    start.start(args.subdomain, args.time)
elif args.command == 'set':
    set.set(args.key, args.value)
elif args.command == 'startup':
    startup.startup('start -s '+args.subdomain+' -t '+args.time)
elif args.command == 'ipv6':
    ipv6.get_global_ipv6()