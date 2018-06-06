from requests import get

for i in xrange(100):
    print i
    data = get('http://110.10.147.30/res/tile/%d.png' % i).content
    with open('%d.png' % i, 'wb') as f:
        f.write(data)
