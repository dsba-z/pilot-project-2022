def get_sublists(a):
    ans = []
    for i in range(pow(2, len(a))):
        ans.append([])
        for j, x in enumerate(a):
            if i & pow(2, j):
                ans[-1].append(x)
    return ans


def sublists_wrapper(input_string):
    "Get all sublists of provided list."
    return get_sublists(input_string.split())
