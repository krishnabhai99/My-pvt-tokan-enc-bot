import os
import time
import re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # Pyro client config
    from os import environ

    API = environ.get("API", "")  # Shortlink API (keep it secret)
    URL = environ.get("URL", "anylinks.in")  # Shortlink domain without https://
    VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "")  # How to open link
    BOT_USERNAME = environ.get("BOT_USERNAME", "")  # Bot username without @
    VERIFY = environ.get("VERIFY", "True").capitalize()  # Ensure correct capitalization
    API_ID = int(environ.get("API_ID", "14050586"))  # Ensure it's an integer
    API_HASH = environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")  # Required, should be kept secret
    BOT_TOKEN = environ.get("BOT_TOKEN", "")  # Required, should be kept secret
    FORCE_SUB = environ.get("FORCE_SUB", "Animes_India_bot")  # Required, should be a string
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB.isdigit() else None  # Convert only if numeric

    # Database config
    DB_URL = environ.get("DB_URL", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")  # MongoDB connection string
    DB_NAME = environ.get("DB_NAME", "KRISHNAEncoderBot")

    # Other Configs
    ADMIN = int(environ.get("ADMIN", "5446367898"))  # Ensure it's an integer
    LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002317509038"))  # Ensure it's an integer
    BOT_UPTIME = time.time()  # Fix the assignment
    START_PIC = environ.get(
        "START_PIC",
        "https://telegra.ph/file/219c7ce28f8f9262c3477-5ac482fb1d0adadca5.jpg"
    )

    # Web response configuration     
    WEBHOOK = environ.get("WEBHOOK", "True").lower() == "true"  # Ensure it's a boolean
    PORT = int(environ.get("PORT", "8080"))  # Ensure it's an integer

    caption = """
🚀 **File Successfully Processed!** 🌟  

📂 **File Name:** `{0}` 📝✨  
📏 **Original Size:** `{1}` 📦📏  
🗜 **Encoded Size:** `{2}` 🔐💾  
📉 **Compression:** `{3}%` 📊🔽  

⏬ **Downloaded in:** `{4}` ⏳📥  
⚙️ **Encoded in:** `{5}` ⚡🎛  
☁️ **Uploaded in:** `{6}` 🚀📤  

🔥 **Your file is compressed, optimized, and ready to go!** 😎✨  
"""
    
