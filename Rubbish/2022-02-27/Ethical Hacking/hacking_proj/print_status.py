import sys

from termcolor import colored, cprint


# class printStatus():
def successful(mssg):
    v = cprint(f'[+] {mssg}', 'green')
    print(v)


def fail(mssg):
    v = cprint(f'[-] {mssg}', 'red')
    print(v)


def info(mssg):
    v = cprint(f'[+] {mssg}', 'blue')
    print(v)


def testing():
    text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
    print(text)
    cprint('Hello, World!', 'green')

    def print_red_on_cyan(x): return cprint(x, 'red', 'on_cyan')

    print_red_on_cyan('Hello, World!')
    print_red_on_cyan('Hello, Universe!')

    for i in range(10):
        cprint(i, 'magenta', end=' ')

    cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
