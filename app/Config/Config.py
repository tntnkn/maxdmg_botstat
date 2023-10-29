from dotenv import load_dotenv
import os 

class Config():
    def __init__(self):
        load_dotenv()

        self.API_TOKEN      = os.getenv('API_TOKEN')
        self.ALLOWED_TG_IDS = { int(i) for i in 
                                os.getenv('ALLOWED_TG_IDS').split(",") }

        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASS = os.getenv('DB_PASS')

