from base.send_request import SendRequests
from function.readfile import ReadFile
import random
class Login(SendRequests):
    def __init__(self,path):
        self.path = path
        read = ReadFile()
        self.ios_url = read.convert_dict(r"D:\data\user\url_ios.txt")
        self.android_url = read.convert_dict(r"D:\data\user\url.txt")
        self.wap_url = "http://titijie.haojiequ.com/index.php?r=login/login"
        pwd = read.read_file_txt(self.path,[])
        index = random.randint(0,len(pwd)-1)
        self.data = {"app_id": 1, "v": 20, "cac_id": "", "type": 2,
                     "phone": pwd[index][0],
                     "password":pwd[index][1][:-1]}
    def ios_uid(self,key):
        response = self.send_request("post",self.ios_url[key],self.data).json()
        uid = self.dict_get(response,"uid",[])
        return uid[-1]
    def android_uid(self,key):
        response = self.send_request("post",self.android_url[key],self.data).json()
        uid = self.dict_get(response, "uid", [])
        return uid[-1]
    def wap_token(self):
        response = self.send_request("post",self.wap_url,self.data).json()
        token = self.dict_get(response, "token",[])
        return token[-1]
if __name__ == '__main__':
    login = Login(r"C:\Users\1\PycharmProjects\cms_api\data\pwd.txt")
    #uid = login.android_uid("login")
    uid = login.wap_token()
    print(uid)
