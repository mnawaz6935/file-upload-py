import os
import requests
from tqdm import tqdm
from pathlib import Path

FILE_PATH = r'e:\Dashboard_comlpeted_v1\Dashboard (2).zip'
ENDPOINT_URL = 'https://3.135.156.101:8091/upload_file/'

def upload_with_progress(file_path, url):
    print(f'Files Exists: {os.path.exists(file_path)}')
    total_size = os.path.getsize(file_path)
    print(f'File Size: {total_size}')
    # Get the file size for progress tracking
    file_size = Path(file_path).stat().st_size

    with open(file_path, 'rb') as file:
        files = {
            'file': (file_path, file),
            'FileName': (None, 'dashboard.zip')
        }

        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            def update_progress(bytes_amount):
                pbar.update(bytes_amount - pbar.n)

            response2 = requests.post(url, files=files, verify=False, hooks={'response': update_progress})

            if response2.status_code == 200:
                print('File uploaded successfully')
    print("Upload completed.")

if __name__ == "__main__":
    upload_with_progress(FILE_PATH, ENDPOINT_URL)
