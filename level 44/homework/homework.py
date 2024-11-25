#1
def string_to_number(s):
    try:
        return int(s)  
    except ValueError:
        try:
            return float()
        except ValueError:
            return None  
#2
def fake_bin(x):
    return ''.join('0' if int(c) < 5 else '1' for c in x)