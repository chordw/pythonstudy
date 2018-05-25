import itchat
# itchat https://github.com/littlecodersh/ItChat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text + ",999"


itchat.auto_login(hotReload=True)
# itchat.run()
a = itchat.search_friends()
print(a)
