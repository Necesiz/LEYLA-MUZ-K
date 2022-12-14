from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgB0-_NdUZX9F8r0fDpxM8IknD-cxQTTU6BYTkNS5Lw42dxa4pTCuPlrG-kU6yBwwcUTGl8Z1Ejc5HXiOo9H-_jNsmxhz_SyvIOLplNdZGi7aI0ZkOcP4rp-yMUtMBYL9l9IOCA54_nSrhpPwdG6672fnn5TlhZMibVh79qXRS5VpcycHIOSa-87ckXql_LVZKhGh0w_wDeppRSYYcewgUrMUlilT6AJ4jvBbppb_s0Uz2N1pxXSFtWa6GYUhl7oUuu3ahfRxdb9Iboh_prlD0s637sJTBdYbP61t8NogvWjlWdCNk4RzIuH7ts7ox5mNXvCI0zwYkY_gWh5bQR-xMDmAAAAAT8q85oA")
BOT_TOKEN = getenv("BOT_TOKEN", "5842321851:AAF4iPzvy8uI8oz7mj2T8YSTxSHJ8z6SAhc")
BOT_NAME = getenv("BOT_NAME", "LEYLA") 
API_ID = int(getenv("API_ID", "17568815"))
API_HASH = getenv("API_HASH", "177622d39f23e7c3d015f3d6ebaacd31")
BOT_USERNAME = getenv("BOT_USERNAME", "leylamusiciBot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5508658149").split()))
