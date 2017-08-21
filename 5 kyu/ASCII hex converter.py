class Converter(object):
    @staticmethod
    def to_ascii(s):
        return s.decode('hex')

    @staticmethod
    def to_hex(s):
        return s.encode('hex')