import ctypes
import functools
import multiprocessing as mp
import os
import time
import wave

import simpleaudio as sa


def skrrt(_func=None, *, audio_file=''):
    if audio_file == '':
        audio_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'mario_15.wav'
        )

    def skrrt_decorator(func):
        return_val = mp.Queue()
        func_running = mp.Value(ctypes.c_bool, True)

        def play_sound():
            wave_obj = sa.WaveObject.from_wave_file(audio_file)

            while func_running.value is True:
                play_obj = wave_obj.play()
                play_obj.wait_done()

        def subwrapper(func, args, kwargs):
            return_val.put(func(*args, **kwargs))
            func_running.value = False

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            p1 = mp.Process(target=subwrapper, args=(func, tuple(args), dict(kwargs)))
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