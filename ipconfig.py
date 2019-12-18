import socket
import subprocess
import os
from requests import get, post
from pathlib import Path

def get_external_ip():
    return get('https://api.ipify.org').text
    
def get_internal_ip():
    return subprocess.check_output("hostname -I", shell=True).decode('utf-8').split()[0]

def add_file_to_torrent(file_name):
    post('url', data={
        'internal_ip':get_internal_ip(),
        'file_path':str(Path.home()) + '/torrent-files',
        'file_name':file_name
    })

def send_user_information():
    post('url', data={
        'internal_ip':get_internal_ip(),
        'external_ip':get_external_ip(),
    })
