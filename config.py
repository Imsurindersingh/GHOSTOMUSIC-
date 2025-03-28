from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("f182fe949bf71f0ed098e14d28c1ce28", None)                # get from my.telegram.org
    API_ID = int(getenv("28260914", 0))                  # get from my.telegram.org
    BOT_TOKEN = getenv("7770806448:AAFOduyOZC1hBgYzOrswGELR9VScCTc9_nY", None)              # get from @BotFather
    DATABASE_URL = getenv("mongodb+srv://GHOSTOMUSIC:CiyvvxoYAS01Pezm@ghosto-omusic.rniqbaf.mongodb.net/GHOSTO_DB?retryWrites=true&w=majority&appName=GHOSTO-OMUSIC", None)        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("BQGvOjIAvwfqNSJ9cuPAE-kIMlgaPDj7Iax9lcsPfIZTnQn1ATIUv8hdt5AKO5GbG1WeGw24pncK5JLKphB67hXDmd_sDsO6O94Et07xFdh8esc3TbkevPNkjRrLv4YoA5N7IIWNPsXOHUtG79g7SyVDoXYWOhZ9O9gnPXo0VkfZYhLSxzTVCPumQu_XSfkA5qdZwZh9P8AGWAL58HYSa32_WmApMefhMUMFSemHMuiMhnpLWzA4MQ19xATKEY4dt1Teh-HYi3cdAy41hIy5La3RjYSMf2YFUdB9-KCOjAeiHlzlq7Sw4us03qkCxd2FEo_mdDYVufzvKyZBaHgVHzNnxWlLqQAAAAHPLRiwAQ", None)  # enter your session string here
    LOGGER_ID = int(getenv("-1002566517734", 0))            # make a channel and get its ID
    OWNER_ID = getenv("7703788539", "")  # enter your id here
    GROUP ID = int(getenv("-1002592634422", 0))  #enter you group logger id
    
    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://telegra.ph/file/2c546060b20dfd7c1ff2d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "\x40\x4d\x75\x73\x69\x63\x5f\x48\x65\x6c\x6c\x42\x6f\x74")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://graph.org/file/4d1467439269f27634331-1ac15481f1992f853d.jpg")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
