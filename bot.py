print("bot started")

def bot_reply(message):
    if "懶人包" in message:
        print("懶人包已記錄")
    elif "團購" in message:
        print("團購已記錄")
    elif "保健" in message:
        print("保健已記錄")
    else:
        print("其他已記錄")

bot_reply("懶人包")
