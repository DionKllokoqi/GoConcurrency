execution_queue = []


class Channel:
    def __init__(self):
        self.closed = False
        self.waiting_to_send = WaitingQueue()
        self.waiting_to_recv = WaitingQueue()


class WaitingQueue(list):
    total = 0

    def enqueue(self, x):
        WaitingQueue.total += 1
        self.append(x)

    def dequeue(self, x=None):
        if x is None:
            x = self.pop(0)
            WaitingQueue.total -= 1
        else:
            # attempt to remove the passed in item from the queue
            idx = self.index(x)
            if idx is not None:
                self.pop(idx)
                WaitingQueue.total -= 1
        return x


def go(callback):
    if callback:
        execution_queue.append(callback)


def run():
    while execution_queue:
        f = execution_queue.pop(0)
        f()

    if WaitingQueue.total > 0:
        raise Exception("fatal error: all goroutines are asleep - deadlock")

def make():
    pass


def len(channel):
    pass


def cap(channel):
    pass


def send(channel, value, callback):
    pass


def recv(channel, callback):
    pass


def close(channel):
    pass


def select(cases, callback):
    pass


default = object()  # used in select
