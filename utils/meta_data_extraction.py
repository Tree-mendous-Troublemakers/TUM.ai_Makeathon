
from datetime import datetime
import os

def parse_date_from_filename(filename):
    filename = filename.split("_")
    datetime_string = filename[1]
    return datetime_string

def format_datetime(datetime_str):
    date_obj = datetime.strptime(datetime_str, "%Y%m%d")
    return date_obj.date().isoformat()

def parse_group_from_filename(filename):
    filename = filename.split("_")
    group = filename[0]
    return group

def return_azure_file_path(file_path):
    return file_path.replace('data/','')
