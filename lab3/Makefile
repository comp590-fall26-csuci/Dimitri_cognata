all:
	gcc 590MakefileLab/main.c 590MakefileLab/fibonacci.c -I590MakefileLab/headers -lm -o fibonacci 

run: 
	./fibonacci

test:
	gcc test_fib.c 590MakefileLab/fibonacci.c -Iheaders -I590MakefileLab/headers -lm -o test_fib
	./test_fib

clean:
	rm -f fibonacci test_fib  
