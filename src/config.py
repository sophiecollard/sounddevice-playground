class PlayFromDiskConfig:

    def __init__(self, fs: int=44100) -> None:
        self.fs = fs # frames per second

class RecThenPlayConfig:
    
    def __init__(self, fs: int=44100, channels: int=2) -> None:
        self.fs = fs # frames per second
        self.channels = channels

class RecToDiskConfig:

    def __init__(self, fs: int=44100, channels: int=2) -> None:
        self.fs = fs # frames per second
        self.channels = channels
