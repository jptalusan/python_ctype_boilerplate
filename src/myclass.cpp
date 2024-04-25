#include "myclass.h"

// C++ class implementation
MyClass::MyClass(int initial_value) : _value(initial_value) {}
void MyClass::add(int value) { _value += value; }
int MyClass::get() const { return _value; }

extern "C" {

// C wrapper function implementations
MyClass* MyClass_new(int initial_value) { return new MyClass(initial_value); }
void MyClass_add(MyClass* obj, int value) { obj->add(value); }
int MyClass_get(const MyClass* obj) { return obj->get(); }
void MyClass_delete(MyClass* obj) { delete obj; }

}