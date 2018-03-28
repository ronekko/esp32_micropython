class FileNotFoundError(Exception):
    def __init__(self, filename):
        message = '"{}" is not found'.format(filename)
        super(FileNotFoundError, self).__init__(message)
