import os
import winshell
import pythoncom
import sys
from win32com.client import Dispatch


def create_shortcut_with_arguments(target_path, shortcut_path, arguments):
    try:
        # 获取Windows Shell的对象
        shell = Dispatch('WScript.Shell')

        # 创建快捷方式
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = target_path
        shortcut.Arguments = arguments

        # 设置快捷方式的起始位置为目标可执行文件所在的目录
        shortcut.WorkingDirectory = os.path.dirname(target_path)

        shortcut.Save()

        print(f"已成功创建启动项:"+arguments)
    except pythoncom.com_error as e:
        print(f"创建快捷方式时出现错误：{e}")


def get_script_path():
    # 获取当前脚本的文件路径
    script_path = os.path.abspath(sys.argv[0])
    return script_path


def startup(arguments):
    # 目标可执行文件的路径
    target_exe_path = os.path.abspath(sys.argv[0])

    # 快捷方式的保存路径及名称
    shortcut_folder = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    shortcut_name = "ddns-q.lnk"
    shortcut_path = os.path.join(shortcut_folder, shortcut_name)

    # 创建带参数的快捷方式
    create_shortcut_with_arguments(target_exe_path, shortcut_path, arguments)



