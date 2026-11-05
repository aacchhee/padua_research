/* Exact CPython integer endpoint loop; no machine-width endpoint arithmetic. */
#define PY_SSIZE_T_CLEAN
#include <Python.h>

/* Accept exact tuples/lists and exact integers only. */
static int sequence(PyObject *v) { return PyTuple_CheckExact(v) || PyList_CheckExact(v); }
static PyObject *item(PyObject *v, Py_ssize_t i) {
    return PyTuple_CheckExact(v) ? PyTuple_GET_ITEM(v, i) : PyList_GET_ITEM(v, i);
}
static int interval(PyObject *v) {
    return sequence(v) && PySequence_Size(v)==2 && PyLong_CheckExact(item(v,0)) && PyLong_CheckExact(item(v,1));
}
static PyObject *accumulate(PyObject *self, PyObject *args) {
    PyObject *terms,*table,*unit,*lo=NULL,*hi=NULL;
    PyObject *p[4]={NULL,NULL,NULL,NULL}, *floor=NULL,*neg=NULL,*q=NULL,*ceil=NULL,*next=NULL;
    if (!PyArg_ParseTuple(args,"OOO",&terms,&table,&unit)) return NULL;
    if (!sequence(terms) || !sequence(table) || !PyLong_CheckExact(unit)) goto bad;
    /* The Python factory pins its scale; this exact primitive supports controls
       at historical n4--7 scales as well. Reject zero/negative divisors. */
    PyObject *zero=PyLong_FromLong(0);
    if(!zero)return NULL;
    int positive=PyObject_RichCompareBool(unit,zero,Py_GT);Py_DECREF(zero);
    if(positive<0)return NULL;
    if(!positive)goto bad;
    lo=PyLong_FromLong(0); hi=PyLong_FromLong(0);
    if(!lo || !hi)goto fail;
    for(Py_ssize_t k=0;k<PySequence_Size(terms);k++) {
        PyObject *term=item(terms,k);
        if(!sequence(term) || PySequence_Size(term)!=3)goto bad;
        PyObject *ii=item(term,0),*jj=item(term,1),*c=item(term,2);
        if(!PyLong_CheckExact(ii)||!PyLong_CheckExact(jj)||!interval(c))goto bad;
        Py_ssize_t i=PyLong_AsSsize_t(ii),j=PyLong_AsSsize_t(jj);
        if(PyErr_Occurred())goto fail;
        if(i<0||j<0||i>=PySequence_Size(table))goto bad;
        PyObject *row=item(table,i);
        if(!sequence(row)||j>=PySequence_Size(row))goto bad;
        PyObject *m=item(row,j);
        if(!interval(m))goto bad;
        /* Preserve frozen multiplication order c0*m0,c0*m1,c1*m0,c1*m1. */
        for(int a=0;a<4;a++) {
            p[a]=PyNumber_Multiply(item(c,a/2),item(m,a%2));
            if(!p[a])goto fail;
        }
        PyObject *minimum=p[0],*maximum=p[0];
        for(int a=1;a<4;a++) {
            int less=PyObject_RichCompareBool(p[a],minimum,Py_LT);
            if(less<0)goto fail;
            if(less)minimum=p[a];
            int greater=PyObject_RichCompareBool(p[a],maximum,Py_GT);
            if(greater<0)goto fail;
            if(greater)maximum=p[a];
        }
        floor=PyNumber_FloorDivide(minimum,unit);
        neg=PyNumber_Negative(maximum);
        if(!floor||!neg)goto fail;
        q=PyNumber_FloorDivide(neg,unit); if(!q)goto fail;
        ceil=PyNumber_Negative(q); if(!ceil)goto fail;
        next=PyNumber_Add(lo,floor); if(!next)goto fail;
        Py_SETREF(lo,next);next=NULL;
        next=PyNumber_Add(hi,ceil); if(!next)goto fail;
        Py_SETREF(hi,next);next=NULL;
        for(int a=0;a<4;a++)Py_CLEAR(p[a]);
        Py_CLEAR(floor);Py_CLEAR(neg);Py_CLEAR(q);Py_CLEAR(ceil);
    }
    { PyObject *result=PyTuple_Pack(2,lo,hi);Py_DECREF(lo);Py_DECREF(hi);return result; }
bad:
    PyErr_SetString(PyExc_ValueError,"expected exact integer terms/table with positive scale and valid indices");
fail:
    for(int a=0;a<4;a++)Py_XDECREF(p[a]);
    Py_XDECREF(floor);Py_XDECREF(neg);Py_XDECREF(q);Py_XDECREF(ceil);Py_XDECREF(next);
    Py_XDECREF(lo);Py_XDECREF(hi);return NULL;
}
static PyMethodDef methods[]={{"accumulate",accumulate,METH_VARARGS,"Ordered exact endpoint sum."},{NULL,NULL,0,NULL}};
static struct PyModuleDef module={PyModuleDef_HEAD_INIT,"_t1_native",NULL,-1,methods};
PyMODINIT_FUNC PyInit__t1_native(void){return PyModule_Create(&module);}
