#include <iostream>
#include <Python.h>
#pragma comment(lib, "python311.lib")
extern "C" {
    PyObject* add(PyObject* self, PyObject* args) {
        int a, b;
        if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
            return NULL;
        }
        int result = a + b;
        return PyLong_FromLong(result);
    }
}
static PyMethodDef myModuleMethods[] = {
    {"add", add, METH_VARARGS, "Add two integers."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",
    NULL,
    -1,
    myModuleMethods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&myModule);
}
