def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Please call me back at 415-555-1011. my office number is 415-555-9999'

# this for loop will pass iterations of a chunk 12 indexes long
# it will pass through each index measuring all 12 looking for matches to the criteria
# in the isPhoneNumber() Function.
for i in range(len(message)):
    chunk = message[i: i+12]        # 'chunk' is 12 indexes long
    if isPhoneNumber(chunk):
        print('Phone Number Found: ' + chunk)

print("Done")
