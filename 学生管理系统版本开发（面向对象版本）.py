students=[]
def menu():
    print('-' * 40)
    print("欢迎使用传智播客，黑马程序员学生管理系统")
    print("[1]添加学生信息")
    print("[2]删除学生信息")
    print("[3]修改学生信息")
    print("[4]查询学生信息")
    print("[5]遍历所有学生信息")
    print("[6]退出系统")
    print('-' * 40)


def add_student():
    student = {}
    name = input("请输入学生的姓名：")
    student["name"] = name
    student["age"] = int(input("请输入学生的年龄："))
    student["mobile"] = input("请输入学生的电话：")
    #声明全局列表
    global students
    students.append(student)
    print(f"学生{name}的信息添加成功")


def del_student():
    name = input("请输入你要选择删除的学生姓名：")
    # 声明全局列表
    global students
    for i in students:
        if i["name"] == name:
            students.remove(i)
            print(f'学生{name}的信息已删除')
            break
    else:
        print("您要删除的学生信息不存在")


def get_all_student():
    global students
    for i in students:
        print(i)


def edit_student():
    name = input("请输入你要选择修改的学生姓名：")
    # 声明全局列表
    global students
    for i in students:
        if i["name"] == name:
            i["name"]=input("请输入修改后的学生姓名：")
            i["age"] = input("请输入修改后的学生年龄：")
            i["mobile"] = input("请输入修改后的学生电话：")
            print(f'学生{name}的信息已修改')
            break
    else:
        print("您要修改的学生信息不存在")


def get_student():
    name = input("请输入你要选择查询的学生姓名：")
    # 声明全局列表
    global students
    for i in students:
        if i["name"] == name:

            print(i)
            break
    else:
        print("您要查询的学生信息不存在")


while True:
    menu()
    user_num=int(input("请输入您要操作的功能编号:"))
    if user_num == 1:
        # 添加学生信息
        add_student()
    elif user_num ==2:
        del_student()
    elif user_num ==3:
        edit_student()
    elif user_num ==4:
        get_student()
    elif user_num ==5:
        get_all_student()
    elif user_num ==6:
        print("退出当前系统")
        break
    else:
        print("您输入的功能编号不正确，请重新输入")