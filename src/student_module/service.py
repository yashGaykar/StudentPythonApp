
def validate_file_type(file_type):
    if not (isinstance(file_type, str)):
        raise Exception("File Type must be a String")
    elif file_type not in ['csv','excel']:
        raise Exception("File Type must be csv or excel")

def validate_file_name(file_name):
    if not (isinstance(file_name, str)):
        raise Exception("File Name must be a String")
