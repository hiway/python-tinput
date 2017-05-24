# coding=utf-8
from __future__ import print_function

import select
import signal
import sys


class TinputTimeoutError(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TinputTimeoutError()


def _get_select_input(prompt):
    try:
        return input(prompt)
    except TinputTimeoutError:
        return None


def signal_timed_input(prompt, timeout):
    """
    ref: 
      - https://stackoverflow.com/a/1336751/996800
    """
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)
    user_input = _get_select_input(prompt)
    signal.alarm(0)
    return user_input


def select_timed_input(prompt, timeout):
    """
    ref: 
     - https://stackoverflow.com/a/2904057/996800
     - https://stackoverflow.com/a/230774/996800
    """
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [], [], timeout)
    if ready:
        return sys.stdin.readline().strip()
    else:
        return None
