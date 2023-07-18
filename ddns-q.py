

import argparse

import config_func
from DNS import dnspod
from command import init, reset, start

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
start_parser.add_argument("--time", "-t", default="10", help="检查ipv6间隔，默认为10s")

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
elif args.command == 'start':
    start.start(args.subdomain, args.time)
