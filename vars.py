#𓆰MANISH 𓆪
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22480303"))
API_HASH = environ.get("API_HASH", "99c931b6c1ae6f8c3c3e87da173fa424")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7518770522"))
CREDIT = "𓆰MANISH𓆪"
AUTH_USER = os.environ.get('AUTH_USERS', '7167916864,7968584207,7836790905').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
