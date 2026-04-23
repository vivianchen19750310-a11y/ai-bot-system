import gspread
import json
import os
from google.oauth2.service_account import Credentials
from datetime import datetime

# 從 GitHub Secret 讀取 JSON
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
    
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

# 開啟試算表
sheet = client.open("IG名單系統").sheet1

def save_to_sheet(message, category):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([time, message, category])
    print("已寫入Google Sheet：", message, category)

def bot_reply(message):
    if "懶人包" in message:
        category = "懶人包"
    elif "團購" in message:
        category = "團購"
    elif "保健" in message:
        category = "保健保養"
    else:
        category = "其他"

    save_to_sheet(message, category)

# 測試
bot_reply("懶人包")
bot_reply("團購優惠")
bot_reply("保健推薦")
