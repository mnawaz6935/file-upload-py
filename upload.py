import os
import requests
from tqdm import tqdm
from pathlib import Path

FILE_PATH = r'e:\Dashboard_comlpeted_v1\Dashboard\dashboard.zip'
ENDPOINT_URL = 'https://3.135.156.101:8091/upload_file/'

def upload_with_progress(file_path, url):
    print(f'Files Exists: {os.path.exists(file_path)}')
    total_size = os.path.getsize(file_path)
    print(f'File Size: {total_size}')
    # Get the file size for progress tracking
    file_size = Path(file_path).stat().st_size

    url2 = url
    filename = file_path
    with open(filename, 'rb') as file:
        files = {
            'file': (filename, file),
            'FileName': (None, 'dashboard.zip')
        }
        response2 = requests.post(url2, files=files, verify=False)

        if response2.status_code == 200:
            print('File uploaded successfully')
            update_cookies_request()
        else:
            print('File upload failed')
    print("Upload completed.")

if __name__ == "__main__":
    upload_with_progress(FILE_PATH, ENDPOINT_URL)
