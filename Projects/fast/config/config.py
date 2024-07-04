from src.utils.azure.secret_client import AzureSecretsClient
from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    NODE_ENV: str = os.getenv('NODE_ENV')
    APM_SERVER_URL: str = os.getenv('APM_SERVER_URL')
