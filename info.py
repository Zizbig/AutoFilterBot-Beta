import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Auto_Filters_Bot')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
PORT = int(environ.get('PORT', '8080'))

# Bot pics and stickers
STICKERS = (environ.get('STICKERS', 'CAACAgIAAxkBAAEGm9hjhf69CtQmXoeQ2HidYCGBFeZ4gAACxgEAAhZCawpKI9T0ydt5RysE CAACAgIAAxkBAAEGm9pjhf7I9jCDh3PpkocMNFcPJfisvwAC0wADVp29CvUyj5fVEvk9KwQ CAACAgIAAxkBAAEGm9xjhf7SH4Yc8EP5yI4e8BTH968ClwACGAADDbbSGX671giQDJU8KwQ')).split()
PICS = (environ.get('PICS', 'https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg')).split()

# Bot Admins
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '').split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if id_pattern.search(index_channels) else index_channels for index_channels in environ.get('INDEX_CHANNELS', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/APDBugSupport')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/APDBug')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "False"), True)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "✅ I Found: <code>{query}</code>\n\nTitle: <a href={url}>{title}</a>\nGenres: {genres}\nRating: <a href={url}/ratings>{rating} / 10</a>\n\nRequested by: {message.from_user.mention}\nPowered by: <b>{message.chat.title}</b>")
FILE_CAPTION = environ.get("FILE_CAPTION", "File Name :- {file_name}\n\n```Caption :-\n{file_caption}```\n\nPowered By: @APDBug")
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
WELCOME_TEXT = environ.get("WELCOME_TEXT", "Hello {mention}, Welcome to {title} Group!")
TUTORIAL = environ.get("TUTORIAL", "https://t.me/APDBug")
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]

# stream features vars
"""Deploy this repo: https://github.com/adarsh-goel/filestreambot"""
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "0"))
URL = environ.get("URL", "https://dl.apdlink.workers.dev")
                           
