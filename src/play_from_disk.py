from argparse import ArgumentParser, Namespace
from config import PlayFromDiskConfig
from configure import get_config
from console import Console, Terminal
import numpy as np
import sounddevice as sd

def main(console: Console, config: PlayFromDiskConfig, filename: str):
    console.print(config)
    console.print("Filename: {} frames per second".format(filename))

    input_device, output_device = get_config()
    sd.default.device = input_device, output_device

    record = np.load(file=filename, allow_pickle=True)
    console.print("Record array size: {}".format(record.size))

    console.print("Start of playback")
    sd.play(record, config.fs)
    sd.wait()
    console.print("End of playback")

def parse_arguments() -> Namespace:
    parser = ArgumentParser(description="Loads and plays a recording from the specified file")
    parser.add_argument("--filename",
                        dest="filename",
                        type=str,
                        default=r".\tmp\sample.npy",
                        help="file name")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    console = Terminal()
    config = PlayFromDiskConfig()
    args = parse_arguments()
    main(console, config, filename=args.filename)
