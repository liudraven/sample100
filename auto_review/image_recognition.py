# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/3/16
# aim: 图像识别

# -----------------------------------------------------------------------------------------------------------
# 调用公共库
# -----------------------------------------------------------------------------------------------------------
import requests
import json
import os
import sys
import base64

cur_file = os.path.abspath(__file__)
cur_path = os.path.dirname(cur_file)
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

# -----------------------------------------------------------------------------------------------------------
# 定义公共参数
# -----------------------------------------------------------------------------------------------------------
IMAGE_RECOGNITION_API_URL = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage'


# -----------------------------------------------------------------------------------------------------------
# 功能函数
# -----------------------------------------------------------------------------------------------------------
def test_api():
    """测试是否可以调用api接口"""
    print_log('INFO', 'begin to test api function')
    _data = {}
    _test_url = 'https://api.apiopen.top/singlePoetry'
    print_log('INFO', 'will do post with URL:{0} DATA:{1}'.format(_test_url, _data))
    _response = requests.post(_test_url, data=_data)
    _response_data = json.loads(_response.text)
    print_log('INFO', 'get response from URl:{0}'.format(_test_url))
    print_log('INFO', 'response : {0}'.format(_response_data))


def get_test_image():
    """测试是否可以获取 符合百度接口的图片"""
    image_folder = os.path.realpath(cur_path + '/images_source')
    _image_list = os.walk(image_folder)

    # 文件
    print_log('INFO', '_image_list : {0}'.format(_image_list))
    _image_name_list = []
    for root, dirs, files in _image_list:
        _image_name_list = files
    print_log('INFO', '_image_name_list : {0}'.format(_image_name_list))

    # 文件绝对路径
    _image_file_path_list = []
    for _file in _image_name_list:
        _image_file_path_list.append([os.path.realpath(image_folder + '/' + _file), _file])
    print_log('INFO', '_image_file_path_list : {0}'.format(_image_file_path_list))

    # 文件数据
    _image_dict = {}
    for _image_path in _image_file_path_list:
        print_log('INFO', '_image_path[0] : {0}'.format(_image_path[0]))
        print_log('INFO', '_image_path[1] : {0}'.format(_image_path[1]))
        with open(_image_path[0], 'r+b') as f:
            img_data = base64.b64encode(f.read())
            _image_dict[_image_path[1]] = img_data

    return _image_dict


def get_token():
    """根据应用用户的信息获取百度PAI的token"""
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    api_key = 'vKtWmG1XSPOBGSexlGAshGEA'
    secret_key = '9eemncR5nmkYOtkr5vpr2x2fGHLZP2r9'
    token = ''
    token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}' \
                '&client_secret={1}'.format(api_key, secret_key)

    _response = requests.get(token_url)
    if _response:
        token_dict = json.loads(_response.text)
        access_token = token_dict['access_token']
        expires_in = token_dict['access_token']
        print_log('INFO', 'get token from api success: {0}'.format(access_token))

    return token


def test_baidu_shibie_api(image_dict):
    """测试是否可以调用百度接口--通用文字识别（标准版）"""
    """页面链接 https://ai.baidu.com/ai-doc/OCR/zk3h7xz52"""
    token = '24.705d2072ee1bbc201f1418863efdc918.2592000.1655562676.282335-26275249'
    access_token = token
    _IMAGE_RECOGNITION_API_URL = IMAGE_RECOGNITION_API_URL + "?access_token=" + access_token

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    params = {}
    _result = {}
    for key, value in image_dict.items():
        params = {"image": value}
        _response = requests.post(_IMAGE_RECOGNITION_API_URL, data=params, headers=headers)
        _response_data = json.loads(_response.text)
        print_log('INFO', 'get response from URl:{0}'.format(_IMAGE_RECOGNITION_API_URL))
        print_log('INFO', 'response : {0}'.format(_response_data))
        _result[key] = _response_data

    with open('result.txt', 'a') as f:
        for key, item in _result.items():
            f.writelines(item + '\n\r')


# -----------------------------------------------------------------------------------------------------------
# 主函数
# -----------------------------------------------------------------------------------------------------------
def main():
    image_dict = get_test_image()
    test_baidu_shibie_api(image_dict)


if __name__ == '__main__':
    main()


