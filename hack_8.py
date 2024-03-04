"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result = [result[item] for item in range(1,4)]
    print(result)
    return result  

fn_hack_8()