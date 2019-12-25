from base.send_request import SendRequests
from function.readfile import ReadFile
import random
class Login(SendRequests):
    def __init__(self,path):
        self.path = path
        read = ReadFile()
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
        self.wap_url = "http://demo.dataoke.com/index.php?r=login/login"
        pwd = read.read_file_txt(self.path,[])
        index = random.randint(0,len(pwd)-1)
        self.data = {"app_id": 1, "v": 20, "cac_id": "", "type": 2,
                     "phone": pwd[index][0],
                     "password": pwd[index][1][:-1]}
    def wap_token(self):
        response = self.send_request("post",self.wap_url,headers=self.headers, data=self.data).json()
        token = self.dict_get(response, "token",[])
        return token[-1]
if __name__ == '__main__':
    login = Login(r"C:\Users\1\PycharmProjects\cms_api\data\gray-pwd.txt")
    uid = login.wap_token()
    print(uid)
