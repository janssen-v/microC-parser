# CSC 4180 Project 3: Parser
Copyright ©2023 by Vincentius Janssen (119010518)

Made in fulfilment of the requirements of the course CSC 4180: Compiler Construction at the Chinese University of Hong Kong, Shenzhen

## How to run
1. `cd` into the `SourceCode` directory
2. `make build` to build the scanner
3. `chmod +x run_parser.sh` to activate the script
4. `./run_parser.sh <input file>` to run the `<input file>` through the scanner and parser.
5. The scanner output will be piped into `scanned.txt`, which will be used as input for the parser.
6. The parser output will be printed to console and saved to `parsed.txt`, since it might be too long to view in the console.
