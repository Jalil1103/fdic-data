import os
import urllib.request
from bs4 import BeautifulSoup as bs
import requests, zipfile, io

# # dir for zipped data
try:
    os.mkdir('./fdic-data')
except:
    pass

# Fdic link
url = 'https://www7.fdic.gov/idasp/advSearch_warp_download_all.asp?intTab=2'
sdi_url = 'https://www7.fdic.gov/sdi/download_large_list_outside.asp'

# data collection
page = urllib.request.urlopen(url)
soup = bs(page)

# html marker for fdic page
table = soup.find(id='divSODDownload')
# removing excess links that are in the table
# [x for x in table.find_all('a') if 'ALL_' in x.text]
# you can prolly find a cleaner way of doing this
links_array = []
file_name = []
for tag in table.find_all('a'):
    if 'ALL_' in tag.text:
        links_array.append(tag.get('href'))
        file_name.append(tag.text)


# parse links and download zipped files
def download_urls(zip_url, path):
    request_response = requests.get(zip_url)
    zip_file = zipfile.ZipFile(io.BytesIO(request_response.content))
    zip_file.extractall(path)


# loop through and save files:
for link in links_array:
    for name in file_name:
        n = name.replace('.ZIP', '')
        path = './fdic-data/' + name
        os.mkdir(path)
        download_urls(link, path)
