#Function to generate a NameError by trying to print a missing variable
def nameError():
    print(missingVariable)

#Function to generate a TypeError by trying to divide a number by a string
def typeError():
    print(1/"string")

#Function to generate a SyntaxError by trying to evaluate invalid python code
def syntaxError():
    eval("1/%0")

#Function to generate a AttributeError by trying to use an invalid attribute from system object
def attributeError():
    import sys
    sys.bogus

#Uncomment the following line to generate a NameError
#nameError()

#Uncomment the following line to generate a TypeError
#typeError()

#Uncomment the following line to generate a SyntaxError
#syntaxError()

#Uncomment the following line to generate a AttributeError
#attributeError()
