from subprocess import Popen, PIPE


def simple_proc(args):
    proc = Popen(args, stdout=PIPE)
    return proc

def simple_read(proc: Popen) -> bytes:
    output, _ = proc.communicate()
    return output
