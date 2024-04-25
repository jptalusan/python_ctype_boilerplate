#ifndef MY_CLASS_H
#define MY_CLASS_H

// The C++ class you want to interact with from Python.
class MyClass {
public:
    MyClass(int initial_value);
    void add(int value);
    int get() const;

private:
    int _value;
};

// C wrapper functions
#ifdef __cplusplus
extern "C" {
#endif

MyClass* MyClass_new(int initial_value);
void MyClass_add(MyClass* obj, int value);
int MyClass_get(const MyClass* obj);
void MyClass_delete(MyClass* obj);

#ifdef __cplusplus
}
#endif

#endif // MY_CLASS_H