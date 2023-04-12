# Specify compiler to be used
CXX = g++
CXXFLAGS += -g -std=c++17

all:
	make activate_script
	make clean
	make build

activate_script:
	chmod +x run_parser.sh

build:
	@echo "Building..."
	g++ -std=c++17 -o scanner scanner.cpp

run:
	@echo "Running..."
	mkdir -p LexerOutput
	./scanner TestCases/test1.c1 > LexerOutput/output1.txt
	./scanner TestCases/test2.c1 > LexerOutput/output2.txt
	./scanner TestCases/test3.c1 > LexerOutput/output3.txt
	./scanner TestCases/test4.c1 > LexerOutput/output4.txt
	./scanner TestCases/test5.c1 > LexerOutput/output5.txt

clean:
	@echo "Cleaning..."
	rm -f scanner
	rm -f scanned.txt
	rm -f prased.txt
	rm -rf LexerOutput