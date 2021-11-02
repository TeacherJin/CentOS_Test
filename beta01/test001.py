# 关于文件操作的测试

import sys
import os

# 输出实验内容
print('在完成本实验时，请打开两个终端，一个运行本程序，另一个用于完成实验内容。以下是实验要求：\n')
print(r'''1. 在主目录中创建目录dirA
2. 在主目录中创建多层目录testdirB/testB/testB1/testB2
3. 在目录testB中创建文件b1和b2
4. 在主目录中创建文件F1
5. 将文件F1移动到目录dirA中，并改名为File1
6. 在主目录中创建文件F2，复制到目录testdirB中，同时改名为File2
7. 创建目录dirB，将目录dirA复制到dirB中
8. 删除目录dirB'''+'\n')


# 获取主目录的路径
home_path = os.environ['HOME']

# 清除命令历史记录
def clean_history():
    # 清空.bash_history文件内容
    # 实测生效
    open(home_path+'/.bash_history', 'w').close()
    # 清除相应的文件???

# 在指定文件中搜索关键词，file表示文件路径，kw表示关键词
def searchKeyword(file,kw):
    with open(file) as f:
        lines=f.readlines()
        for line in lines:
            if kw in line:
                return True
    
    return False


# 使用字典表示每个步骤正确与否
d1 = [x for x in range(1, 8)]
d2 = [False] * 7
result = dict(zip(d1, d2))

# 检测每个条目是否完成
def detectTest():
    global result
    # 1，判断目录dirA是否存在
    result[1]=os.path.exists(home_path+'/dirA')
        
    # 2，判断多层目录testdirB/testB/testB1/testB2是否存在
    result[2]=os.path.exists(home_path+'/testdirB/testB/testB1/testB2')

    # 3，判断是否在目录testB中创建文件b1和b2
    result[3]=os.path.exists(home_path+'/testdirB/testB/b1') and os.path.exists(home_path+'/testdirB/testB/b2')
    
    # 4，搜索命令历史记录，并检测文件是否存在
    result[4]=searchKeyword(home_path+'/.bash_history','touch F1') and os.path.exists(home_path+'/dirA/File1')
    
    # 5，搜索命令历史记录，并检测文件是否存在
    result[5]=searchKeyword(home_path+'/.bash_history','cp F2 testdirB/File2') and os.path.exists(home_path+'/F2') and os.path.exists(home_path+'/testdirB/File2')
    
    # 6，搜索命令历史记录
    result[6]=searchKeyword(home_path+'/.bash_history','mkdir dirB') and searchKeyword(home_path+'/.bash_history','cp -R dirA dirB')
    
    # 7，搜索命令历史记录
    result[7]=searchKeyword(home_path+'/.bash_history','rm -rf dirB')
   
 
choice = input("是否要开始测试？Y/N")
if choice == 'Y' or choice == 'y':
    print('请启动另一个终端，开始完成实验中的每一步')
    # 清理历史记录文件
    clean_history()
    endString=input('完成后请关闭做实验的终端，并输入 end')
    if(endString == 'end'):
        detectTest()
        print('你的实验结果是：')
        for key,value in result.items():
            print("第",key,"步：",'正确' if value else '错误')
else:
    print('退出程序')
    sys.exit()
