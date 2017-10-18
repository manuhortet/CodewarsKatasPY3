def brain_luck(code, input):
    cc = 0
    dc = 0
    ic = 0
    data = []
    output = []
    block = []
    clen = len(code)
    while cc < clen:
        while len(data) <= dc:
            data.append(0)
        if not code[cc]:
            break
        elif code[cc] == '>':
            dc += 1
        elif code[cc] == '<':
            dc -= 1
        elif code[cc] == '+':
            data[dc] = (data[dc] + 1) & 0xff
        elif code[cc] == '-':
            data[dc] = (data[dc] - 1) & 0xff
        elif code[cc] == '.':
            output.append(chr(data[dc]))
        elif code[cc] == ',':
            data[dc] = ord(input[ic])
            ic += 1
        elif code[cc] == '[':
            if not data[dc]:
                bl = len(block)
                block.append(cc)
                cc += 1
                while True:
                    if code[cc] == '[':
                        block.append(cc)
                    elif code[cc] == ']':
                        block.pop()
                    if len(block) == bl:
                        break
                    cc += 1
            else:
                block.append(cc)
        elif code[cc] == ']':
            if data[dc]:
                cc = block[-1]
            else:
                block.pop()
        cc += 1
    return ''.join(output)
'''    
brain_luck(',+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[[++-][+-][++++++++++[--[++-][+-]+[[-][-]][[+-][-]]][++-][+-]+[[-][-]][+[-]]][++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++[--]++++++++++++++++++++++++++++++++++++++++++++++++.[-][++-][+-]-[..[-]][++-][+-][+-][+-]-]', map(chr, [10]))
'''