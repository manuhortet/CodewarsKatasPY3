ingredients = {'a':'beef','e':'beef','i':'beef','o':'beef','u':'beef','t':'tomato','l':'lettuce','c':'cheese','g':'guacamole','s':'salsa'}
def tacofy(word):
    return ['shell']+[ingredients[c] for c in word.lower() if c in ingredients]+['shell']