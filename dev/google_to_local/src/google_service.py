from __future__ import print_function

import json
import os.path
import os
from os import path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    'https://www.googleapis.com/auth/documents.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

# The ID of a sample document.
# DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'
DOCUMENT_ID = '1nkhOEwAbUw3FvXb2hpZo-nAnSgTT8B9A_D2Bw5-iBQE'

class GoogleService:
    def __init__(self):
        """Shows basic usage of the Docs API.
        Prints the title of a sample document.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            print("Token found")
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("Refreshing token")
                creds.refresh(Request())
            else:
                print("Installing new token")
                flow = InstalledAppFlow.from_client_secrets_file(
                    'secrets/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            self.service = build('docs', 'v1', credentials=creds)
        except HttpError as err:
            print(err)

    def obtain_document(self, document_id):
        try:
            # Retrieve the documents contents from the Docs service.
            document = self.service.documents().get(documentId=document_id).execute()

            # print('The title of the document is: {}'.format(document.get('title')))
            return document.get('body')
        except HttpError as err:
            print(err)
            return None

    def to_local(self, document_id, destination):
        # todo: HERE

        """Shows basic usage of the Docs API.
        Prints the title of a sample document.
        """
        to_rpy = self.obtain_document(document_id)
        to_rpy = json.dumps(to_rpy)

        # directory existence check
        directory_split = destination.split("/")
        directory_split.pop()  # remove file
        dir_test = ""
        for dir in directory_split:
            dir_test += dir + "/"
            if dir == ".." or dir == ".":
                pass
            elif not path.exists(dir_test):
                os.mkdir(dir_test)
            elif path.exists(dir_test) and path.isfile(dir_test):
                print(f"Error! Treating file as directory: {dir_test}")

        # save
        with open(destination, "w", encoding="utf-8") as file:
            file.write(to_rpy)


if __name__ == '__main__':
    # service = GoogleService()
    # service.to_local()
    pass
