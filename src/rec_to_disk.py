from argparse import ArgumentParser, Namespace
from config import RecToDiskConfig
from configure import get_config
from console import Console, Terminal
import numpy as np
import os
import sounddevice as sd

def main(console: Console, config: RecToDiskConfig, duration: int, filename: str):
    frames = int(duration * config.fs)

    console.print("Sampling frequency: {} frames per second".format(config.fs))
    console.print("Channels: {}".format(config.channels))
    console.print("Duration: {} seconds".format(duration))
    console.print("Number of frames: {}".format(frames))
    console.print("Recording array size: {}".format(frames * config.channels))
    console.print("Filename: {} frames per second".format(filename))

    input_device, output_device = get_config()
    sd.default.device = input_device, output_device
    
    console.print("Start of recording")
    record = sd.rec(frames, samplerate=config.fs, channels=config.channels)
    sd.wait()
    console.print("End of recording")

    if not os.path.exists(filename):
        open(filename, "w").close()

    np.save(file=filename, arr=record)

def parse_arguments() -> Namespace:
    parser = ArgumentParser(description="Records a sample of the specified duration and saves it to the specified file")
    parser.add_argument("--duration",
                        dest="duration",
                        type=int,
                        default=10,
                        help="recoding duration in seconds")
    parser.add_argument("--filename",
                        dest="filename",
                        type=str,
                        default=r".\tmp\sample.npy",
                        help="file name")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    console = Terminal()
    config = RecToDiskConfig()
    args = parse_arguments()
    main(console, config, duration=args.duration, filename=args.filename)
