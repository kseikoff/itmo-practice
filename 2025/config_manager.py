import yaml


class Config:
    ip: str = ""
    port: int = 0


    @classmethod
    def load(cls, path: str = "config.yaml"):
        with open(path, "r") as file:
            config = yaml.safe_load(file)
            cls.ip = config["connection"]["ip"]
            cls.port = config["connection"]["port"]


    @classmethod
    def save(cls, path: str = "config.yaml"):
        with open(path, "w") as file:
            yaml.safe_dump({
                "connection": {
                    "ip": cls.ip,
                    "port": cls.port
                }
            }, file)


    @classmethod
    def set_config(cls, ip: str, port: int):
        cls.ip = ip
        cls.port = port
