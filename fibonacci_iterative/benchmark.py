# importing the required modules
import timeit

PLACES = 100000


def python_fib_iter():
  SETUP_CODE = '''
from _Python import fib_iter
  '''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def nuitka_fib_iter():
  SETUP_CODE = '''
from _Nuitka import fib_iter
'''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def nim_fib_iter():
  SETUP_CODE = '''
from _Nim import fib_iter
  '''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def cython_fib_iter():
  SETUP_CODE = '''
from _Cython import fib_iter
  '''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


def numba_fib_iter():
  SETUP_CODE = '''
from _Numba import fib_iter
  '''

  TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=20
    )

  # printing minimum exec. time
  return min(times)


if __name__ == "__main__":
  print("\nRunning benchmark 'fibonacci_iterative' to {PLACES} places.".format(**globals()))
  print("---------------------------------------------------"+('-'*len(str(PLACES))))

  min_time_python = python_fib_iter()
  print('Pure Python : {min_time_python:.4f}s'.format(**locals()))
  
  min_time_nuitka = nuitka_fib_iter()
  diff_nuitka = min_time_python / min_time_nuitka
  print('Nuitka      : {min_time_nuitka:.4f}s'.format(**locals()) + '{diff_nuitka:>40,.2f}x'.format(**locals()))
  
  min_time_cython = cython_fib_iter()
  diff_cython = min_time_python / min_time_cython
  print('Cython      : {min_time_cython:.4f}s'.format(**locals()) + '{diff_cython:>40,.2f}x'.format(**locals()))

  min_time_numba = numba_fib_iter()
  diff_numba = min_time_python / min_time_numba
  print('Numba       : {min_time_numba:.4f}s'.format(**locals()) + '{diff_numba:>40,.2f}x'.format(**locals()))

  min_time_nim = nim_fib_iter()
  diff_nim = min_time_python / min_time_nim
  print('Nim         : {min_time_nim:.4f}s'.format(**locals()) + '{diff_nim:>40,.2f}x'.format(**locals()))