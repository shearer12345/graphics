#What Is OpenGL?

- A real API
- There are a number of languages that have implemented it
    - but it all comes back to C in the end
   - and guess what language we’re running the course in?
- The API, in C, is defined by a number of `typedefs`, `#defined` enumerator values, and `functions`
    - `typedefs` define basic GL types like `GLint`, `GLfloat` and so forth
    - Complex aggregates like structs are never directly exposed in OpenGL

---

##C/C++ and OpenGL

```C
structObject{
    int anInteger;
    float aFloat;
    char *aString;
};

//Create the storage for the object.
ObjectnewObject;

//Put data into the object.
newObject.anInteger= 5;
newObject.aFloat= 0.4f;
newObject.aString= "Some String";
```

```C
//Create the storage for the object
GLuintobjectName;
glGenObject(1, &objectName);

//Put data into the object.
glBindObject(GL_MODIFY,objectName);
glObjectParameteri(GL_MODIFY, GL_OBJECT_AN_INTEGER, 5);
glObjectParameterf(GL_MODIFY, GL_OBJECT_A_FLOAT, 0.4f);
glObjectParameters(GL_MODIFY, GL_OBJECT_A_STRING, "Some String");
```

---

##Explaining C and OpenGL

```C
//Create the storage for the object
GLuintobjectName;
glGenObject(1, &objectName);

//Put data into the object.
glBindObject(GL_MODIFY,objectName);
glObjectParameteri(GL_MODIFY, GL_OBJECT_AN_INTEGER, 5);
glObjectParameterf(GL_MODIFY, GL_OBJECT_A_FLOAT, 0.4f);
glObjectParameters(GL_MODIFY, GL_OBJECT_A_STRING, "Some String");
```

- Not actual OpenGL commands but..
- OpenGL owns the storage for all OpenGL objects
    - the user can only access an object by reference.
    - almost all OpenGL objects are referred to by an unsigned integer (theGLuint)
        - ?? OMG !!

---

##Explaining C and OpenGL

```C
GLuintobjectName;
glGenObject(1, &objectName);

//Put data into the object.
glBindObject(GL_MODIFY,objectName);
glObjectParameteri(GL_MODIFY, GL_OBJECT_AN_INTEGER, 5);
glObjectParameterf(GL_MODIFY, GL_OBJECT_A_FLOAT, 0.4f);
glObjectParameters(GL_MODIFY, GL_OBJECT_A_STRING, "Some String");
```

- Objects are created by a function of the form`glGen*`, where * is the type of the object
- `glGen*(No.of objects to create)`
    - `GLuint*` array that receives the newly created object names

---

##Explaining C and OpenGL

```C
GLuintobjectName;
glGenObject(1, &objectName);

//Put data into the object.
glBindObject(GL_MODIFY,objectName);
glObjectParameteri(GL_MODIFY, GL_OBJECT_AN_INTEGER, 5);
glObjectParameterf(GL_MODIFY, GL_OBJECT_A_FLOAT, 0.4f);
glObjectParameters(GL_MODIFY, GL_OBJECT_A_STRING, "Some String");
```

- To modify most objects, they must first be **bound** to thecontext
- `GL_BindObject(Thefictitious targetisthelocation where, ObjectNameisbound)`
- Many objects can be bound to different locations in the context; this allows the same object to be used in different ways

---

##Explaining C and OpenGL

```C
GLuintobjectName;
glGenObject(1, &objectName);

//Put data into the object.
glBindObject(GL_MODIFY,objectName);
glObjectParameteri(GL_MODIFY, GL_OBJECT_AN_INTEGER, 5);
glObjectParameterf(GL_MODIFY, GL_OBJECT_A_FLOAT, 0.4f);
glObjectParameters(GL_MODIFY, GL_OBJECT_A_STRING, "Some String");
```

- Functions that actually change values within the object are given a target parameter, so that they could modify objects bound to different targets
- `glObjectParameterf(GL_MODIFY, An integer that points to an object, A new float value)`
- Note: All OpenGL objects are not as simple as this example, and the functions that change object state do **not all follow** these naming conventions

---

##The Structure of OpenGL

- The OpenGLAPI is defined as a statemachine
- Almost all of the OpenGL functions set or retrieve some state in OpenGL
    - the only functions that do not change state are functions that use the currently set state to cause rendering to happen
    - (*except a bunch of other functions that we'll pretend don't exist*)
- Think of the state machine as a very large `struct` with a great many different fields called the *OpenGL context*
    - each field in the context represents some information necessary for rendering

---

##The Structure of OpenGL

- Objects in OpenGL are thus defined as a list of fields in thisstructthat can be saved and restored
- Binding an object to a target within the context causes the data in this object to replace some of the context's state.
- Afterhe binding, future function calls that read from or modify this context state will read or modify the state within the object.

---

##Objects in OpenGL

```C
//Create the storage for the object
GLuintobjectName;
glGenObject(1, &objectName);

//Put data into the object.
glBindObject(GL_MODIFY,objectName);
glObjectParameteri(GL_MODIFY,GL_OBJECT_AN_INTEGER, 5);
glObjectParameterf(GL_MODIFY, GL_OBJECT_A_FLOAT, 0.4f);
glObjectParameters(GL_MODIFY, GL_OBJECT_A_STRING, "Some String");
```

- Objects are usually represented as `GLuint` integers
    - these are handles to the actual OpenGLobjects
- The integer value 0 is special; it acts as the object equivalent of a `NULL` pointer
    - binding object 0 means to unbind the currently boundobject
- This means that the original context state, the state that was in place before the binding took place, now becomes the context state

---

#The OpenGLSpecification

- the specification defines
    - the initial OpenGLstate
    - what each function does to change or retrieve it
    - what happens when you call a rendering function
- The most important thing to understand about the specification is it describes results, not implementation
- The specification is written by the OpenGL Architectural Review Board (ARB)
    - a group of representatives from companies like Apple, NVIDIA, and AMD (the ATI part), among others
    - The ARB is part of the **Khronos Group**

---

#The OpenGLSpecification

- The OpenGL ARB controls the specification, but it does not control OpenGL's code
- It is up to the developers of that hardware to write an OpenGL Implementation for that hardware
- Who controls the OpenGL implementation is different for different operatingsystems:
    - on Windows, OpenGL implementations are controlled virtually entirely by the hardware makers themselves
    - on Mac OSX, OpenGL implementations are controlled byApple
- The upshot of this is if you are writing a program and it seems to be exhibiting off-spec behaviour, the fault is with the maker of your OpenGL implementation

---

##And finally, just for fun...

- There are many versions of the OpenGL Specification
- OpenGL versions are not like most Direct3D versions, which typically change most of the API
- Code that works on one version of OpenGL will almost always work on later versions ofOpenGL





