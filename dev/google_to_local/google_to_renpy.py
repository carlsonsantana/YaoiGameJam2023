from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.google_meta import GoogleMeta

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
# DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'
DOCUMENT_ID = '1nkhOEwAbUw3FvXb2hpZo-nAnSgTT8B9A_D2Bw5-iBQE'


def main():
    meta = GoogleMeta()
    meta.run()


if __name__ == '__main__':
    main()
