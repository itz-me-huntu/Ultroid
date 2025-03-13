# Ultroid - UserBot
# Copyright (C) 2021-2025 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=6, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default="BQE4KIoAWs6UbRxYqQp-N59NnNArveuJsUn1iYGh5M7T57Pi-zs-EeuoSWqCl0u_xKATCs_4WS11NFjWMsJQ4VVxfFB-7uaHbPF2MoeME3D2GAzFS9q0vd1L6h0cbi-ApsONiweGMM9_gHZe5M6wMsJ_E1rQjQBnmpsuChZPQtuBH_dctr49gdwuWkaA8BAEYYznN--yUjenLeuA3GPGeEKkBQuXmaelzDSF0ad5AfmiFj5lEy1bv6BHW7-84vYH9StKTo1ZsBE-jliZFi0QHboJ_nz315CA90NOu59GvaF441E9KNJPOgQzoTRuot1RuPVDg2-e0O5syc7LtxGoHVTDmXy2IAAAAAHVsfZvAA")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default="7941143576:AAHCtMhEPO6R_r7XQ4OoHheEHj2YuMBo4bA")
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default="mongodb+srv://jjkbot:jjkbot@botdata.b7rf7.mongodb.net/?retryWrites=true&w=majority&appName=botdata")
