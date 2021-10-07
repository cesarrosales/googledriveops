from config import c_gdrive_scopes
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from googleapiclient import discovery
from logger import script_log_info

script_log_info("configuring gdrive client....")

credentials = None

access_token = file.Storage('tmp/access_token.json')
credentials = access_token.get()

if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('gdrive_secrets.json', c_gdrive_scopes())
    credentials = tools.run_flow(flow, access_token)

gdrive = discovery.build('drive', 'v3', http=credentials.authorize(Http()))

def list_files():
    files = gdrive.files().list().execute().get('files', [])
    for f in files:
        print(f['name'], f['mimeType'])