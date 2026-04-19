import os

# Get the directory where the script is running
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Bot Token (use environment variable on server, default for local)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8677144168:AAGL8a0B85LgSvBLci1RiyFHfh5kM7nAWGI")

# Admin Chat ID
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5958336964"))

# UPI Details
UPI_ID = os.environ.get("UPI_ID", "kashif-28@ptyes")

# Website URLs
BASE_URL = "https://dawateislamiindia.org"
BOOKLET_URL = "https://dawateislamiindia.org/weekly-booklet"
PANEL_BASE_URL = "https://panel.dawateislamiindia.org/"

# Database path (relative to script directory)
_db_path = os.environ.get("DB_PATH", "")
DB_PATH = os.path.join(BASE_DIR, _db_path) if _db_path else os.path.join(BASE_DIR, "bot_data.db")

# Data directory for photos etc
_data_dir = os.environ.get("DATA_DIR", "")
DATA_DIR = os.path.join(BASE_DIR, _data_dir) if _data_dir else os.path.join(BASE_DIR, "data")
