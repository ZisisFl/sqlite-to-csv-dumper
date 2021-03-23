import subprocess
import os

output = subprocess.check_output(['sqlite3', 'superset.db', '.tables'])

list_of_tables = output.split()
list_of_tables = [item.decode('utf-8') for item in list_of_tables]
target_directory = 'dumped_csvs'
os.mkdir(target_directory)

for file in list_of_tables:
    print(file)
    os.system('''sqlite3 -header -csv superset.db "select * from {0};" > {1}/{0}.csv'''.format(file, target_directory))
