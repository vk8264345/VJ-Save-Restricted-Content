import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20853306"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1ea3fe3e360e1de419753997d5907401")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vk8264345:ozSTHApYmWPuwh1p@cluster0.fgfu8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
