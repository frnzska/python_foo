import time
import asyncio


def timing(f):
    def wrap(*args):
        time1 = time.time()
        result = f(*args)
        time2 = time.time()
        print('{:s} function took {:.4f} sec'.format(f.__name__, (time2-time1)), f' for x={args}')
        return result
    return wrap

### Basic

async def my_costy_function(x):
    print(f'in costy with {x}')
    for i in range(0,x):
        x**i

    print(f'done for costy with {x}')
    return x

@timing
def main():
    tasks=(my_costy_function(i) for i in range(100, 5000, 100))
    loop = asyncio.get_event_loop()
    x = loop.run_until_complete(asyncio.gather(*tasks))
    print(x)

# sequencially
def _my_costy_function(x):
    print(f'in costy with {x}')
    for i in range(0,x):
        x**i
    print(f'done for costy with {x}')
    return x


@timing
def _main():
    x = [_my_costy_function(i) for i in range(100, 5000, 100)]




main()
#_main()