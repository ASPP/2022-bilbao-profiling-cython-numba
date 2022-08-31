import time


def function_a():
    time.sleep(0.2)
    function_b()


def function_b():
    time.sleep(0.8)


def function_c():
    time.sleep(0.4)


if __name__ == "__main__":
    function_a()
    function_c()
