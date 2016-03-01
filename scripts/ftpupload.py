#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from ftplib import FTP
import socket
import time

from conf import ftp_address, ftp_dir

html_dir = os.path.abspath(os.path.join('_build', 'html'))


# Process extensions
extensions = []
if len(sys.argv) > 1:
    extensions = sys.argv[1:]
    extensions = ['.'+e.strip('.*') for e in extensions]


def storeFile(ftp, dir, fname):
    fname_local = os.path.join(html_dir, dir, fname)
    while True:
        try:
            ftp.storbinary('STOR %s' % fname, open(fname_local, 'rb'))
            print('Uploaded %s' % os.path.join(dir, fname))
            break
        except socket.error:
            time.sleep(1.0)
            print('Socket error, waited one second and will now try again ...')
    
    
def storeFilesInDir(ftp, ftproot, dir, recursive=True):
    # Get normalized ftpdir
    ftproot = '/%s/' % ftproot.strip('/')
    ftpdir = ftproot + dir.replace('\\', '/').strip('/')
    
    # Change directory remotely. We normalized so that its an 
    # absolute path
    try:
        ftp.cwd(ftpdir)
    except Exception:
        ftp.mkd(ftpdir)
        ftp.cwd(ftpdir)
    
    # Init
    local_dir = os.path.join(html_dir, dir)
    files = []
    dirs = []
    
    # Collect
    for fname in os.listdir(local_dir):
        fname2 = os.path.join(local_dir, fname)
        if os.path.isdir(fname2) and recursive:
            dirs.append(fname)
        elif os.path.isfile(fname2):
            if extensions and os.path.splitext(fname)[1] not in extensions:
                pass
            else:
                files.append(fname)
    
    # Process files before dirs (otherwise the working dir has changed)
    for fname in files:
        storeFile(ftp, dir, fname)
    for fname in dirs:
        storeFilesInDir(ftp, ftproot, os.path.join(dir, fname))


def find_cred():
    key = None
    this_dir = os.path.dirname(os.path.abspath(__file__))
    possible_dirs = ['../.hg', '../.git']
    for pdir in possible_dirs:
        fname = os.path.join(this_dir, pdir, 'ftp.key')
        if os.path.isfile(fname):
            key = open(fname, 'rb').read().decode('utf-8').strip()
            break
    if key is None:
        raise RuntimeError('Could not find ftp key.')
    return tuple([s.strip() for s in key.split('\n')])


def mangle(s):
    s2 = ''
    for i, c in enumerate(s):
        s2 += chr(ord(c)+i)
    return s2

def unmangle(s):
    s2 = ''
    for i, c in enumerate(s):
        s2 += chr(ord(c)-i)
    return s2


if __name__ == '__main__':
    ftp = FTP(ftp_address) 
    ftp_cred = find_cred()
    ftp.login(*[unmangle(s) for s in ftp_cred])
    storeFilesInDir(ftp, ftp_dir, '')

