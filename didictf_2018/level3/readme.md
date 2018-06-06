DDCTF{ddctf-android2-KEY}

p = 0x17A904F1B91290
mod = 0xDBDEE7AE5A90

```
In [23]: i = 1
    ...: remain = 1
    ...: while True:
    ...:     remain = ((remain << 1) & 0xFFFFFFFFFFFFFFFF) % 0x17A904F1B91290
    ...:     if remain == 0xDBDEE7AE5A90:
    ...:         print i, remain, hex(remain >> 32), hex(remain & 0xFFFFFFFF)
    ...:         break
    ...:     i += 1
    ...:
595887 241750416186000 0xdbdeL 0xe7ae5a90L
```