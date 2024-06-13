import os
import json
import socket
import datetime

import asgineer

from makesite import create_assets


stats_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_stats(request, status_code=None, rtime=None, is_page=None):
    """ Send request stats over UPD to a stats server. """
    p = request.path
    stats = {"group": os.getenv("MYPAAS_SERVICE", "")}
    stats["requests|count"] = 1
    stats["path|cat"] = f"{status_code} - {p}" if (status_code and p) else p
    if rtime is not None:
        stats["rtime|num|s"] = float(rtime)
    if is_page:  # anomimously register page view, visitors, language, and more
        stats["pageview"] = request.headers
    try:
        stats_socket.sendto(json.dumps(stats).encode(), ("stats", 8125))
    except Exception:
        pass


asset_handler = asgineer.utils.make_asset_handler(create_assets())

redirects = {
    "www.pyzo.org": "https://pyzo.org",
    "community.pyzo.org": "https://github.com/pyzo/pyzo/discussions",
    "repo.pyzo.org": "https://github.com/pyzo/pyzo",
    "issues.pyzo.org": "https://github.com/pyzo/pyzo/issues",
    "guide.pyzo.org": "https://pyzo.org/guide.html",
    "miniconda.pyzo.org": "https://conda.io/miniconda.html",
    "matlab.pyzo.org": "https://numpy.org/doc/stable/user/numpy-for-matlab-users.html",
}


@asgineer.to_asgi
async def main_handler(request):

    if request.host in redirects:
        url = redirects[request.host]
        return 307, {"Location": url }, b""

    path = request.path.lstrip("/")

    response = await asset_handler(request, path or "index.html")
    response = asgineer.utils.normalize_response(response)

    is_page = "." not in path or path.endswith(".html")
    send_stats(request, response[0], is_page=is_page)

    return response


if __name__ == "__main__":
    asgineer.run(main_handler, "uvicorn", "0.0.0.0:80", log_level="warning")
