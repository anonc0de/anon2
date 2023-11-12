import os

DEVS = [
    2100442624,
    5312739535,
]

API_ID = int(os.getenv("API_ID", "14687692"))

API_HASH = os.getenv("API_HASH", "01581fe794e8242d7da24efd2bea503c")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6651675667:AAGGW-klkPk2wm9qEx5nb3w76OlgqARf3o0")

OWNER_ID = int(os.getenv("OWNER_ID",  "2100442624"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1001817670395"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001538826310 -1001462256506 -1001812143750 -1002012397923 -1001812143750 -1001964273937 -1002006883687 -1001951721136 -1002045881007 -1001986858575 -1001883961446 -1001974313872").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
)

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://anonuserbot:1234@cluster0.1xdt8lj.mongodb.net/?retryWrites=true&w=majority",
)

