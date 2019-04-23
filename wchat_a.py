def analysis(msg):
    status = True;
    if "任务" in msg.text:
        msg.user.send('成功拦截到关键字%s' % (msg.text))
        status = False;
    return status;
