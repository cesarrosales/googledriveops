from logger import script_log_info
from gdriveclient import get_recursive_totals
from config import c_source_folder
import json

script_log_info('getting recursive report totals...')

sourceFolder = c_source_folder()
reportTotals = get_recursive_totals(sourceFolder)

with open('src/recursive_report.json', 'w') as fp:
    json.dump({
        'totalNestedFolders': len(reportTotals),
        'report': reportTotals
    }, fp)

script_log_info('process complete.')