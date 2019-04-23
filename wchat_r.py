import itchat, time, wchat_a, os
from itchat.content import *


os.system("mode con cols=120 lines=9999")
# Auth Sena 请勿删除版权
            
    
# 通过以下命令可以在登陆的时候使用命令行显示二维码：
# itchat.auto_login(enableCmdQR=True)

# 部分系统可能字幅宽度有出入，可以通过将enableCmdQR赋值为特定的倍数进行调整：
# 如部分的linux系统，块字符的宽度为一个字符（正常应为两字符），故赋值为2
# itchat.auto_login(enableCmdQR=2)

# 默认控制台背景色为暗色（黑色），若背景色为浅色（白色），可以将enableCmdQR赋值为负值：
# itchat.auto_login(enableCmdQR=-1)

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    if wchat_a.analysis(msg) :
        print("【私聊信息】 %s" % (msg.text));
    msg.user.send('接收到%s类型: %s【AI程序自动学习中】' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print("download_files(msg)");
    #msg.download(msg.fileName)
    #typeSymbol = {
    #    PICTURE: 'img',
    #    VIDEO: 'vid', }.get(msg.type, 'fil')
    #return '@%s@%s' % (typeSymbol, msg.fileName)
    msg.user.send('接收到%s类型: %s文件, 自动保存成功【AI程序自动学习中】' % (msg.type, msg.fileName));

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print("add_friend(msg)");
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print("【群消息】 %s" % (msg.text));
    # 如果是群聊判断是否被@了
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))

    
itchat.auto_login(enableCmdQR=True)
itchat.run(True)

itchat.send('成功启动WC管理', toUserName='filehelper')