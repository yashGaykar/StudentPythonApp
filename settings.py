from dotenv import load_dotenv
import os

dotenv_path = '.env'
load_dotenv(dotenv_path)

JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY")
NODE_APP=os.environ.get("NODE_APP")
