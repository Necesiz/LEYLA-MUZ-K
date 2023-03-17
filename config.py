from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AgAj0wFPavV5LhgeeK2gu7LiX3bLApjj9Oq42JAQOUodAtPgR_o0DXbd0RPKm0Jsxz5sw49B3hupQyS4OfFwbzbff_BLQb7gEEywlosiHsVELhYnbmhgXIA8QdvwP6lg_QUqx4Eflowz6fxSwpeDKMNCpxNIDXSkgeNr2owRlLJaeGDbyLZFB26_QZEgIus2wkYg6sYayCqzrzYSPegLEybUuilod_6qbaS8D9dXDWVzWRAmM-2PNfQcmqB3kSOqCgDzLI6Y1pRH37VpwAFp2SbiOTX1Jm_E5Mo0CuSbPRQnTMtM5rmvOqSsGeqVg0lZCJajFCCZve_C7CM6umBjfo6FAAAAAUhXc-UA")
BOT_TOKEN = getenv("BOT_TOKEN", "5681957815:AAFu8TdIl9pYlQjSzm2r8rDL1TQqjxGyzGg")
BOT_NAME = getenv("BOT_NAME", "AzeSongRobot") 
API_ID = int(getenv("API_ID", "15954332"))
API_HASH = getenv("API_HASH", "85adea6f1eaf068b707703b4846a9ced")
BOT_USERNAME = getenv("BOT_USERNAME", "AzeSongRobot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5134595693").split()))
