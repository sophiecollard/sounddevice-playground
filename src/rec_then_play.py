from argparse import ArgumentParser, Namespace
from config import RecThenPlayConfig
from configure import get_config
from console import Console, Terminal
import sounddevice as sd

def main(console: Console, config: RecThenPlayConfig, duration: int):
    console.print(config)
    console.print("Duration: {} seconds".format(duration))

    frames = int(duration * config.fs)
    console.print("Number of frames: {}".format(frames))
    console.print("Recording array size: {}".format(frames * config.channels))

    input_device, output_device = get_config()
    sd.default.device = input_device, output_device
    
    console.print("Start of recording")
    record = sd.rec(frames, samplerate=config.fs, channels=config.channels)
    sd.wait()
    console.print("End of recording")

    console.print("Start of playback")
    sd.play(record, config.fs)
    sd.wait()
    console.print("End of playback")

def parse_arguments() -> Namespace:
    parser = ArgumentParser(description="Records a sample of the specified duration then plays it back")
    parser.add_argument("--duration",
                        dest="duration",
                        type=int,
                        default=10,
                        help="recoding duration in seconds")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    console = Terminal()
    config = RecThenPlayConfig()
    args = parse_arguments()
    main(console, config, duration=args.duration)
