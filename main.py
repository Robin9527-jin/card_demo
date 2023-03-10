
import tools

while True:
    #显示系统信息
    tools.show_menu()
    ctl = tools.input_opetions("请输入操作选项：")
    # print("您输入的选项是【%s】 " % ctl)

    # 判断用户的输入是否是【1，2，3】
    if ctl in ["1" ,"2" ,"3"]:
        if ctl == "1":
            tools.new_card()
        elif ctl == "2":
            tools.show_all()
        else:
            tools.search_card()

    # 如果输入0表示退出系统
    elif ctl == "0":
        print("系统已经退出")
        break
    # 如果输入其他数字，提示用户输入错误
    else:
        tools.input_opetions("请输入操作选项：")
        # print("您的输入有误，请重新输入！")



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('PyCharm')


