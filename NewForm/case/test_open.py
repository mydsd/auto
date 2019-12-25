import pytest
import os
import json
import datetime
import copy
import random
from base.send_request import SendRequests
from function.readfile import ReadFile
from function.connectdb import ConnectDb
from function.json_data import Json_Data
from function.getFilePath import GetFilePath
read = ReadFile()
get_path = GetFilePath()
read_json = Json_Data()
data_file_path = get_path.get_file(os.path.abspath('..'))
config_data = read.read_yaml(data_file_path[0])
headers = {'User-Agent':config_data['test1']}
send = SendRequests()
url = read.read_yaml(data_file_path[1])
class TestSpecialList():
    def setup(self):
        self.data = {'id':'','al_type':1}
        if 'haojiequ' in url['special-list']:
            self.connect = ConnectDb()
        elif 'dataoke' in url['special-list']:
            self.connect = ConnectDb(host="39.107.98.125", port=3307, user="dataoke2", password="0Ab9v4Ou0PsMk2soMfVk",dbname="dataoke2")
    def test_list(self):
        res = send.send_request('get',url['special-list'],headers=headers).json()
        id = send.dict_get(res,'id',[])
        self.data['id'] = random.choice(id)
        self.response = send.send_request('get',url=url['special-info'],params=self.data).json()
        tmp = send.dict_get(self.response,'id',[])
        assert (tmp[0] == self.data['id'])
    def teardown(self):
        self.connect.close_db()
        #print(self.response)
if __name__ == '__main__':
    pytest.main(["-s", "test_open.py"])