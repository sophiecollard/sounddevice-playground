import configparser
from console import Console, Terminal
import sounddevice as sd

CONFIG_FILENAME = "config.ini"

def get_config(config_filename: str=CONFIG_FILENAME) -> tuple[int, int]:
    config = configparser.ConfigParser()
    config.read(config_filename)
    # TODO Handle ValueError
    input_device = int(config["AudioIO"]["input_device"])
    output_device = int(config["AudioIO"]["output_device"])
    return (input_device, output_device)

def set_config(console: Console, config_filename: str=CONFIG_FILENAME) -> None:
    devices = sd.query_devices()
    console.print("Devices available:\n{}".format(devices))

    n_devices = len(devices)
    input_device = __prompt_user_for_device(console, "Select input device: ", n_devices)
    console.print("Input device: {}".format(devices[input_device].get("name")))

    output_device = __prompt_user_for_device(console, "Select output device: ", n_devices)
    console.print("Output device: {}".format(devices[output_device].get("name")))

    config = configparser.ConfigParser()

    config.add_section("AudioIO")
    config.set("AudioIO", "input_device", str(input_device))
    config.set("AudioIO", "output_device", str(output_device))

    with open(config_filename, "w") as config_file_obj:
        config.write(config_file_obj)
        config_file_obj.flush()
        config_file_obj.close()

def __prompt_user_for_device(console: Console, message: str, n_devices: int) -> int:

    def retry() -> int:
        console.print("Invalid input. Please select a number between 0 and {}.".format(n_devices - 1))
        __prompt_user_for_device(console, message, n_devices)

    user_input = console.read(message)
    try:
        device = int(user_input)
        if device >= 0 & device < n_devices:
            return device
        else:
            retry()
    except ValueError:
        retry()

if __name__ == "__main__":
    set_config(Terminal())
