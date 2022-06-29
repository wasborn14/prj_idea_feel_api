from .base import *
from decouple import config
from pathlib import Path
from dj_database_url import parse as dburl

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

ALLOWED_HOSTS = []

# アクセス許可
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://idea-project-app.vercel.app"
]

# 本番環境のDatabaseのURLがない時はsqlite3を使用する
# こちらは参考にした設定の記述。
default_dburl = 'sqlite:///' + str(BASE_DIR / "db.sqlite3")

DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}



