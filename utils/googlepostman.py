class GooglePostman:
    def __init__(self):
        self.scopes = ['https://mail.google.com/']
        self.service = self.gmail_authenticate()

    def gmail_authenticate(self):

        import os
        import pickle
        # Gmail API utils
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request

        creds = None
        # the file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time
        if os.path.exists("token.pickle"):
            with open("token.pickle", "rb") as token:
                creds = pickle.load(token)
        # if there are no (valid) credentials availablle, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.scopes)
                creds = flow.run_local_server(port=0)
            # save the credentials for the next run
            with open("token.pickle", "wb") as token:
                pickle.dump(creds, token)

        return build('gmail', 'v1', credentials=creds)

    def search_messages(self, service, query):
        result = self.service.users().messages().list(userId='me',q=query).execute()
        messages = [ ]
        if 'messages' in result:
            messages.extend(result['messages'])
        while 'nextPageToken' in result:
            page_token = result['nextPageToken']
            result = self.service.users().messages().list(userId='me',q=query, pageToken=page_token).execute()
            if 'messages' in result:
                messages.extend(result['messages'])
        return messages
    
    def delete_messages(self, query):
        messages_to_delete = self.search_messages(self.service, query)
        print(f"Deleting {len(messages_to_delete)} emails.")
        # it's possible to delete a single message with the delete API, like this:
        # service.users().messages().delete(userId='me', id=msg['id'])
        # but it's also possible to delete all the selected messages with one query, batchDelete
        return self.service.users().messages().batchDelete(
        userId='me',
        body={
            'ids': [ msg['id'] for msg in messages_to_delete]
        }
        ).execute()
    
        