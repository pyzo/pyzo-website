"""
Need the boto package. This should be available on py33 via the py3kport
branch, but I get lots of errors. If I solve these, I get connection problems.
So we stick to Python2 for s3upload.

I did have these "broken pipe" and "connection refused by peer" errors
but they disappeared when I added the host argument to S3Connection().

AWS changed some stuff, so new websites need new boto. You can also install
boto in Python3 and use that.

"""

from __future__ import print_function

import os
import sys
import time

import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto.s3.connection import Location


import ssl
if hasattr(ssl, '_create_unverified_context'):
   ssl._create_default_https_context = ssl._create_unverified_context


def find_key():
    key = None
    this_dir = os.path.dirname(os.path.abspath(__file__))
    possible_dirs = ['../.hg', '../.git']
    for pdir in possible_dirs:
        fname = os.path.join(this_dir, pdir, 's3.key')
        if os.path.isfile(fname):
            key = open(fname, 'rb').read().decode('utf-8').strip()
            break
    if key is None:
        raise RuntimeError('Could not find s3 key.')
    return key


# Define keys, secret key should be a secret!
access_key = 'AKIAJU3C3QOCJRMDOGQQ'
secret_key = find_key()

# Make connection
conn = S3Connection(access_key, secret_key, host='s3-eu-west-1.amazonaws.com')

CONTENT_TYPES = {
    '.html': 'text/html',
    '.htm': 'text/html',
    '.css': 'text/css',
    '.js':  'application/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.rst': 'text/plain',
}


def upload_website(bucket_name, dir_name):
    
    # Get bucket (or return existing)
    bucket = conn.get_bucket(bucket_name)
    
    # Store files
    for dirpath, dirnames, filenames in os.walk(dir_name):
        dirpath = os.path.relpath(dirpath, dir_name)
        for fname in filenames:
            if fname.startswith('.'):
                continue
            # Determine filenames
            fname_local = os.path.join(dir_name, dirpath, fname)
            fname_remote = os.path.normpath(os.path.join(dirpath, fname))
            fname_local = os.path.abspath(fname_local)
            
            # Create key
            k = Key(bucket)
            k.key = fname_remote.replace('\\', '/')
            # Set metadata
            content_type = CONTENT_TYPES.get(os.path.splitext(fname)[1].lower(), None)
            if content_type is not None:
                k.set_metadata('Content-Type', content_type)
            # Upload
            cb = FileLoaderProgress(fname_remote)
            count = 0
            while True:
                count += 1
                try:
                    k.set_contents_from_filename(fname_local, cb=cb)
                except Exception as err:
                    print('\n')
                    print(err)
                    if count > 8:
                        print('  WARNING Skipping this file .................')
                        break
                    else:
                        print('   Try again ...')
                else:
                    print()
                    break
                


class FileLoaderProgress:
    def __init__(self, filename_short):
        filename_short = filename_short
        # Init
        self._lasttime = time.time()
        self._text = ''
        self._i = 0
        print("Uploading '%s':" % filename_short)
    
    def __call__(self, i, nmax):
        # Calculate progress
        percent = 100.0 * i / (nmax + 0.1)
        # Calculate speed
        n = i - self._i
        speed = n / (time.time() - self._lasttime + 0.000001)
        self._lasttime = time.time()
        # Print it
        untext = '\b'*len(self._text)
        M = 2**20
        self._text = '%1.2f/%1.2f MB - %1.1f%% (%1.2f MBps)' % (
                                        i/M, nmax/M, percent, speed/M)
        print(untext+self._text, end='')
        # Next round
        self._i = i


POLICY = """{
    "Version": "2008-10-17",
    "Statement": [
        {
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::%s/*"
        }
    ]
}
"""
REDIRECT = """<html>
    <head>
        <meta HTTP-EQUIV="REFRESH" content="0; url=TARGET">
    </head>
    <body>
    Redirecting to <a href='TARGET'>TARGET</a>
    </body>
</html>
"""

def create_html_redirect(url, target):
    """ Create an html redirect for a domain name. 
    You can also use this to initialize a bucket for website use.
    Buckets are created in EU (because that's where we live :) )
    """
    # Create bucket (or return existing)
    try:
        bucket = conn.create_bucket(url, location=Location.EU)
    except boto.exception.S3CreateError:
        bucket = conn.get_bucket(url)
    
    # Turn it into a website
    bucket.configure_website('index.html')
    bucket.set_policy(POLICY % url)
    
    # Create key for index doc
    k = Key(bucket)
    k.key = 'index.html'
    k.set_metadata('Content-Type', 'text/html')
    
    # Upload index.html
    k.set_contents_from_string(REDIRECT.replace('TARGET', target))
    
    # Fix bug in boto
    boto.s3.bucket.S3WebsiteEndpointTranslate.trans_region['EU'] = 's3-website-eu-west-1'
    
    # Get the endpoint
    print('To enable the link of %s, set its CNAME record to:' % url)
    print(bucket.get_website_endpoint())

    
if __name__ == '__main__':
    sys.path.insert(0, '.')
    import conf
    html_dir = os.path.abspath(os.path.join('_build', 'html'))
    bucket_name = conf.bucket_name
    upload_website(bucket_name, html_dir)


