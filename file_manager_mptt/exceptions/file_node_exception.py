
class FileNodeException(Exception):

    def __init__(self, *args):

        self._message = args[0] if args else "File Exception Error"


    def __str__(self):

        return self._message
