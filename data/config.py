from environs import Env

"""
Get personal data from .env
"""

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")  # TelegramBot token from @BotFather - str
chat_id = env.int("chat_id")  # Admin chat ID - int
group_id = env.int("group_id")  # Group chat ID, not necessary but in my case it was needed - int
ip = env.str("IP")  # IP address. In future case should be list type - str
login = env.str("login")  # Telegram login for reminder and push notification - str
log_path = env.str("log_path")  # Path to .log file - str
