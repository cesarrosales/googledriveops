from logger import script_log_info
from gdriveclient import get_directory_and_file_totals
from config import c_source_folder
import json

script_log_info('getting simple report totals...')

sourceFolder = c_source_folder()
reportTotals = get_directory_and_file_totals(sourceFolder)

with open('src/simple_report.json', 'w') as fp:
    json.dump({
        'folderId': sourceFolder,
        'report': reportTotals
    }, fp)

script_log_info('process complete.')