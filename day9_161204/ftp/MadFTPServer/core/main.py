import optparse


class ArgvHandler(object):
    def __init__(self):
        self.parser = optparse.OptionParser()
        (options, args) = self.parser.parse_args()
        self.verify_args(options, args)

    def verify_args(self, options, args):
        """校验并调用相应的功能"""
        if hasattr(self, args[0]):
            func = getattr(self.arg[0])
            func()
        else:
            self.parser.print_help()

    def start(self) -> object:
        print("-------going to start server---")
