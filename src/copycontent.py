from logger import script_log_info
from gdriveclient import copyfolder
from config import c_source_folder, c_destination_folder
import json

script_log_info('starting folder copy operation...')

sourceFolder = c_source_folder()
destinationFolder = c_destination_folder()

reportTotals = copyfolder(sourceFolder, destinationFolder)

script_log_info('process complete.')