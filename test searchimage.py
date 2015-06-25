# small   = small.convert('RGB').convert  ('P', palette=Image.ADAPTIVE, colors=32)
# big     = big.convert('RGB').convert    ('P', palette=Image.ADAPTIVE, colors=32)



def subimg_location(needle,haystack):
    haystack = haystack.convert('RGB')
    needle   = needle.convert('RGB')

    haystack_str = haystack.tostring()
    needle_str   = needle.tostring()    

    gap_size = (haystack.size[0] - needle.size[0]) * 3
    gap_regex = '.{' + str(gap_size) + '}'



    # Split b into needle.size[0] chunks
    chunk_size = needle.size[0] * 3
    split = [needle_str[i:i+chunk_size] for i in range(0, len(needle_str), chunk_size)]

    # Build regex
    regex = re.escape(split[0])
    for i in range(1, len(split)):
        regex += gap_regex.encode() + re.escape(split[i])
        # print(gap_regex,len(split),split[i])

    p = re.compile(regex)
    # print(needle_str)
    # print('\n'*3,split)
    m = p.search(haystack_str)


    if not m:
        return None

    x, _ = m.span()

    left = x % (haystack.size[0] * 3) / 3
    top  = x / haystack.size[0] / 3

    return (int(left), int(top) )

