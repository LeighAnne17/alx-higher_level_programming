#include <Python.h>

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size < 10 ? size + 1 : 10);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02hhx", str[i]);
        if (i + 1 < size && i + 1 < 10)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_list - Prints information about Python list objects
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: ", i);
        if (PyBytes_Check(item))
            printf("bytes\n");
        else if (PyFloat_Check(item))
            printf("float\n");
        else if (PyList_Check(item))
            printf("list\n");
        else
            printf("%s\n", Py_TYPE(item)->tp_name);
    }
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    printf("  value: %.*g\n", 16, value);
}

