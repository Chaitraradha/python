import requests
import tarfile

sourceurl="https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.18/bin/apache-tomcat-10.1.18.tar.gz"
file_path="/home/ubuntu/tomcat.tar"

def download_file(url,file_path):
    try:
        response=requests.get(url)
        with open(file_path, 'wb') as fh:
            fh.write(response.content)
            print("file downloaded successfully")
        with tarfile.open(file_path, 'r') as fa:
            fa.extractall("/home/ubuntu/")
            print("tar file extracted successfully")
    except requests.exceptions.RequestException as e:
        print(f"failed to download the tar file")

download_file(sourceurl, file_path)
