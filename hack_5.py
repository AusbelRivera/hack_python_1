"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    new=result.replace(result,"f00z1m@n")
    result = new
    print(new)
    return result

fn_hack_5()  