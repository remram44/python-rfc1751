This is a Pure-Python implementation of [RFC 1751](https://www.rfc-editor.org/rfc/rfc1751).

Using this small library, you can turn binary strings (for example IDs or passwords) into small sequences of short English words. For example:

```
EB33 F77E E73D 4053
```

would become:

```
TIDE ITCH SLOW REIN RULE MOT
```

The algorithm turns a 64-bit string into 6 English words and vice versa. Two bits of parity are included in the sequence of words, which allow detecting an invalid or corrupted phrase.
