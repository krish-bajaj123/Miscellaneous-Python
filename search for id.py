a=[(b'DL-1A-2402 / E-2',  1, b'corona'),(b'DL-1A-2402 / E-2',  1, b'non corona'),(b'DL-1A-2403 / W-20',  1, b'non corona')]
x="W-20"
for y in a:
    if x in y[0].decode('utf-8'):
        print(y)
