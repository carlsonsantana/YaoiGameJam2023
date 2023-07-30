from __future__ import print_function

from src.google_meta import GoogleMeta

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
# DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'
DOCUMENT_ID = '1nkhOEwAbUw3FvXb2hpZo-nAnSgTT8B9A_D2Bw5-iBQE'


def main():
    meta = GoogleMeta()
    meta.run_to_local()


if __name__ == '__main__':
    main()
