from config import RecThenPlayConfig
from configure import get_config
from console import Console, Terminal
import sounddevice as sd

def main(console: Console, config: RecThenPlayConfig, duration: int=10):
    frames = int(duration * config.fs)

    console.print("Sampling frequency: {} frames per second".format(config.fs))
    console.print("Channels: {}".format(config.channels))
    console.print("Duration: {} seconds".format(duration))
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

if __name__ == '__main__':
    console = Terminal()
    config = RecThenPlayConfig()
    main(console, config)
