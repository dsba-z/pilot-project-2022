def interest_rate(rate, rubles, kopecks):
    k = (rubles * 100 + kopecks) * (100 + rate) // 100
    return k//100, k % 100


def interest_rate_wrapper(input_string):
    """Calculate interest problem."""
    rate, rubles, kopecks = map(int, input_string.split())
    ans = interest_rate(rate, rubles, kopecks)
    print(f"In one year you will get {ans[0]} rub {ans[1]} kop")
