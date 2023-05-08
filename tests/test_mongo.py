import pymongo

uri = "mongodb://vkltd:piskogryz@45.12.238.170:27017/?authSource=chatgpt_telegram_bot"

client = pymongo.MongoClient(uri)
db = client["chatgpt_telegram_bot"]
user = db["user"]
user.count_documents({"_id":5048075977})

# mongosh --port 27017 -u vkltd -p  --authenticationDatabase 'chatgpt_telegram_bot'