import csv

grammarfile = open("grammartest.txt", "r")
gramload = grammarfile.read()
grammar = gramload.split("\n")

# grammar = ["S' -> S",
#            "S -> C C",
#            "C -> c C",
#            "C -> d"]

# Turns a string of tokens into a list of tokens
def splitTokens(tokenString):
    return tokenString.strip().split()

def getGrammar(rule):
    # Convert Production Rule
    prod = grammar[int(rule)].split('->')
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


        print("State:", state)
        print("S:", step, "Stack:", stack, "Input:", input, "Action:", action)
        print()
        
        if (step > 11):
            break
        
        # Make case for empty '' action 
        # Case SHIFT
        if ('s' in action):
            state.append(action[-1])
            stack.append(input.pop(0))
        # Case REDUCE
        elif ('r' in action):
            # Reduce by grammar action[-1]
            lhs, rhs = getGrammar(action[1:])
            # Pop stack & state by amount of rules in rhs
            for i in range(len(rhs)):
                stack.pop()
                state.pop()
            # Push grammar to state
            stack.append(lhs)
        # Case SHIFT/REDUCE Conflict
            # Shift by Default
        # Case ACCEPT
        elif (action == ''):
            print('Empty')
        # Case GOTO
        elif (int(action)):
            # Add GOTO to state
            state.append(action)
    
        step+=1
        #if (len(input) < 1):
        #   break
        
def main():
    with open("/Users/vincent/Documents/Microsoft Office/LR(1)test.csv", newline='') as csvfile:
        lr1 = csv.DictReader(csvfile)
        lr1Table = []
        for state in lr1:
            lr1Table.append(dict(state))
    
    sampleTokens = 'c d d'
    tokenList = splitTokens(sampleTokens)
    
    parseInput(tokenList, lr1Table)

if __name__ == "__main__":
    #print(table[0]["c"])
    main()
# end main