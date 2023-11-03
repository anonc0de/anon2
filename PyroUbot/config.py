import os

DEVS = [
    id
]

API_ID = int(os.getenv("API_ID", "24623085"))

API_HASH = os.getenv("API_HASH", "75ce0c6125ae201c9e3d5a825c667a91")

BOT_TOKEN = os.getenv("BOT_TOKEN", "bot token")

OWNER_ID = int(os.getenv("OWNER_ID", "id"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001538826310 -1001462256506 -1001812143750").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "10"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongoddb",
)

