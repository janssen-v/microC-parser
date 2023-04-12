import csv

# Helper Functions

# Preprocesses output from scanner to make it compatible with this parser
def preprocess(filename):
    f = open(filename, 'r')
    tokens = (f.read().strip().split('\n'))
    f.close()
    cleanTokens = []
    for token in tokens:
        cleanTokens.append(token[7:])
    cleanTokens.append('EOF')
    #output = " ".join(cleanTokens)
    return cleanTokens

# If table has a shift reduce conflict of sSV / rRV, return (SV, RV) 
def splitSHR(shiftreduce):
    temp = shiftreduce.split('/')
    sr = []
    for item in temp:
        sr.append(item.strip())
    shift = sr[0]
    reduce = sr[1]
    return (shift[1:], reduce[1:])

def printCurrent(state, stack, input, action):
    curStack = stack.copy()
    curState = state[-1]
    nextType = input[0]
    nextAction = ''
    # Action Formatting
    # Case SHIFT/REDUCE
    
    if ('/' in action):
        '''
        temp = action.split('/')
        sr = []
        for item in temp:
            sr.append(item.strip())
        nextAction = 'shift to state' + sr[0][1:]
        '''
        SV, RV =splitSHR(action)
        nextAction = 'shift to state ' + SV
    # Case SHIFT
    elif ('s' in action):
        nextAction = 'shift to state ' + action[1:]
    # Case REDUCE
    elif ('r' in action):
        lhs, rhs = getRule(action[1:])
        rhs = (' ').join(rhs)
        rule = (lhs, rhs)
        nextType = lhs
        nextAction = 'reduce by grammar ' + action[1:] + ': ' + ('->').join(rule) 
    # Case GOTO
    elif (action.isnumeric()):
        nextAction = 'goto state ' + action
        
    elif (action == 'acc'):
        nextAction = 'Accept !'
    
    # Add stack pointer
    # If stack less than state, pointer at end
    if len(stack) < len(state):
        curStack.append('|')
    # If stack equals state, pointer before last
    else:
        curStack.insert(-1,'|')
    
    print(f'state: {curState:8} next type: {nextType:18} {nextAction}')
    print('current parsing stack: ' + (' ').join(curStack))    
    
    print()   

# Parser
MAX_STEPS = 1000

grammarfile = open("Grammars/grammarPART.txt", "r")
gramload = grammarfile.read()
grammar = gramload.split("\n")
rules = []
for line in grammar:
    if (line == ''):
        continue
    else:
        rules.append(line)
grammarfile.close()


# Turns a string of tokens into a list of tokens (used for sample only)
def splitSampleTokens(tokenString):
    return tokenString.strip().split()

def getRule(rule):
    # Convert Production Rule
    prod = rules[int(rule)].split('->')
    lhs = prod[0]
    lhs = lhs.strip()
    rhs = prod[1].strip()
    rhs = rhs.split(' ')
    return(lhs, rhs)

# LR(1) Shift-Reduce Parser
def parseInput(tokens, table):
    accept = False
    input = tokens.copy()
    input.append('$')
    state = ['0']
    stack = []
    step = 1
    # While state != accept state
    while (accept != True):
        # Look up table based on current state
        
        lookup = table[int(state[-1])]
        # If state.len <= stack.len, GOTO
        if (len(state) <= len(stack)):
            action = (lookup[stack[-1]])
        else:
            action = lookup[input[0]]


        # print("State:", state)
        # print("S:", step, "Stack:", stack, "Input:", input, "Action:", action)
        # print()
        #printCurrent(state, stack, input, action)
        
        # Break if past maximum runtime or if accept state
        if (step > MAX_STEPS or action == 'acc'):
            break
        
        # Make case for empty '' action 
        # Case SHIFT/REDUCE Conflict
            # Shift by Default
        # Case SHIFT
        if ('s' in action):
            state.append(action[1:])
            stack.append(input.pop(0))
        # Case REDUCE
        elif ('r' in action):
            # Reduce by grammar action[-1]
            lhs, rhs = getRule(action[1:])
            # Pop stack & state by amount of rules in rhs
            for i in range(len(rhs)):
                stack.pop()
                state.pop()
            # Push grammar to state
            stack.append(lhs)
        # Case GOTO (Is Integer)
        elif (action.isnumeric()):
            # Add GOTO to state
            state.append(action)
    
        step+=1
        #if (len(input) < 1):
        #   break
        printCurrent(state,stack,input,action)
        
def main():
    with open("ParseTable/LR(1).csv", newline='') as csvfile:
        lr1 = csv.DictReader(csvfile)
        lr1Table = []
        for state in lr1:
            lr1Table.append(dict(state))
    
    #sampleTokens = 'INT ID SEMI INT ID SEMI ID ASSIGN ID PLUS INT_NUM SEMI RETURN SEMI EOF'
    #tokenList = splitSampleTokens(sampleTokens)
    
    tokenList = preprocess('LexerOutput/output1.txt')
    
    parseInput(tokenList, lr1Table)

if __name__ == "__main__":
    main()
# end main