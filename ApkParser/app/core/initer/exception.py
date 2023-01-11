class SystemHealthPostgresqlConnectionException(Exception):
    def __init__(self) -> None:
        self.msg = "Postgresql Failed connection"

    def __str__(self) -> str:
        return "{}".format(self.msg)


class SystemHealthRedisConnectionException(Exception):
    def __init__(self) -> None:
        self.msg = "Redis failed connection"

    def __str__(self) -> str:
        return "{}".format(self.msg)
