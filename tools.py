
# 显示系统菜单
def show_menu():
    """显示系统信息"""
    print("=" * 50)
    print("\t\t\t欢迎使用【名片管理系统】 V 1.0\n")
    pos = "1:新建名片\t2:显示全部\t3:查询名片\t0:退出系统"
    print(pos.center(33))
    print("=" * 50)


# 处理用户的选择
# 保存用户信息
user_info = []
# 1,新建名片
def new_card():
    """新建名片"""
    print("-"*50)
    name_str = input("请输入你的姓名：")
    phone_str = int(input("请输入您的电话："))
    qq_str = int(input("请输入您的qq号码："))
    user_card = {"name":name_str,"phone":phone_str,"qq":qq_str}
    user_info.append(user_card)
    print("%s的名片创建完成！"%name_str)


# 2,显示全部
def show_all():
    """
    显示全部名片信息
    :return: 如果列表中有名片信息就返回，没有则给出提示
    """
    print("-" * 50)
    #打印表头
    # 判断列表是否为空
    if len(user_info) == 0:
        print("没有查询到任何名片信息")
        return
    for k in ["姓名", "电话", "QQ"]:
        print(k,end="\t\t")
    print("")
    print("-"*50)
    #遍历输出名片列表信息
    for name in user_info:
        rename = "%s\t\t%s\t\t%s\t\t"%(name["name"],name["phone"],name["qq"])
        print(rename)


# 3,查询名片
def search_card():
    """
    查询用户名片
    """
    #定义一个变量来保存用户输入的名字
    u_name = input("请输入您的名字：")
    #检查用户输入的名字是否存在
    for card_name in user_info:
        #如果在字典中找到输入的名字，打印用户所有信息
        if card_name["name"] == u_name:
            #打印表头
            print("姓名\t\t电话\t\tqq")
            #打印用户信息
            print("%s\t\t%s\t\t%s"%(card_name["name"],card_name["phone"],card_name["qq"]))
            deal_card(card_name)
            # return card_name
            break
    else:
        print("抱歉，没有找到%s这个用户！"%u_name)

#   处理用户信息
def deal_card(card_name):
    """
    处理用对名片的操作【改/删/返回】
    :param card_name:
    """
    deal_c = input("[1]修改名片\t[2]删除名片\t[0]返回上级菜单\n"
                   "请输入您的操作：")
    if deal_c == "1":
        print("修改名片")
        card_name["name"] = input_card_name(card_name["name"],"请输入姓名：")
        card_name["phone"] = input_card_name(card_name["phone"],"请输入您的电话：")
        card_name["qq"] = input_card_name(card_name["qq"],"请输入您的qq:")
        print("名片修改完成！")
    elif deal_c == "2":
        user_info.remove(card_name)
        print("%s的名片成功删除！" % card_name["name"])
    print("-" * 50)


def input_card_name(card_name,tip_masege):
    """
    检查用户是否输入了内容
    :param card_name: 原字典中的信息
    :param tip_masege: 提示用户输入
    :return:如果用户输入了内容就保存用户的输入，没有则返回原字典中信息
    """
    result = input(tip_masege)
    if len(result) > 0:
        return result
    else:
        return card_name


def input_opetions(tip):
    ret = input(tip)
    if len(ret) > 0:
        print("您输入的选项是【%s】 " % ret)
        return ret
    else:
        print("请输入正确的选项！")