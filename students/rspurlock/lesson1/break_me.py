def nameError():
    print(missingVariable)

def typeError():
    print(1/"string")

def syntaxError():
    eval("1/%0")

def attributeError():
    import sys
    sys.bogus

#nameError()
#typeError()
#syntaxError()
#attributeError()
