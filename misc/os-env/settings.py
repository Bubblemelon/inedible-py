#database configuration settings

database = dict(
    DATABASE = "mysql",
    USER     = "root",
    PASS     = "jam"
)

# loads from .env
from os.path import join, dirname, abspath
from dotenv import load_dotenv

# if .env is one level up from current dir
# dotenv_path = abspath(join(dirname(__file__), '..' ,'.env'))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)