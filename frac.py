from fractions import Fraction

DEBUG_MODE = False


def frac(amount, limit=100):
    """Takes a string, e.g., `'0.17603'` or a float, e.g., `0.17603`
    and returns a tuple where the first element is the Fraction and
    the second element is the difference to the original value as a
    proportion of the original value.
    """
    frac = Fraction(amount).limit_denominator(limit)
    frac_double = frac.numerator / frac.denominator

    try:
        frac_diff = frac_double - amount
    except TypeError:  # amount is a string
        amt = float(amount)
        frac_diff = frac_double - amt
        relative_diff = frac_diff / amt
    else:
        relative_diff = frac_diff / amount

    return (frac, relative_diff)


def simplest_frac(amount, max_diff=0.01, stepfunc=None, debug=DEBUG_MODE):
    """Computes the simplest (smallest denominator) fraction that
    approximates (within `max_diff * amount`) amount. By default, increases
    the limit by 1 each time (slow) but will definitely stop at the first
    result that is sufficiently simple.

    Alternatively, pass a function (stepfunc is a func of type (int) -> int
    ). For example `lambda x: 10 * x` will increase the limit by an order
    of magnitude each iteration, thus it will find first the best result
    with a max denominator of 1, then the best result with a max
    denominator of 10, then the best result with a max denominator of 100
    and so on until a result is found that is sufficiently close to the
    target."""
    current_diff = max_diff + 1
    current_result = None
    current_limit = 1
    while abs(current_diff) > max_diff:
        current_result = frac(amount, current_limit)
        if debug:
            print(f'max diff: {max_diff}')
            print(f'current_diff: {current_diff}')
            print(f'current_limit: {current_limit}')
            print(f'current_result: {current_result}')
        
        current_diff = current_result[1]
        if stepfunc:
            if debug:
                print(f'stepfunc provided')
            current_limit = stepfunc(current_limit)
        else:
            if debug:
                print(f'no stepfunc provided')
            current_limit += 1

    if debug:
        print(f'\n\nFinal result:')
        print(f'{current_result} (limit: {current_limit})')
    return current_result

