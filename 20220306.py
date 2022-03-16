# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/3/16
# aim: 自动修改作业


def image_recognition(image_folder_path):
    """图像识别"""
    _recognition_dict = {}
    return _recognition_dict


def deal_with_config(score_regulation_config_path):
    """读取评分规则"""
    _score_regulation_dict = {}
    return _score_regulation_dict


def do_score(recognition_dict, score_regulation_dict):


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



if __name__ == '__main__':
    main()
