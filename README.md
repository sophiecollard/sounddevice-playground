# SoundDevice Experiment

Playing around with the [sounddevice](https://python-sounddevice.readthedocs.io/en/0.4.4/usage.html) package.

## Quickstart guide

##### Virtual environment and dependencies

Create and activate a new virtual environment in MacOS/Linux terminal:

```sh
virtualenv /path/to/env
./path/to/env/Scripts/activate
```

In Windows Powershell:

```ps
virtualenv \path\to\env
.\path\to\env\Scripts\activate.ps1
```

Install requirements:

```ps
pip install -r requirements.txt
```

To deactivate the virtual environment at the end of a work session:

```ps
deactivate
```

##### Configuring audio input and output

MacOS/Linux terminal:

```sh
python ./src/configure.py
```

Windows Powershell:

```ps
python .\src\configure.py
```

##### Recording a sample then immediately playing it back

MacOS/Linux terminal:

```sh
python ./src/rec_then_play.py --duration=5
```

Windows Powershell:

```ps
python .\src\rec_then_play.py --duration=5
```

##### Recording a sample and saving it to disk

MacOS/Linux terminal:

```sh
python ./src/rec_to_disk.py --duration=5 --filename="./tmp/sample.npy"
```

Windows Powershell:

```ps
python .\src\rec_to_disk.py --duration=5 --filename=".\tmp\sample.npy"
```

##### Playing a sample from disk

MacOS/Linux terminal:

```sh
python ./src/play_from_disk.py --filename=".\tmp\sample.npy"
```

Windows Powershell:

```ps
python .\src\play_from_disk.py --filename=".\tmp\sample.npy"
```
