#Adam Ignaciuk - Python w zastosowaniach naukowych, zajęcia 3

import functools
import time
import numpy as np
import matplotlib.pyplot as plt
from rich import print as rprint
from rich.console import Console
from rich.table import Table

def mydecorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        functionvalues = []
        functionvalues.append("Time of resolving[1]:")
        start = time.time()
        func(*args)
        stop = time.time()
        resolving = stop-start
        functionvalues.append(resolving)
        functionvalues.append("Maximum value[3]:")
        maximum = max(func(*args))
        functionvalues.append(maximum)
        functionvalues.append("Minimum value[5]:")
        minimum = min(func(*args))
        functionvalues.append(minimum)
        functionvalues.append("Standard deviation[7]:")
        dev = np.std(func(*args))
        functionvalues.append(dev)
        functionvalues.append("Mean value[9]:")
        mean = np.mean(func(*args))
        functionvalues.append(mean)
        console = Console()
        #console.log("Function", func.__name__, "values and other")
        table = Table(title="Values extracted from function "+func.__name__)
        table.add_column("Name", style="cyan")
        table.add_column("Value", style="magenta")
        table.add_row("Time of resolving", str(resolving))
        table.add_row("Max", str(maximum))
        table.add_row("Min", str(minimum))
        table.add_row("Standard deviation", str(dev))
        table.add_row("Mean value", str(mean))
        console.print(table)
        #rprint("Time of function resolving: ", resolving)
        return func(*args, **kwargs), functionvalues
    return wrapper

MAX_ITER = 100
@mydecorator
def FFT(arr):
    t = np.arange(arr)
    sp = np.fft.fft(np.sin(t))
    freq = np.fft.fftfreq(t.shape[-1])
    return freq


function,dec = FFT(100000)
#print(dec)

