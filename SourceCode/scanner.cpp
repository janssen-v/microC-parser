#include "scanner.hpp"

// Globals
std::string buffer;
std::string lookahead;
std::vector<std::string> tokens;

std::string getToken(std::string lexeme) {
    // Check if lexeme exists in tokenMap
    if (tokenMap.find(lexeme) != tokenMap.end()) {
        return tokenMap[lexeme];
    }
    // Check if lexeme are all integers
    for (int i = 0; i < lexeme.length(); i++) {
        if (!isdigit(lexeme[i])) {
            if (lexeme != " " && lexeme != "\t" && lexeme != "\n" && lexeme != "" && lexeme != "\0" && lexeme[0] != '\0'){
                return "ID";
            } else {
                return "";
            }
            break;
        }
    }
    // Else return INT
    if (lexeme != " " && lexeme != "\t" && lexeme != "\n" && lexeme != "" && lexeme != "\0" && lexeme[0] != '\0'){
        return "INT_NUM";
    } else {
        return "";
    }
    //return "INT_NUM";
}

// Scan line for tokens
void scanLine(std::string line)
{
    for (int i = 0; i<=line.length(); i++) {
        // readout buffer
        std::string readout = buffer;
        char c = '\0';
        if (i < line.length()) {
            c = line[i];
        }
        char n;
        char p;
        // Set lookahead value if it exists
        if (i+1 < line.length()) {
            n = line[i+1];
        } else {
            n = '\0';
        }
        // Set lookbehind value if it exists
        if (i-1 >= 0) {
            p = line[i-1];
        } else {
            p = '\0';
        }
        
        if (isalnum(c) || c == '_'){
            // Keyword, INT, or ID
            if (c!= '\n' && c != '\t' && c != ' '){
                buffer.append(1,c);
            }

        } else { 
            // Is space, newline, tab, or special symbol

            // If current char is space, newline, tab, or previous tab is alphanumeric (and current is not), flush buffer
            if (isspace(c) || c == '\n' || c == '\t' || isalnum(p) || c == '_' && (!isalnum(c) && c != '_')) { 
                // tokenise and flush buffer if not empty since spaces always terminal
                if (buffer != "") {
                    std::string tok = getToken(buffer);
                    buffer.clear();
                    // print token
                    if (tok != "") {tokens.push_back(tok);}
                }
                //std::string tok = getToken (buffer);
                //buffer.clear();
            //    if (c!= '\n' && c != '\t' && c != ' '){
            //        buffer.append(1,c);
            //    }
                // print token
                //if (tok != "") {tokens.push_back(tok);}

            // Is special symbol
            } 
            //else { // This else can be removed i think
                // Is nonterminal symbol
                if (c == '<' || c == '>' || c == '=' || c == '!' || c == '&' || c == '|') {
                    // Check for if c and n are terminal when combined
                    buffer.append(1,c);
                    std::string tok;
                    if (n != ' ') {
                        lookahead.append(1,n);
                        tok = getToken(buffer+lookahead);                        
                    } else {
                        tok = getToken(buffer);
                    }
                    if (tok != "INT_NUM" && tok != "ID") {
                        // advance i since we already checked n
                        i++; 
                    } else {
                        // Single symbol, always terminal, no lookahead, tokenize and flush
                        tok = getToken(buffer);
                    }
                    buffer.clear();
                    lookahead.clear();
                    // print token
                    if (tok != "") {tokens.push_back(tok);}

                } else { // Is terminal symbol
                // Single symbol, always terminal, no lookahead, add and flush
                    buffer.append(1, c);
                    std::string tok = getToken(buffer);
                    buffer.clear();
                    // print token
                    if (tok != "") {tokens.push_back(tok);}

                }
            //}
        }
        // check if buffer is a symbol, and if it is terminal then flush
        if (!isalnum(buffer[0])){
            if (buffer != "&" || buffer != "|" || buffer != "!" || buffer != "=" || buffer != "<" || buffer != ">" || buffer != "") {
            std::string tok = getToken(buffer);
            buffer.clear();
            // print token
            if (tok != "") {tokens.push_back(tok);}
            }
        }
        
    }
    
}

int main(int argc, char const *argv[])
{
    if (argc < 2)
    {
        std::cout << "Error: No file specified" << std::endl;
        return 1;
    } else if (argc > 2)
    {
        std::cout << "Error: Too many arguments" << std::endl;
        return 1;
    }
    // open file
    std::ifstream file(argv[1]);
    // check if file is open
    if (!file.is_open())
    {
        std::cout << "Error: File not found" << std::endl;
        return 1;
    }
    // read file
    std::string line;
    while (std::getline(file, line))
    {
        //std::cout << line << std::endl;
        scanLine(line);
        for (int i = 0; i < tokens.size(); i++) {
            std::cout << "Token: " << tokens[i] << std::endl;
        }
        tokens.clear();
    }
    // close file



    return 0;
}
