
def next_coin_greedy(n, change):
    while (n > 0):
        if (n >= 25):
            change.append('quarter')
            n -= 25
            continue
        if (n >= 10):
            change.append('dime')
            n -= 10
            continue
        if (n >= 5):
            change.append('nickel')
            n -= 5
            continue
        if (n >= 1):
            change.append('penny')
            n -= 1
            continue

def make_change_greedy(n):
    change = []
    next_coin_greedy(n, change)
    return change
