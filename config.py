from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgCBtZyrgI0Upp_sCjXbbqLRRS1JPC_CUJNMQrzHS0F4JES0nAph4CuN74HHN-HRkW3VXldfSjdJjS8XZetNvUo1pggNO8QWjkjpWZoY5DdgfrzQnUQRRjv6u3KVeU3wbEn6lZTPXt0AWX9R6sGWyrS6nL_viIjuj99cc0lwiXE45fXMm_S1DcIm5-T2uLmS0cKKqx5OUHgcMj6f3w3AZ23_Y31tmO-gfTFgQwHwipX8JsyWUanfZFEqobQiuzsxF_MLHYH_a3rVoWBamjIupoE3wf_BXOqNzKjUoBETrB6coGT-dsqbtTcymwysEFBMVH7F3OmXuaup8-I0tclaHMhNAAAAAT8q85oA")
BOT_TOKEN = getenv("BOT_TOKEN", "5668475663:AAGgNGCuDr1MMiOg3yHMuz-OlNHyO4XD04A")
BOT_NAME = getenv("BOT_NAME", "LEYLA") 
API_ID = int(getenv("API_ID", "17568815"))
API_HASH = getenv("API_HASH", "177622d39f23e7c3d015f3d6ebaacd31")
BOT_USERNAME = getenv("BOT_USERNAME", "leylamusiciBot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5508658149").split()))
