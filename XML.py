#XML 1

def get_attr_number(node):
    # your code goes here
    return etree.tostring(node).count(b'=')
