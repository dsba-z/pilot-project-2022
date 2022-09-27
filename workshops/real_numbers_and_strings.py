def interest_rate(interest_rate, rubles, kopecks):
    k = (rubles * 100 + kopecks) * (100 + interest_rate) // 100
    return k//100, k % 100


def interest_rate_wrapper(input_string):
    rate, rubles, kopecks = map(int, input_string.split())
    ans = interest_rate(rate, rubles, kopecks)
    print("In one year you will get {} rub {} kop".format(ans[0], ans[1]))
