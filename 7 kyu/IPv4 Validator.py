import re

def ipValidator(ip):
    if ip is ip.replace(' ', ''):
        list = ip.split(".")
        if len(list) is 4:
            print(list)
            for x in range(0, len(list)):
                try:
                    if int(list[x]) < 0 or int(list[x]) > 255:
                        return False
                except ValueError:
                    return False
            return True
    return False
