import csv
from datetime import datetime

def save_to_csv(message, category):
    file_name = "lead_list.csv"
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([time, message, category])

    print("已寫入名單：", message, category)


def bot_reply(message):

    if "懶人包" in message:
        category = "懶人包"
    elif "團購" in message:
        category = "團購"
    elif "保健" in message:
        category = "保健保養"
    else:
        category = "其他"

    save_to_csv(message, category)


# 模擬留言
bot_reply("懶人包")
bot_reply("團購優惠")
bot_reply("保健推薦")
