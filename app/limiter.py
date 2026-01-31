import time

_last_reset = time.time()
_count = 0

def allow(limit):
    global _last_reset, _count

    now = time.time()
    if now - _last_reset >= 3600:
        _last_reset = now
        _count = 0

    if _count >= limit:
        return False

    _count += 1
    return True
