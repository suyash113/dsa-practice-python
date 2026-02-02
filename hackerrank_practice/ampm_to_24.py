def timeConversion(s):
    # Write your code here
    ampm = s[-2:] 
    s2 = ""
    if ampm == "AM" and int(s[:2]) >= 12:
        s2 = "00" + s[2:-2]
    elif ampm == "PM" and int(s[:2]) < 12:
        s2 = str(12 + int(s[:2])) + s[2:-2]
    else:
        s2 = s[:-2]
    return s2
s = "12:45:54PM"
print(timeConversion(s))