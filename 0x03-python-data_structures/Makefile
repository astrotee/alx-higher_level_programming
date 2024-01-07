all: palindrome libPyList.so

palindrome: 13-main.c linked_lists.c 13-is_palindrome.c
	gcc -Wall -Werror -Wextra -pedantic $^ -o $@ -g

libPyList.so: 100-print_python_list_info.c
	gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o $@ -fPIC -I/usr/include/python3.8 $^ -g

