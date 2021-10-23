import time
import json

def app(environ, start_response):
    data = {
        "time": time.ctime(time.time()),
        "url": environ["RAW_URI"]
    }
    data = bytes(json.dumps(data), 'utf-8')

    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])