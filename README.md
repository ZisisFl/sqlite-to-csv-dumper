## SQLite database to csv dumper ##
This is a simple Python script that takes as input a sqlite db file and an output path. For each table in the database it produces a csv file in output path directory.
Only native Python libraries are being used.

In this project you can find a sample .db file taken from [here](https://www.sqlitetutorial.net/sqlite-sample-database/).


### Usage example ###
```sh
python sqlite_dumper.py --input chinook.db --output output_files 
```
