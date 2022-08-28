import argparse
import matplotlib.pyplot as plt
import numpy as np


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Measure error of numerical intergration."
    )
    parser.add_argument(
        "n_max",
        metavar="n_max",
        type=int,
        help="maximal number of bins to use for integration",
    )
    parser.add_argument(
        "a", metavar="a", type=float, help="lower bound for integration"
    )
    parser.add_argument(
        "b", metavar="b", type=float, help="upper bound for integration"
    )

    return parser.parse_args()


def integrate(f, a, b, n):
    s = 0.0
    for i in range(n):
        dx = (b - a) / n
        x = a + (i + 0.5) * dx
        s += f(x) * dx
    return s


def measure_integration_errors(n_max, a, b):
    f = lambda x: x ** 4 - 3 * x
    F = lambda x: 1 / 5 * x ** 5 - 3 / 2 * x ** 2

    errors = []
    for n in range(1, n_max):
        F_analytical = F(b) - F(a)
        F_numerical = integrate(f, a, b, n)
        error = F_analytical - F_numerical
        errors = errors + [error]
    return errors


def plot_results(n_max, errors):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(1, n_max)
    ax.set_ylim(1e-4, max(errors))
    ax.set_xlabel("Number of bins")
    ax.set_ylabel("Error")
    ax.set_yscale("log")
    ax.plot(range(1, n_max), errors)
    fig.savefig("numerical_integration_error.pdf")


def main():
    args = parse_arguments()
    errors = measure_integration_errors(args.n_max, args.a, args.b)
    plot_results(args.n_max, errors)


if __name__ == "__main__":
    main()
