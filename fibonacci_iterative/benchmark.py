# importing the required modules
import timeit
import os

PLACES = 100000


def benchIt(dir):
  if not dir:
    raise ValueError("Parameter 'dir' is required.")

  if dir == "_V":
    SETUP_CODE = '''
from ctypes import CDLL
lib = CDLL("./{dir}/fib_iter.so")
  '''.format(**locals())

    TEST_CODE = '''
x = lib.fib_iter__fib({PLACES})'''.format(**globals())  
  else:
    SETUP_CODE = '''
from {dir} import fib_iter
  '''.format(**locals())

    TEST_CODE = '''
x = fib_iter.fibIter({PLACES})'''.format(**globals())

  # timeit.repeat statement
  times = timeit.repeat(
    setup=SETUP_CODE,
    stmt=TEST_CODE,
    repeat=3,
    number=10
    )

  # printing minimum exec. time
  return min(times)


if __name__ == "__main__":
  print("\nRunning benchmark 'fibonacci_iterative' to {PLACES} places.".format(**globals()))
  print("---------------------------------------------------"+('-'*len(str(PLACES))))

  dictTimes = dict()

  for benchName in ['Python', 'Nuitka', 'Cython', 'Numba', 'Nim', 'V']:
    dirName = '_'+benchName
    path    = os.getcwd()+os.path.sep+dirName
    if os.path.exists(os.path.abspath(path)):
      time = benchIt(dirName)
      dictTimes[benchName] = time
      speedup = dictTimes['Python'] / time
      print('{benchName:7}: {time:.4f}s'.format(**locals()) + '{speedup:>40,.2f}x'.format(**locals()))
