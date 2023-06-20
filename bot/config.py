import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
payment_token = config_yaml['payment_token']
openai_api_key = config_yaml["openai_api_key"]
use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)
mongodb_uri = f"mongodb://{config_env['MONGODB_USERNAME']}:{config_env['MONGODB_PASSWORD']}@{config_env['MONGODB_HOST']}:" \
              f"{config_env['MONGODB_PORT']}/?authSource=chatgpt_telegram_bot"

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"


INVOICE_LIVE_TIME = 30 * 60

PRICE_LIST = [
    {
        'price_rub': 69,
        'title': "Платеж за 100 вызовов",
        'description': "Вы оплачиваете 100 вызовов нейросети",
        'price_label': '100 вызовов',
        'button_label': '100 вызовов – 69.00 руб',
        'calls_count': 100
    },
    {
        'price_rub': 299,
        'title': "Платеж за 1000 вызовов",
        'description': "Вы оплачиваете 1000 вызовов нейросети",
        'price_label': '1000 вызовов',
        'button_label': '1000 вызовов – 299.00 руб',
        'calls_count': 1000
    },
    {
        'price_rub': 999,
        'title': "Платеж за 4000 вызовов",
        'description': "Вы оплачиваете 4000 вызовов нейросети",
        'price_label': '4000 вызовов',
        'button_label': '4000 вызовов – 999.00 руб',
        'calls_count': 4000
    }
    # 1: 100,
    # 5: 1000,
    # 30: 10000
]
