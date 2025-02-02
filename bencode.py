def decode_int(x, f):
    f += 1
    newf = x.index('e', f)
    n = int(x[f:newf])
    if x[f] == '-':
        if x[f + 1] == '0':
            raise ValueError
    elif x[f] == '0' and newf != f + 1:
        raise ValueError
    return (n, newf + 1)

def decode_string(x, f):
    colon = x.index(':', f)
    n = int(x[f:colon])
    if x[f] == '0' and colon != f + 1:
        raise ValueError
    colon += 1
    return (x[colon:colon + n], colon + n)

def decode_list(x, f):
    r, f = [], f + 1
    while x[f] != 'e':
        v, f = decode_func[x[f]](x, f)
        r.append(v)
    return (r, f + 1)

def decode_dict(x, f):
    r, f = {}, f + 1
    while x[f] != 'e':
        k, f = decode_string(x, f)
        r[k], f = decode_func[x[f]](x, f)
    return (r, f + 1)

decode_func = {
    'l': decode_list,
    'd': decode_dict,
    'i': decode_int,
    '0': decode_string,
    '1': decode_string,
    '2': decode_string,
    '3': decode_string,
    '4': decode_string,
    '5': decode_string,
    '6': decode_string,
    '7': decode_string,
    '8': decode_string,
    '9': decode_string,
}

def bdecode(x):
    try:
        r, l = decode_func[x[0]](x, 0)
    except (IndexError, KeyError, ValueError):
        raise Exception("not a valid bencoded string")
    return r

class Bencached:
    __slots__ = ['bencoded']

    def __init__(self, s):
        self.bencoded = s

def encode_bencached(x, r):
    r.append(x.bencoded)

def encode_int(x, r):
    r.extend(('i', str(x), 'e'))

def encode_bool(x, r):
    encode_int(1 if x else 0, r)

def encode_string(x, r):
    r.extend((str(len(x)), ':', x))

def encode_list(x, r):
    r.append('l')
    for i in x:
        encode_func[type(i)](i, r)
    r.append('e')

def encode_dict(x, r):
    r.append('d')
    ilist = sorted(x.items())
    for k, v in ilist:
        r.extend((str(len(k)), ':', k))
        encode_func[type(v)](v, r)
    r.append('e')

encode_func = {
    Bencached: encode_bencached,
    int: encode_int,
    str: encode_string,
    list: encode_list,
    tuple: encode_list,
    dict: encode_dict,
    bool: encode_bool,
}

def bencode(x):
    r = []
    encode_func[type(x)](x, r)
    return ''.join(r)
