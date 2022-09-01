import plugins


class PluginA(plugins.Base):

    def __init__(self):
        pass

    def print(self, command):
        print(">> TEST PLUGIN PRINTING")
        print(command)