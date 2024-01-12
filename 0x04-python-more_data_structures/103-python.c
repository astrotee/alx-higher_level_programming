#include "Python.h"
#include "bytesobject.h"
#include <stdio.h>

/**
* print_python_bytes - print info about a bytes object
* @p: a pointer to the object
* Return: nothing
*/
void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	int bytes = size < 10 ? size + 1 : 10;
	int i;

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %d bytes:", bytes);

	for (i = 0; i < bytes; i++)
		printf(" %02x", (char)((PyBytesObject *)p)->ob_sval[i] & 0xff);
	printf("\n");
}

/**
* print_python_list - print info about a list object
* @p: a pointer to the object
* Return: nothing
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyObject *item;
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)(p))->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, (item->ob_type)->tp_name);
		if (PyBytes_CheckExact(item))
			print_python_bytes(item);
	}

}
