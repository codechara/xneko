import os

class Properties(dict):
    class Dot:
        CONFIG = {
            "server": "localhost:443",
            "server_ssl": "1"
        }

    def __init__(self, path):
        self.path = path

    def overwrite(self, new: dict):
        self.update(new)

        return self

    def write(self):
        with open(self.path, encoding="utf-8", mode="w") as f:
            for key in self:
                f.write("%s=%s\n" % (key, self[key]))

        return self

    def read(self):
        if os.path.exists(self.path):
            with open(self.path, encoding="utf-8", mode="r") as f:
                for line in f.read().split("\n"):
                    if line:
                        splited = line.split("=", 1)
                        self[splited[0]] = splited[1]

        self.write()

        return self