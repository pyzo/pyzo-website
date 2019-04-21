"""
Script to deploy this site on my server.
"""

import os
import io
import zipfile

import requests

import makesite


def deploy():
    f = io.BytesIO()
    with zipfile.ZipFile(f, "w") as zf:
        for fname, blob in makesite.create_assets().items():
            zf.writestr(fname, blob)

    UPDATE_ACCESS_TOKEN = os.getenv("UPDATE_ACCESS_TOKEN_SITE")

    url = f"https://pyzo.org/site-update/?token={UPDATE_ACCESS_TOKEN}"
    # url = f'http://localhost/site-update/?token={UPDATE_ACCESS_TOKEN}&domain=xx.pyzo.org'
    r = requests.post(url, data=f.getvalue())
    if r.status_code != 200:
        raise RuntimeError("Publish failed: " + r.text)
    else:
        print("Publish succeeded, " + r.text)


if __name__ == "__main__":
    deploy()
