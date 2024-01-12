all: libPython.so


libPython.so: 103-python.c
	gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o $@ -fPIC -I/usr/include/python3.8 $^ -g

