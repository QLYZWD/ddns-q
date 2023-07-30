# -*- coding: utf-8 -*-
from dotenv import dotenv_values, set_key
def modify_config(file_path, target_option, new_value):
    config = dotenv_values(file_path)

    # 修改目标配置项的值
    config[target_option] = new_value

    # 将修改后的配置写回文件
    set_key(file_path, target_option, new_value, quote_mode='never')


# 读取整个配置文件
def read_config(file_path):
    config_data = dotenv_values(file_path)
    return config_data


# 读取单个配置的值
def read_config_value(file_path, key):
    config_data = dotenv_values(file_path)
    value = config_data.get(key)
    return value


