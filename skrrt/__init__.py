import ctypes
import functools
import multiprocessing as mp
import os
import time
import wave

import simpleaudio as sa


_AUDIO_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "audio"
)


def skrrt(_func=None, *, audio_file=""):
    if not audio_file:
        audio_file = os.path.join(_AUDIO_DIR, "mario.wav")

    def skrrt_decorator(func):
        return_val = mp.Queue()
        func_running = mp.Value(ctypes.c_bool, True)

        def play_sound():
            failed = False
            try:
                wave_obj = sa.WaveObject.from_wave_file(audio_file)
            except (FileNotFoundError, wave.Error):
                print("\033[93mCould not load original file.\033[0m")
                wave_obj = sa.WaveObject.from_wave_file(
                    os.path.join(_AUDIO_DIR, "failure.wav")
                )
                failed = True

            while func_running.value is True:
                play_obj = wave_obj.play()
                play_obj.wait_done()
                if failed is True:
                    break

        def subwrapper(func, args, kwargs):
            return_val.put(func(*args, **kwargs))
            func_running.value = False

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            p1 = mp.Process(
                target=subwrapper, args=(func, tuple(args), dict(kwargs))
            )
            p2 = mp.Process(target=play_sound)

            p1.start()
            p2.start()

            p1.join()
            p2.terminate()

            return return_val.get()

        return wrapper

    if _func is None:
        return skrrt_decorator
    else:
        return skrrt_decorator(_func)


if __name__ == "__main__":
    pass
