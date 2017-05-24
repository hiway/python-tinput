# coding=utf-8
import signal


class TinputTimeoutError(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TinputTimeoutError()


def _get_input(prompt):
    try:
        return input(prompt)
    except TinputTimeoutError:
        return None


def signal_timed_input(prompt, timeout):
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout)
    user_input = _get_input(prompt)
    signal.alarm(0)
    return user_input
