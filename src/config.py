class PlayFromDiskConfig:

    def __init__(self, fs: int=44100) -> None:
        self.fs = fs # frames per second

    def __str__(self) -> str:
        s = "Sampling frequency: {} frames per second".format(self.fs)
        return s

class RecThenPlayConfig:
    
    def __init__(self, fs: int=44100, channels: int=2) -> None:
        self.fs = fs # frames per second
        self.channels = channels

    def __str__(self):
        lines = [
            "Sampling frequency: {} frames per second".format(self.fs),
            "Channels: {}".format(self.channels)
        ]
        s = "\n".join(lines)
        return s

class RecToDiskConfig:

    def __init__(self, fs: int=44100, channels: int=2) -> None:
        self.fs = fs # frames per second
        self.channels = channels

    def __str__(self):
        lines = [
            "Sampling frequency: {} frames per second".format(self.fs),
            "Channels: {}".format(self.channels)
        ]
        s = "\n".join(lines)
        return s
