# googledriveops

Google Drive API operations with Python

#### Core Libraries
- https://github.com/googleapis/google-api-python-client (google drive apis interface)
- https://github.com/googleapis/oauth2client (oauth2 interface)

#### Setup
Dependencies:
```
source venv/bin/activate

pip install google-api-python-client
pip install oauth2client
```
Secrets:

Add file `drive_secrets.sjon` in `src` directory with your user's OAuth secrets.

#### Scripts

- `simplereport.py`: Generates a report (`src/simple_report.json`) that shows number of files and folders for source folder.
- `recursivereport.py`: Generates a report (`src/recursive_report.json`) that recursively calculates each nested folder's file count.

#### Code Organization

- `gdriveclient.py`: Main service with common functionality for scripts.
- `config.py`: Configuration interface for static json config (`config.json`).
- `logger.py`: Generates centralized logging to `src/logs.log` with configurable console output.