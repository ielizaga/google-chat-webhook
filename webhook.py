from json import dumps
from httplib2 import Http
import os

def main():
    """Google Chat incoming webhook."""

    space_id = os.getenv("SPACEID")
    api_key = os.getenv("APIKEY")
    api_token = os.getenv("APITOKEN")

    url = f"https://chat.googleapis.com/v1/spaces/{space_id}/messages?key={api_key}&token={api_token}"
    app_message = {"text": "Hello Ignacio!"}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)


if __name__ == "__main__":
    main()