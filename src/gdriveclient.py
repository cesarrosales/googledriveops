from config import c_gdrive_scopes, c_source_folder
from httplib2 import Http
from oauth2client import file, client, tools
from googleapiclient.discovery import build
from googleapiclient import discovery
from logger import script_log_info

script_log_info("configuring gdrive client....")

MIME_TYPE_FOLDER = 'application/vnd.google-apps.folder'

credentials = None

gDriveObjectCache = {}

access_token = file.Storage('src/tmp/access_token.json')
credentials = access_token.get()

directoryFiles = {}

if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets('src/gdrive_secrets.json', c_gdrive_scopes())
    credentials = tools.run_flow(flow, access_token)

service = discovery.build('drive', 'v3', http=credentials.authorize(Http()))

def get_directory_and_file_totals(dir):
    script_log_info(f'querying directory and file totals for directory {dir}')
    folderSet = set()
    fileSet = set()
    
    files = get_files_by_query(f"parents = '{dir}'")
    
    for f in files:
        if f['mimeType'] == MIME_TYPE_FOLDER:
            folderSet.add(f['id'])
        else:
            fileSet.add(f['id'])

    script_log_info(f'found {len(folderSet)} folders and {len(fileSet)} files')
    
    return {
        'totalObjects': (len(folderSet) + len(fileSet)),
        'folders': len(folderSet),
        'files': len(fileSet)
    }

def get_recursive_totals(dir):
    reportTotals = {}

    get_directory_and_file_recursive_totals(dir)

    for folder in directoryFiles:
        if folder != dir:
            folderFiles = directoryFiles[folder]
            folderName = gDriveObjectCache[folder]['name']
            reportTotals[folder] = {
                'folderName': folderName,
                'fileCount': len(folderFiles)
            }

            script_log_info(f'Folder id={folder}, name={folderName} has {len(folderFiles)} files')

    return reportTotals

def get_directory_and_file_recursive_totals(dir):
    script_log_info(f'querying directory and file recursive totals for directory {dir}')
    folderSet = set()
    fileSet = set()
    
    files = get_files_by_query(f"parents = '{dir}'")
    
    for f in files:
        folderId = f['id']
        gDriveObjectCache[folderId] = f
        if f['mimeType'] == MIME_TYPE_FOLDER:
            folderSet.add(folderId)
        else:
            fileSet.add(folderId)

    script_log_info(f'found {len(folderSet)} folders and {len(fileSet)} files')

    directoryFiles[dir] = fileSet

    if len(folderSet) > 0:
        for folderId in folderSet:
            get_directory_and_file_recursive_totals(folderId)
    
def get_files_by_query(s):
    response = service.files().list(q=s).execute()
    files = response.get('files')

    nextPageToken = response.get('nextPageToken')

    while nextPageToken:
        response = service.files().list().execute()
        files.extend(response.get('files'))
        nextPageToken = response.get('nextPageToken')
        script_log_info(f'pagination count: {len(files)}')

    return files

