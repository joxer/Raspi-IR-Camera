import ConfigParser

class Config:
    def __init__(self,filename):
        self.config = ConfigParser.ConfigParser()
        self.config.read(filename)
        self.dictionary = {}
        for section in self.config.sections():
            options = self.config.options(section)
            for option in options:
                try:
                    self.dictionary[option] = self.config.get(section, option)
                    if self.dictionary[option] == -1:
                        DebugPrint("skip: %s" % option)
                except:
                    print("exception on %s!" % option)
                    dictionary[option] = None
                
    def get_dictionary(self):
        return self.dictionary
