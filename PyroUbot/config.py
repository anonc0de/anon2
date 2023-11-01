import os

DEVS = list(map(int, os.getenv("DEVS", "6629259024 2066017531").split()))

API_ID = int(os.getenv("API_ID", "24623085"))

API_HASH = os.getenv("API_HASH", "75ce0c6125ae201c9e3d5a825c667a91")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6590270131:AAEMI3qFnkYYXJWESCwm_VB395QsR8dLkGc")

OWNER_ID = int(os.getenv("OWNER_ID", "6629259024"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001462256506"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001538826310 -1001462256506 -1001812143750").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://ohmyshin12:ohmyshin12@cluster0.jboolzn.mongodb.net/?retryWrites=true&w=majority",
)

#mongodb+srv://dinexa1064:0212@cluster0.ep5evwf.mongodb.net/?retryWrites=true&w=majority

#mongodb+srv://ilxnvuj833:0212@cluster0.ile0pdo.mongodb.net/?retryWrites=true&w=majority

#mongodb+srv://odos1:odos1@odos.rdrfcsf.mongodb.net/?retryWrites=true&w=majority
