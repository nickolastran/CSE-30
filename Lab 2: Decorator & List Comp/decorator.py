import time

def calculate_time(x):
    def wrapping_function(*args, **kwargs):
        start = time.time()
        result = x(*args, **kwargs)
        stop = time.time()
        print(f'It took {stop-start} sec.')
        return result
    return wrapping_function

@calculate_time
def sum1(n):
   result = 0
   for i in range(1, n + 1):
      result += i
   return result

if __name__ == '__main__':
    n = 1000000
    s = sum1(100000)
    print(f'The sum of numbers from 1 to {n} is {s}.')
