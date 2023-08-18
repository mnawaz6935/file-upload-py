import os
import requests

FILE_PATH = r'e:\Dashboard_comlpeted_v1\Dashboard (2).zip'
ENDPOINT_URL = 'https://3.135.156.101:8091/upload_file/'

def upload_with_progress(file_path, url):
    total_size = os.path.getsize(file_path)
    print(f'File Size: {total_size}')
    uploaded_size = 0

    with open(file_path, 'rb') as f:
        with requests.post(url, data=f, stream=True, verify=False) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                uploaded_size += len(chunk)
                percent_complete = (uploaded_size / total_size) * 100
                print(f"Uploading: {percent_complete:.2f}% complete", end='\r', flush=True)

    print("Upload completed.")

if __name__ == "__main__":
    upload_with_progress(FILE_PATH, ENDPOINT_URL)
