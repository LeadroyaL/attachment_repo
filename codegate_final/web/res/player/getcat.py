from requests import get

for i in xrange(30):
    print i
    data = get('http://110.10.147.30/res/player/cat%d.png' % i).content
    with open('cat%d.png' % i, 'wb') as f:
        f.write(data)
