## Clear the Mind
> They've gotten into your mind, but haven't managed to dive that deep yet. Root them out before it becomes an issue.

RSA with very small e. Take the e root of c.

```
>>> import gmpy2
>>> from Crypto.Util.number import long_to_bytes
>>> gmpy2.get_context().precision=2048
>>> e = 3
>>> c = 4458558515804625757984145622008292910146092770232527464448604606202639682157127059968851563875246010604577447368616002300477986613082254856311395681221546841526780960776842385163089662821
>>> pt = gmpy2.root(c, e)
>>> print(long_to_bytes(pt).decode())
```

Flag: `flag{w3_need_7o_g0_d3ep3r}`

