print("bot started")

def bot_reply(message):
    if "懶人包" in message:
        print("分類：懶人包")
    elif "團購" in message:
        print("分類：團購")
    elif "保健" in message:
        print("分類：保健保養")
    else:
        print("分類：其他")

# 模擬一則留言
bot_reply("懶人包")
