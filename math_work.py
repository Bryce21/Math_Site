import math
import pprint


def binomial(number_of_successes, total_tests, prob_of_success):
    """
    In the theory of probability and statistics, a Bernoulli trial (or binomial trial) is a random experiment with exactly
    two possible outcomes, "success" and "failure", in which the probability of success is the same every time the experiment
    is conducted.
    """
    if number_of_successes > total_tests:
        return 0
    coef = get_bernoulli_coeffiecient(total_tests, number_of_successes)
    return "%.2f" % (coef * prob_of_success ** number_of_successes * (1 - prob_of_success) ** (
            total_tests - number_of_successes) * 100)


def get_bernoulli_coeffiecient(total_flips, number_of_successes):
    """
    Helper function to find the coeffiecient for the bernoulli equation.
    """
    return math.factorial(total_flips) / (
            math.factorial(number_of_successes) * (math.factorial(total_flips - number_of_successes)))


def same_birthday_probability(n):
    return "%.2f" % ((1 - (364 / 365) ** (n - 1)) * 100)


if __name__ == '__main__':
    print('Main')
    [print('t{}_r{}_c{}'.format(t, r, c), 'value') for t in range(1, 3) for r in range(1, 4) for c in range(1, 4)]
