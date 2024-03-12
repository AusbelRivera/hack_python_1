"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    new_result = []
    for i in result:
        if i == "o":
            new_result.append("0")
        elif i == "i":
            new_result.append("1")
        elif i == "a":
            new_result.append("@")
        else:
            new_result.append(i.upper())
    
    result = new_result
    print(result)
    return result  

fn_hack_10()