import xlrd
import configparser
import os
import yaml
from xlutils.copy import copy
from function.log import Logger
config = configparser.ConfigParser()
class ReadFile():
    api_log = Logger(r"D:\data\log\log.txt")
    def read_file_txt(self,path,tmp_list):
        try:
            if "txt" in path or "csv" in path:
                with open(path,"r",encoding="utf-8") as file:
                    parameter = file.readlines()
                    for i in parameter:
                        if isinstance(tmp_list, list):
                            tmp_list.append(i.split(","))
                        else:
                            print("请传入列表参数!")
                            msg = "请传入列表参数!"
                            self.api_log.info(msg)
            else:
                print("请传入txt文本类型或csv文件类型!")
                msg = "请传入txt文本类型或csv文件类型!"
                self.api_log.info(msg)
        except:
            print("未找到文件，请确认文件路径是否正确!")
            msg = "未找到文件，请确认文件路径是否正确!"
            self.api_log.info(msg)
        return tmp_list
    '''将Excel文件转换成字典，sheet索引从0开始'''
    def read_file_xlsx(self,path,index=0):
        try:
            if "xlsx" in path:
                with xlrd.open_workbook(path) as sheet:
                    table = sheet.sheet_by_index(index)
                    nrows = table.nrows #获取行
                    ncols = table.ncols #获取列
                    '''将Excel第一行做为key值'''
                    keys = table.row_values(0)
                    if nrows > 1 and ncols > 1:
                        api_data = []
                        for row in range(1,nrows):
                            values = table.row_values(row)
                            api_dict = dict(zip(keys,values))
                            api_data.append(api_dict)
                        return api_data
                    else:
                        print("请在Excel文件中填写测试用例数据！")
            else:
                print("请传入Excel文件!")
                self.api_log.info("请传入Excel文件!")
        except:
            print("请检查文件路径或格式!")
            self.api_log.info("请检查文件路径!")
    '''转换为字典'''
    def convert_dict(self,path):
        dict = {}
        for i in self.read_file_txt(path,[]):
            if len(i) == 2:
                dict[i[0]] = i[1][:-1]
        return dict
    '''读取配置文件'''
    def config_data(self,path,section,key):
        config.read(path)
        data = config.get(section,key)
        return data
    '''修改Excel文件'''
    def change_excel(self,path,col=None,value=None,index=0):
        with xlrd.open_workbook(path) as sheet:
            table = sheet.sheet_by_index(index)
            rows = table.nrows
            wb = copy(sheet)
            ws = wb.get_sheet(index)
            for row in range(1,rows):
                ws.write(row,col,value)
            wb.save(path)
    '''读取yaml文件'''
    def read_yaml(self,path):
        with open(path, 'r', encoding='utf-8') as file:
            data = file.read()
        return yaml.unsafe_load(data)
if __name__ == "__main__":
    data = ReadFile().read_file_xlsx(r"D:\data\ddtdata\test.xlsx")
    print(data)
    con = ReadFile()
    urlc = con.config_data(r"D:\data\user\url_ios.conf","url","count")
    url = con.convert_dict(r"D:\data\user\url_ios.txt")
    print(url)
    print(urlc)