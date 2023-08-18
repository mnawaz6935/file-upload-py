import os
import requests

FILE_PATH = r'e:\Dashboard_comlpeted_v1\Dashboard (2).zip'
ENDPOINT_URL = 'https://3.135.156.101:8091/upload_file/'

def upload_with_progress(file_path, url):
    total_size = os.path.getsize(file_path)
    print(f'File Size: {total_size}')
    uploaded_size = 0
    headers = {'Content-Type': 'multipart/form-data'}
    with open(file_path, 'rb', encoding='utf-8') as f:
        with requests.post(url, data=f, headers=headers, stream=True, verify=False) as response:
            try:
                response.raise_for_status()
                for chunk in response.iter_content(chunk_size=8192):
                    uploaded_size += len(chunk)
                    percent_complete = (uploaded_size / total_size) * 100
                    print(f"Uploading: {percent_complete:.2f}% complete", end='\r', flush=True)

                print("Upload completed.")
            except requests.exceptions.HTTPError as e:
                print("Upload failed. HTTP Error:")
                print(e)
                print(response.text)
    print("Upload completed.")

if __name__ == "__main__":
    upload_with_progress(FILE_PATH, ENDPOINT_URL)
