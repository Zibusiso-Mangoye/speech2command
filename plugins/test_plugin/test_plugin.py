import plugins


class PluginA(plugins.Base):

    def __init__(self):
        pass

    def execute(self, command):
        print(">> TEST PLUGIN PRINTING")
        print(command)