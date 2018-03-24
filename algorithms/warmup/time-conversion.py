s = raw_input().split(":")
pm = s[-1][2:] == "PM"
s[0] = int(s[0]) % 12
if pm:
    s[0] = str(s[0] + 12)
elif s[0] == 0:
    s[0] = "00"

print "{0}:{1}:{2}".format(s[0], s[1], s[-1][:2])
