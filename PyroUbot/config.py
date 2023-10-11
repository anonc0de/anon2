import os

DEVS = [
    1054295664,
    6629259024,
]

API_ID = int(os.getenv("API_ID", "12183627"))

API_HASH = os.getenv("API_HASH", "6a0cc8885587adddebae612b440d5018")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6590270131:AAEMI3qFnkYYXJWESCwm_VB395QsR8dLkGc")

OWNER_ID = int(os.getenv("OWNER_ID", "6629259024"))

USER_ID = list(map(int,os.getenv("USER_ID", "6629259024 722852368 6055603026 1329936747",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001538826310"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001538826310 -1001462256506").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://dinexa1064:0212@cluster0.ep5evwf.mongodb.net/?retryWrites=true&w=majority",
)

#mongodb+srv://dinexa1064:0212@cluster0.ep5evwf.mongodb.net/?retryWrites=true&w=majority

#mongodb+srv://ilxnvuj833:0212@cluster0.ile0pdo.mongodb.net/?retryWrites=true&w=majority

#mongodb+srv://odos1:odos1@odos.rdrfcsf.mongodb.net/?retryWrites=true&w=majority
