# This is a simple command line utility function that will create a text file for each day of the inputted month and year.

import argparse
from datetime import datetime

from create_dates.create_monthly_files import create_monthly_files

parser = argparse.ArgumentParser(description="A command line function to create text files for each day in a given month")
parser.add_argument("--date",type=str,help="A date of the form mm/yyyy")
parser.add_argument("--directory",type=str,help="A filepath to save the files to, must end with /")

if __name__ == "__main__":
    """
    HOW TO RUN:
        Input into your terminal:
            `python cmd_line.py --date mm/yyyy --directory <directory path>/
        This will create the files.
    """
    args = parser.parse_args()
    datetime = args.date
    date_obj = datetime.strptime(datetime,"%m/%Y")
    create_monthly_files(date_obj.month,date_obj.year,args.directory)