from config import PlayFromDiskConfig
from configure import get_config
from console import Console, Terminal
import numpy as np
import sounddevice as sd

def main(console: Console, config: PlayFromDiskConfig, filename: str):
    console.print("Sampling frequency: {} frames per second".format(config.fs))
    console.print("Filename: {} frames per second".format(filename))

    input_device, output_device = get_config()
    sd.default.device = input_device, output_device

    record = np.load(file=filename, allow_pickle=True)
    console.print("Record array size: {}".format(record.size))

    console.print("Start of playback")
    sd.play(record, config.fs)
    sd.wait()
    console.print("End of playback")

if __name__ == "__main__":
    console = Terminal()
    config = PlayFromDiskConfig()
    main(console, config, filename=r".\tmp\sample.npy")
