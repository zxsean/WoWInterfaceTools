import sys
import zipfile
import os
import shutil


def unzip_file(_path):
    zip_path = os.path.join(_path, "wow_interface.zip")
    if os.path.exists(zip_path):
        print("zip file exists")

        # 删除Interface和WTF目录
        dir_interface = os.path.join(_path, "Interface")
        dir_wtf = os.path.join(_path, "WTF")
        if os.path.exists(dir_interface):
            print("Interface exists")
            shutil.rmtree(dir_interface)
            print("Interface deleted")
        if os.path.exists(dir_wtf):
            print("WTF exists")
            shutil.rmtree(dir_wtf)
            print("WTF deleted")

        with zipfile.ZipFile(zip_path, 'r') as target_zip:
            print("开始解压...")
            target_zip.extractall(_path)

        print("解压完成")
    else:
        print("zip file is not exist")
        sys.exit()


def zip_files(_path):
    # 判断路径下面是否有Interface和WTF
    dir_interface = os.path.join(_path, "Interface")
    dir_wtf = os.path.join(_path, "WTF")

    if os.path.exists(dir_interface) and os.path.exists(dir_wtf):
        print("Interface and WTF exists")
        zip_path = os.path.join(_path, "wow_interface.zip")

        print("开始压缩...")

        with zipfile.ZipFile(zip_path, 'w') as target_zip:
            # 将Interface目录下的文件压缩到zip文件中
            for i in os.walk(dir_interface):
                for j in i[2]:
                    _filePath = ''.join((i[0], '\\', j))
                    # print(_filePath)
                    _index = _filePath.find('Interface\\AddOns\\')
                    if _index <= 0:
                        print(_index)
                    else:
                        # print(_filePath[_index:])
                        target_zip.write(_filePath, _filePath[_index:], compress_type=zipfile.ZIP_DEFLATED)

            # 将WTF目录下的文件压缩到zip文件中
            for i in os.walk(dir_wtf):
                for j in i[2]:
                    _filePath = ''.join((i[0], '\\', j))
                    # print(_filePath)
                    _index = _filePath.find('WTF\\')
                    if _index <= 0:
                        print(_index)
                    else:
                        # print(_filePath[_index:])
                        target_zip.write(_filePath, _filePath[_index:], compress_type=zipfile.ZIP_DEFLATED)
    else:
        print("Interface or WTF is not exist")
        sys.exit()


if __name__ == '__main__':
    while True:
        input_str = input("1, 解压zip文件\n2, 压缩文件\n")

        if input_str == "1":
            os.system("cls")
            path = sys.argv[0]
            dir_path = os.path.dirname(path)
            print("执行文件路径:%s" % path)
            print("文件路径:%s" % dir_path)
            unzip_file(dir_path)
            break
        elif input_str == "2":
            os.system("cls")
            path = sys.argv[0]
            dir_path = os.path.dirname(path)
            print("执行文件路径:%s" % path)
            print("文件路径:%s" % dir_path)

            zip_files(dir_path)
            print("压缩完成")
            break
        else:
            os.system("cls")
            print("输入错误，请重新输入")

    input('Press any key to quit program.')
