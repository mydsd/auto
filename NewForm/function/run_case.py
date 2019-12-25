import unittest
from HTMLTestRunner import HTMLTestRunner
#from BeautifulReport import BeautifulReport
from function.send_email import SendEmail
from time import strftime
now_time = strftime("%Y%m%d%H%M")
class RunCase():
    def __init__(self,test_case):
        self.case = test_case
    def unittest_run(self):
        discover = unittest.defaultTestLoader.discover(start_dir="case",
                                                       pattern="{}".format(self.case))
        runner = unittest.TextTestRunner()
        runner.run(discover)
    def html_report(self,path,name="测试人员",title="接口自动化测试报告",description="测试环境：window10，Chrome，16G内存",):
        path1 = path.split(".")
        case_name = path1[0]+now_time+"."+path1[1]
        with open(r"{}".format(case_name),"wb") as file:
            runner = HTMLTestRunner(
                stream= file,
                title= title,
                tester= name,
                description= description,
            )
            discover = unittest.defaultTestLoader.discover(start_dir="case",
                                                           pattern="{}".format(self.case))
            runner.run(discover)
        SendEmail(path=case_name).send_email()
    # def beautiful_report(self,name):
    #     name1 = name.split(".")
    #     filename = name1[0] + now_time + "." + name1[1]
    #     discover = unittest.defaultTestLoader.discover(start_dir="case",
    #                                                    pattern="{}".format(self.case))
    #     report = BeautifulReport(discover)
    #     report.report(filename=filename,  # 文件名
    #                   description="接口自动化测试用例",  # 用例名称
    #                   log_path=r"D:\report"  # 路径
    #                   )
    #     SendEmail(path="D:\\report"+"\\"+filename).send_email()
if __name__ == '__main__':
    RunCase("test_ddt*.py").html_report(r"D:\report\aaa.html")
    #RunCase("test_ddt*.py").beautiful_report("aaaaa.html")
