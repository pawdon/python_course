from subprocess import call, Popen, PIPE, DEVNULL
import time


def run_shell():
    print('START')
    rc = call('git status', stdout=DEVNULL)
    print('RESULT', rc)


def run_shell_to_file():
    print('START')
    with open('logs.txt', 'w') as f:
        # rc = call('git status', stdout=f, stderr=f)
        rc = call(['git', 'status'], stdout=f, stderr=f)  # nie zaleca sie przechwytywania outputu bezposrednio do zmiennej
    print('RESULT', rc)


def run_shell2():
    print('START')
    p = Popen('git status')  # , stdout=
    print('SLEEP')
    time.sleep(3)
    print('COMMUNICATE')
    p.communicate()  # czekamy na zakonczenie
    rc = p.returncode
    print('RESULT', rc)


def run_and_read_output():
    print('START')
    # PIPE oznacza, ze chcemy przechwycic
    p = Popen('git status', stdin=PIPE, stdout=PIPE, stderr=PIPE)  # , encoding='utf-8'
    print('SLEEP')
    time.sleep(3)
    print('COMMUNICATE')
    output, err = p.communicate()  # timeout
    rc = p.returncode
    print('RESULT', rc)
    print('OUTPUT', output)  # output.decode("utf-8")
    print('ERR', err)


run_and_read_output()
