def get_sublists(a):
    ans = []
    for i in range(pow(2, len(a))):
        ans.append([])
        for j in range(len(a)):
            if (i & pow(2, j)):
                ans[-1].append(a[j])
    return ans


def sublists_wrapper(input_string):
    "Get all sublists of provided list."
    return get_sublists(input_string.split())
