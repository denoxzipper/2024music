import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27763635
API_HASH = "61481dcdf095e69da95e9ca70869d9f0"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7797728151:AAFKrIeCTZ3RSsOtL-3fSSS56IZtQY-S1Dc"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://n4nd404:n4nd404@cluster0.5uq5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1001774290021

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7478639332

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/n4vpn2"
SUPPORT_GROUP = "https://t.me/t3amn4chat"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "AQGno7MAP6Rg8wQGlg9LZqqHRB4QM7foYXntNQi7k_EOv3vjbM2nNyMLgmTF7pZN8Trxl4D0j7isB6kgXj3J30aYLg1AqThuQVlOoMsDWcs8TwpupzMkqSzrbN8-A7zVfgS8vPq96RZ0iYmSmPauzBsMUPfV8CYYxeg4gNNafIaAfqti_5e5rRLUtxulQqXN-H9uRdfcjJceUV9rCWZFdSd4C0MQF9bwmLUygH1W7ISGelfX2FG5VSzCZXN6dO9dgVvCmRZrY559BfepPVebEWOKtp8ueI_fztRvZuGmqiwZhEEuifGfwcSh9whMIn8aUO1W15phZ1RS_Sq9mcCuSLhaj7wangAAAAFx0ewhAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://telegra.ph/file/c23fb291c62260773cb2a-796476f1e0ebd93213.jpg"

PING_IMG_URL = "https://telegra.ph/file/820dbca6d14c8e3a6114a-56af5d8006c5a0c702.jpg"

PLAYLIST_IMG_URL = "https://telegra.ph/file/e75dc3ecb5d4660c91537-2fdd3ea9ef37e1bbe0.jpg"
STATS_IMG_URL = "https://telegra.ph/file/60743dfdf68b5c664dd22-e96770bcdd3aa37331.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/c818e0630a4f9b5e80d87-a8c8aa804ff7628f10.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/3240afeb71ec150c2a90b-f3b82507b093e50ac6.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/224a58028d4f1a73103f0-4be78df495c4907dff.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/224a58028d4f1a73103f0-4be78df495c4907dff.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
