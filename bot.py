def bot_reply(message):
    if any(word in message for word in ["懶人包", "清單", "資訊", "給我", "有嗎"]):
        return "我幫你整理好懶人包了，這邊可以直接看👇"
    elif any(word in message for word in ["團購", "我要", "哪裡買", "下單"]):
        return "目前有團購優惠，我幫你整理好連結👇"
    elif any(word in message for word in ["保健", "保養", "怎麼選", "適合我嗎", "推薦", "吃什麼", "擦什麼"]):
        return "我可以幫你評估適合的保健或保養產品，請問你的需求或困擾是什麼呢？"
    else:
        return "我收到你的訊息了，我幫你整理後回覆你"

user_message = input("請輸入訊息：")
print(bot_reply(user_message))