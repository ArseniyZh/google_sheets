from __future__ import print_function

import os.path

import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SAMPLE_RANGE_NAME = 'test_list!A2:D'  # Default range for this task


class GoogleSheet:
    def __init__(self):
        self.SPREADSHEET_ID = '1v4j_nmf7VtC_iWXya14B5QmXDnEP99Z7FNnK49wNJe4'  # ID my own google sheets
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.service = None
        self.creds = None

        if os.path.exists('google_api/token.pickle'):
            with open('google_api/token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'google_api/credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open('google_api/token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('sheets', 'v4', credentials=self.creds)

    def read_data(self, range_=SAMPLE_RANGE_NAME) -> None or list:
        try:
            service = build('sheets', 'v4', credentials=self.creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                        range=range_).execute()
            values = result.get('values', [])

            if not values:
                print('No data found.')
                return

            return values

        except HttpError as err:
            print(err)
