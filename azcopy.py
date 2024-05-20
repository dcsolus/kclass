import os
from dotenv import load_dotenv

load_dotenv()

storage_account_name = os.getenv('STORAGE_ACCOUNT_NAME')
container_name = os.getenv('CONTAINER_NAME')
target_dir = f'https://{storage_account_name}.blob.core.windows.net/{container_name}'

source_dir = os.getcwd()
source_table = os.path.join(source_dir, 'ratings')

cmd_str = f"azcopy copy '{source_table}' '{target_dir}' --recursive"

print('source dir:', source_dir)
print('target_dir:', target_dir)

print('command:', cmd_str)
