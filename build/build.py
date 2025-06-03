import PyInstaller.__main__

PyInstaller.__main__.run([
    '../src/main.py',
    '--log-level=DEBUG',
    '--name=QA_DB_CLEANER',
    '--icon=assets/qa_db_cleaner.ico',
    '--clean',
    '--onefile',
    '-w',
    '--uac-admin',
])