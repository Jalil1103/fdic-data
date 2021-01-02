import os
import urllib.request
from bs4 import BeautifulSoup as bs
import requests, zipfile, io

# # dir for zipped data
try:
    os.mkdir('./fdic-flat-files')
except:
    pass

# download files into local repo
def download_urls(zip_url, path):
    request_response = requests.get(zip_url)
    zip_file = zipfile.ZipFile(io.BytesIO(request_response.content))
    zip_file.extractall(path)

def get_data(count):
    while(count < 2021):
        url = 'https://www7.fdic.gov/sod/ShowFileWithStats1.asp?strFileName=ALL_{count}.zip'.format(count=count)
        path = './fdic-flat-files/{count}'.format(count=count)
        os.mkdir(path)
        download_urls(url, path)
        count += 1
        print(count)
    return


get_data(2015)
