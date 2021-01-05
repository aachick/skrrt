import argparse
import os
import subprocess as sp
import sys

from skrrt import skrrt


def _cli_entry():
    """Play music while executing a program.

    Example usage: skrrt sleep 10
    """
    parser = argparse.ArgumentParser(
        prog=__name__,
        description=__doc__,
    )
    parser.add_argument(
        "-i",
        "--input",
        dest="input_file",
        default="",
        help="The non-default audio file to play."
    )

    args, unknown = parser.parse_known_args()
    music_file = args.input_file

    if music_file and not os.path.exists(music_file):
        msg = "{} does not exist.".format(music_file)
        parser.exit(1, message=msg)

    @skrrt(audio_file=music_file)
    def exec_subcommand(args: list):
        pipe = sp.Popen(args, stdout=sp.PIPE, stderr=sp.PIPE)
        out, err = pipe.communicate()

        ret = pipe.poll()

        if ret:
            print(err.decode(), file=sys.stderr)
        else:
            print(out.decode())

        return ret

    sys.exit(exec_subcommand(unknown))


if __name__ == "__main__":
    _cli_entry()
