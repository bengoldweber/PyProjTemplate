import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
ENV = os.getenv('ENV', 'production')
ROOT_DIR = os.getenv('ROOT_DIR', os.path.dirname(os.path.abspath("__file__")))
