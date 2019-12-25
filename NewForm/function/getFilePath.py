import os
class GetFilePath(): #工程目录
    def get_dir(slef,path):  # 获取目录路径
        dir = []
        for root, dirs, files in os.walk(path):  # 遍历path,进入每个目录都调用visit函数，，有3个参数，root表示目录路径，dirs表示当前目录的目录名，files代表当前目录的文件名
            for i in dirs:
                # print(dir)             #文件夹名
                tmp = os.path.join(root, i)  # 把目录和文件名合成一个路径
                dir.append(tmp)
        return dir
    def get_file(self,path):  # 文件夹目录，获取文件路径
        file_path = []
        for root, dirs, files in os.walk(self.get_dir(path)[3]):
            for file in files:
                # print(file)     #文件名
                file_path.append(os.path.join(root, file))
        return file_path