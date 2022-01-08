import os
from configparser import ConfigParser

import yaml

ROOT_DIR = os.path.dirname(__file__)
print(ROOT_DIR)
INPUT_DIR = os.path.join(ROOT_DIR, "STATIC", "INPUT")
OUTPUT_DIR = os.path.join(ROOT_DIR, "STATIC", "OUTPUT")
LOG_DIR = os.path.join(ROOT_DIR, "LOG")
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

LOG_CONFIG_PATH = os.path.join(ROOT_DIR, "config", "logging.ini")

ENVIRONMENT = os.getenv("ENVIROMENT", "dev")
# iniファイルの読み込み
parser = ConfigParser()
ini_file_path = os.path.join(
    os.path.join(ROOT_DIR, "config", f"config_{ENVIRONMENT}.ini")
)

if os.path.isfile(ini_file_path):
    parser.read(ini_file_path)
else:
    raise FileNotFoundError(f"iniファイルが存在しません : {ini_file_path}")
# yamlファイルの読み込み
yaml_file_path = os.path.join(ROOT_DIR, "config", f"config_{ENVIRONMENT}.yaml")
if os.path.isfile(yaml_file_path):
    with open(yaml_file_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
else:
    raise FileNotFoundError(f"yamlファイルが存在しません : {yaml_file_path}")
