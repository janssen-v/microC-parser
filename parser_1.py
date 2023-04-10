sampleTokens = ['INT ID SEMI INT ID SEMI ID ASSIGN ID PLUS INT_NUM SEMI RETURN SEMI EOF']

# Turns a string of tokens into a list of tokens
def splitTokens(tokenString):
    return tokenString[0].split()


# LR(1) Shift-Reduce Parser
def parseInput(tokens):
    stack=[]
    for tokIter in range(len(tokens)):
        token = tokens[tokIter]
        lookahead = tokens[tokIter+1]
        
        
        
        
        
            


tokenList = splitTokens(sampleTokens)
parseInput(tokenList)
