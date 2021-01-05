# skrrt

`skrrt` is a package designed to play audio files during the execution of other routines. Currently, only non-compressed `.wav` files are supported.

## Installation

1. Install with `pip` from the command line:

```bash
pip install git+https://github.com/aachick/skrrt.git
```

## TODO list

Some nice features to add to the decorator would be:

* Support for other audio formats than `.wav`

* Support for playlists

## Example

The following example will play the default package audio file (the Mario theme song) during the execution of the function that it wraps.

```python
import time

import skrrt


@skrrt.skrrt
def wasting_time():
    print("About to waste some time.")
    time.sleep(10)
    print("Now let's get back to business.")


if __name__ == '__main__':
    wasting_time()
```

You may also specify a different file path in order to play a different audio track as so:

```python
@skrrt.skrrt(audio_file='path/to/file.wav')
def wasting_time():
    print("About to waste some time.")
    time.sleep(10)
    print("Now let's get back to business.")
```

`skrrt` can also be used from the command line:

```bash
skrrt sleep 5
```

With a custom `.wav` file:
```bash
skrrt -i mymusic.wav sleep 5
```

## Dependencies

`skrrt` was written using Python 3.6 and depends on the `simpleaudio` package to function (link [here](https://pypi.org/project/simpleaudio/)).
