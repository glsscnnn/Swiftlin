# Tokens

What are tokens? Tokens are the things that mean something a token essentially is an object that is telling the computer what a certian symbol means, the tokens are going to consist of two attributes (pattern, action) the pattern is the set which the symbol belongs to, the action is the action which the symbol proforms. For example if we have the symbol ``+`` this is a plus sign the object or token which contains the meaning of this symbol would say that this sign contains pattern BINOP which is the label we would give this general set of operators, if it was a letter we may use the pattern ALPHABET or LETTER to denote the set which the character belongs to. So for this plus the action that it does is concat two diffrent identifiers, in an operation ADD(n1, n2) where ``+`` would signify that these two n1 and n2 are action on each other with action ADD. Examples:

``` python

class plus:
    def __init__(self, val = "+"):
        self.val = val
        self.pat = BINOP
        self.action = ADD(n1, n2)
        # checks if not plus
        if self.val != "+":
            print("Error")
        else:
            return (self.pat, self.action)

class f_slash:
    def __init__(self, val = "/"):
        self.val = val
        self.pat = BINOP
        self.action = DIVIDE
        if self.val != "/":
            print("Error")
        else:
            return (self.pat, self.action)

class LETTER:
    def __init__(self, val = None):
        self.val = val
        if self.val in ALPHABET:
            return self.val
        elif self.val == ' ':
            pass
        elif self.val == None:
            return EOF
        else:
            print("Error")
```