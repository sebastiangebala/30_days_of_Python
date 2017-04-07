import os
def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path %s"%(file_path))
    return file_path
    
def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()