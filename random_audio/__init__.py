import argparse
from os import listdir
from os.path import isfile, join, splitext
from random import randint, uniform
from pydub import AudioSegment

def main():
    parser = argparse.ArgumentParser(description="Make a randomized mash-up of audio clips.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("directory",
        help="Directory to read audio files from, must contain only the audio files.")
    parser.add_argument("-s", metavar=("A", "B"), nargs=2, type=float,
        help="Each clip is speeded up X times, where X is A random number between A and B."
             " A and B must be greater than 1, and A less than B."
             " Omit this option to have all clips play at normal speed.")
    parser.add_argument("-n", type=int,
        help="Number of times a random clip is picked and added to the mash-up.", default=15)
    parser.add_argument("-o", help="Name of output file.", default="output.mp3")
    parser.add_argument("-v", action="store_true", help="Enable verbose mode.")
    args = parser.parse_args()

    path = args.directory
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    audio_segments = [AudioSegment.from_file(f, splitext(f)[1][1:]) for f in files]

    speed_bounds = [1.01, 1.01]
    if args.s is not None:
        lower, upper = args.s
        speed_bounds = [max(lower, 1.01), max(upper, 1.01)]

    results = AudioSegment.empty()

    for _ in range(args.n):
        audio_seg_index = randint(0, len(audio_segments) - 1)
        audio_seg = audio_segments[audio_seg_index]
        speedup_factor = uniform(*speed_bounds)
        results += audio_seg.speedup(playback_speed=speedup_factor)
        if args.v:
            print("Adding file {} speeded up by a factor of {}".format(files[audio_seg_index], speedup_factor))

    results.export(args.o)

    print("Successfully written output to", args.o)

if __name__ == "__main__":
    main()
