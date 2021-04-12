from subprocess import check_output
from os import mkdir, system, path
import argparse


def dump_sqlite_tables(sqlite_file, output_directory, verbose=True):
    if path.exists(sqlite_file):
        list_of_tables = check_output(['sqlite3', sqlite_file, '.tables']).split()
        # parse tables names to utf-8
        list_of_tables = [item.decode('utf-8') for item in list_of_tables]

        # if output directory doesn't exist create it
        if not path.exists(output_directory): 
            mkdir(output_directory)

        for table_name in list_of_tables:
            if verbose:
                print(table_name)
            
            system('''sqlite3 -header -csv {2} "select * from {0};" > {1}/{0}.csv'''.format(table_name, output_directory, sqlite_file))
    
    else:
        raise OSError('File {} does not exist'.format(sqlite_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='SQLite to csv parser dumper')

    parser.add_argument('--input', help='Input sqlite file', type=str, required=True)
    parser.add_argument('--output', help='Output directory', type=str, required=True)

    args = parser.parse_args()

    # set parameter values
    input_sqlite_file = args.input
    output_directory = args.output

    dump_sqlite_tables(input_sqlite_file, output_directory)