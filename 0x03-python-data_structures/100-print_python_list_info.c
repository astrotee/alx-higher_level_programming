#include "Python.h"

/**
* print_python_list_info - print info about a list object
* @p: a pointer to the object
* Return: nothing
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	PyObject *item;
	Py_ssize_t i;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)(p))->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}

}
