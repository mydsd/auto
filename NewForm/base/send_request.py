import requests
import json
import os
from function.json_data import Json_Data
from function.log import Logger
from function.readfile import ReadFile
log = Logger(r"D:\data\log\log.txt")
session = requests.Session()
class SendRequests(Json_Data):
    def send_requests(self,args):
        type = args["type"]
        url = args["url"]
        method = args["method"]
        verify = False
        if args["headers"] == "":
            headers = None
        else:
            headers = eval(args["headers"])
        if args["params"] == "":
            params = None
        else:
            params = eval(args["params"])
        if args["body"] == "":
            body = None
        else:
            form = eval(args["body"])
            if type == "json":
                body = json.dumps(form)
            elif type == "data":
                body = form
            else:
                body = form
        if args["cookies"] =="":
            cookies = None
        else:
            cookies = eval(args["cookies"])
        try:
            response = requests.request(method=method,url=url,data=body,params=params,headers=headers,verify=verify,cookies=cookies)
            if response.status_code == 200:
                return response
            else:
                print(response.text,'\n',response.status_code)
        except Exception as error:
            log.info("请检查请求地址【{}】以及错误详情{}！".format(url,error))
    '''multiple_files = [
        ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
        ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
         r = requests.post(url, files=multiple_files) #上传图片，分模块编码'''
    def send_request(self,method,url,data=None,params=None,headers=None,files=None,verify=False,cookies=None,type=0):
        try:
            if type == 0:
                response = requests.request(method=method,url=url,data=data,params=params,headers=headers,files=files,
                                            verify=verify,cookies=cookies)
                if response.status_code == 200:
                    return response
                else:
                    print(response.text, response.status_code)
            elif type == 1:
                response = session.request(method=method, url=url, data=data,params=params,headers=headers, files=files,
                                            verify=verify, cookies=cookies)
                if response.status_code == 200:
                    return response
                else:
                    print(response.text, response.status_code)
        except Exception as error:
            msg = "接口调用失败，请检查详情：【{}】，{}".format(url, error)
            log.info(msg)
            return msg
if __name__ == '__main__':
    api_data = ReadFile().read_file_xlsx(r"D:\data\ddtdata\column.xlsx")
    data = SendRequests().send_requests(api_data[0]).json()
    data1 = SendRequests().send_request("get","https://www.baidu.com/")
    print(data,data1)
