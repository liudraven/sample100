# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/3/16
# aim: 自动修改作业
import os
import sys

cur_file = os.path.abspath(__file__)
cur_path = os.path.dirname(cur_file)
# -----------------------------------------------------------------------------------------------------------
# 调用私有lib
# -----------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------
# 跨文件夹调用公有tools
# -----------------------------------------------------------------------------------------------------------
g_script_path = os.path.split(os.path.realpath(__file__))[0]
g_install_dir = os.path.realpath(g_script_path + '/../tools/')
exception_list = []
if g_install_dir not in sys.path:
    sys.path.append(g_install_dir)

if g_script_path not in sys.path:
    sys.path.append(g_script_path)

from tools.print_log import print_log


def image_recognition(image_folder_path):
    """图像识别"""
    _recognition_dict = {}
    return _recognition_dict


def deal_with_config(score_regulation_config_path):
    """读取评分规则"""
    _score_regulation_dict = {}
    return _score_regulation_dict


def do_score(recognition_dict, score_regulation_dict):
    """根据评分规则，作业字典给所有作业打分"""
    _score_result_dict = {}
    return _score_result_dict


def do_output(score_result_dict):
    """将评分结果输出成想要的格式"""
    pass


def main():
    image_folder_path = ''
    score_regulation_config_path = ''
    """图像识别"""
    recognition_dict = image_recognition(image_folder_path)

    """读取配置项"""
    score_regulation_dict = deal_with_config(score_regulation_config_path)

    """开始评分"""
    score_result_dict = do_score(recognition_dict, score_regulation_dict)

    """组织成希望获取的输出形式"""
    do_output(score_result_dict)


if __name__ == '__main__':
    main()
