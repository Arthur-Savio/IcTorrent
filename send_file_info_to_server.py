import os
from ipconfig import get_internal_ip
from requests import post


file_path = input('Type the file path: \n')

info = os.stat(file_path)
file_size = info.st_size
url = ''

post('url', data={
    'type':file_path.rsplit('.')[1],
    'size':file_size,
    'path':file_path,
    'user':get_internal_ip()
})