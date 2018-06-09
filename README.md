# random_audio

A Python CLI tool to generate a mash-up of audio clips. An excellent use case is when you have potentially embarassing audio clips of your friends and you'd like to embarass them further.

## Installation

Run `pip install random_audio`.

## Usage

```
usage: random_audio [-h] [-s A B] [-n N] [-o O] [-v] directory

Make a randomized mash-up of audio clips.

positional arguments:
  directory   Directory to read audio files from, must contain only the audio
              files.

optional arguments:
  -h, --help  show this help message and exit
  -s A B      Each clip is speeded up X times, where X is A random number
              between A and B. A and B must be greater than 1, and A less than
              B. Omit this option to have all clips play at normal speed.
              (default: None)
  -n N        Number of times a random clip is picked and added to the mash-
              up. (default: 15)
  -o O        Name of output file. (default: output.mp3)
  -v          Enable verbose mode. (default: False)
```

### Example Usage

All audio clips are in a folder `audio/` in the current directory, we want to output to `masterpiece.mp3` and want our clips to be speeded up by a factor in the range 2-3:

`random_audio -s 2 3 -o masterpiece.mp3 audio/`