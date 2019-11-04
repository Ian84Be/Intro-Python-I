import functools
import time

def timer(func):
	@functools.wraps(func)
	def wrapper_timer(*args, **kwargs):
		start = time.perf_counter
		value = func(*args, **kwargs)
		end = time.perf_counter()
		run_time = end - start
		print(f'Ran {func.__name__!r} in {run_time:.4f} secs')
		return value
	return wrapper_timer