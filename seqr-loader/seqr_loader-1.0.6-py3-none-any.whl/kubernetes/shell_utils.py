from collections import namedtuple
from io import StringIO
import logging
import os
import subprocess
import sys

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def run_in_background(command, print_command=True, env={}):
    """Runs the given command in a shell and returns without waiting for the command to finish.

    Args:
        command (string): the command to run
        print_command (bool): whether to print command before running
        env (dict): A custom environment in which to run
    Return:
        subprocess Popen object
    """
    full_env = dict(os.environ)  # copy external environment
    full_env.update({key: str(value) for key, value in env.items()})  # make sure all values are strings

    if print_command:
        logger.info("==> %(command)s" % locals())

    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=full_env, bufsize=1)

    return p


def simple_run(command):
    print(command)
    os.system(command)


def run(command,
        ok_return_codes=(0,),
        errors_to_ignore=None,
        ignore_all_errors=False,
        print_command=True,
        verbose=True,
        env={},
        is_interactive=False):

    """Runs the given command in a shell.

    Args:
        command (string): the command to run
        ok_return_codes (list): list of returncodes that indicate the command succeeded
        errors_to_ignore (list): if the command's return code isn't in ok_return_codes, but its
            output contains one of the strings in this list, the bad return code will be ignored,
            and this function will return None. Otherwise, it raises a RuntimeException.
        ignore_all_errors (bool): if True, all non-zero return codes will be ignored.
        print_command (bool): whether to print command before running
        verbose (bool): whether to print command output while command is running
        wait (bool): Whether to wait for the command to finish before returning
        env (dict): A custom environment in which to run
    Return:
        string: command output (combined stdout and stderr), or if return_subprocess_obj=True the return 2-tuple: (output, subprocess Popen object)
    """
    full_env = dict(os.environ)  # copy external environment
    full_env.update({key: str(value) for key, value in env.items()})  # make sure all values are strings

    if print_command:
        logger.info("==> %(command)s" % locals())

    if is_interactive:
        p = subprocess.Popen(command, shell=True, env=full_env)
        p.wait()
        return None

    # pipe output to log
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=full_env, bufsize=1)
    line_buffer = StringIO()
    log_buffer = StringIO()
    previous_is_slash_r = False
    while True:
        out = p.stdout.read(1).decode('utf-8')
        if out == '' and p.poll() is not None:
            break
        if out != '':
            log_buffer.write(out)
            if verbose:
                line_buffer.write(out)
                if out.endswith('\r') or (out.endswith('\n') and previous_is_slash_r):
                    sys.stdout.write(line_buffer.getvalue())
                    sys.stdout.flush()
                    line_buffer = StringIO()
                    previous_is_slash_r = True
                elif out.endswith('\n'):
                    logger.info(line_buffer.getvalue().rstrip('\n'))
                    line_buffer = StringIO()
                    previous_is_slash_r = False
                else:
                    previous_is_slash_r = False
    p.wait()

    output = log_buffer.getvalue()
    if p.returncode not in ok_return_codes:
        if ignore_all_errors or (errors_to_ignore and any([error_to_ignore in str(output) for error_to_ignore in errors_to_ignore])):
            return None
        else:
            raise RuntimeError(output)
    else:
        return output


def wait_for(procs):
    """Takes a list of subprocess.Popen objects and doesn't return until all these processes have completed"""

    for proc in procs:
        proc.wait()


def ask_yes_no_question(question):
    """Prompt the user and return True or False depending on whether they replied 'Y' or 'n'

    Args:
        question (string): question to ask
    """
    while True:
        i = raw_input(str(question) + " [Y/n] ")

        if i and i.lower() == 'y':
            return True
        elif i and i.lower() == 'n':
            return False


FileStats = namedtuple('FileStats', ['ctime', 'mtime', 'size', 'md5'])


def get_file_stats(file_path):
    """
    """
    return FileStats(
        ctime=os.path.getctime(file_path),
        mtime=os.path.getmtime(file_path),
        size=os.path.getsize(file_path),
    )