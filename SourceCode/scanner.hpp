#include <string>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>


// Reserved Words (Keywords)
std::string reservedWords[] = {
    "int",
    "main",
    "void",
    "break",
    "do",
    "else",
    "if",
    "while",
    "return",
    "scanf",
    "printf"
};  

// Special Symbols
std::string specialSymbols[] = {
    "{",
    "}",
    "(",
    ")",
    "[",
    "]",
    ";",
    "+",
    "-",
    "*",
    "/",
    "&", // nt -> &&
    "|", // nt -> ||
    "!", // nt -> !=
    "=", // nt -> ==
    "<", // nt -> <=
    ">", // nt -> >=
    "<<",
    ">>",
    "==",
    "!=",
    "<=",
    ">=",
    "&&",
    "||",
    ",",
};

std::unordered_map<std::string, std::string> tokenMap = { 
    {"int", "INT"},
    {"main", "MAIN"},
    {"void", "VOID"},
    {"break", "BREAK"},
    {"do", "DO"},
    {"else", "ELSE"},
    {"if", "IF"},
    {"while", "WHILE"},
    {"return", "RETURN"},
    {"scanf", "READ"},
    {"printf", "WRITE"},
    {"{", "LBRACE"},
    {"}", "RBRACE"},
    {"(", "LPAR"},
    {")", "RPAR"},
    {"[", "LSQUARE"},
    {"]", "RSQUARE"},
    {";", "SEMI"},
    {"+", "PLUS"},
    {"-", "MINUS"},
    {"*", "MUL_OP"},
    {"/", "DIV_OP"},
    {"&", "AND_OP"},
    {"|", "OR_OP"},
    {"!", "NOT_OP"},
    {"=", "ASSIGN"},
    {"<", "LT"},
    {">", "GT"},
    {"<<", "SHL_OP"},
    {">>", "SHR_OP"},
    {"==", "EQ"},
    {"!=", "NOTEQ"},
    {"<=", "LTEQ"},
    {">=", "GTEQ"},
    {"&&", "ANDAND"},
    {"||", "OROR"},
    {",", "COMMA"}
};