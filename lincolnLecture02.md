
---
title: lincoln Lectures On Graphics - 02
author: shearer12345
---


---
title: Graphics Assessment
author: shearer12345
---

#Assessment Methods and Weighting

- Assignment (Coursework)
    - weighting = 70%
- Exam (Closed-book)
    - weighting = 30%

- From the Module Specification - Graphics 2015-16
    - Blackboard=>Graphics (CGP2012M)->About this module

---

##Learning Outcomes

- Both assessments assess both Learning Outcomes
- Learning Outcome 1

    > design and develop interactive 3D graphics software, applying appropriate mathematical/algorithmic techniques for efficient 2D and 3D graphics
- Learning Outcome 2

    > Demonstrate deep understanding of computer graphics programming techniques and approaches
- Both are *individually* assessed

---

##What to expect in the assignment

- based around developing an interactive 3D scenario
    - such as a simple computer game:
        - Pong
        - Space Invaders
        - Virtual plane

- will submit to blackboard, but live-demo in the following workshop, affording:
    - faster mark turn around
    - immediate verbal feedback
    - written feedback with mark release
    - opportunity to ask questions

---

##What features in the assignment will be assessed

- aims to assess practical capability in writing programs that generate 3D graphics and updating the 3D scene based on human input
- requires a set of basic 3D graphics features, such as:
    - 3D geometry
    - 3D (perspective) projections
    - moving/rotating objects
    - moving/rotating view points
    - coloured objects
    - advanced features, such as:
        - lighting simulation
        - texturing.

---

##What to expect on the Exam

- will assess the more theorectical side of computer graphics
- wider understanding of the area
- questions on the following would be appropriate (examplar, other questions could occur):
    - how standard algorithms or techniques work
    - the factors that affect the performance of graphical systems
    - writing graphics "shaders" from scratch
    - or critique/modify/correct provided "shaders"

#Recommended Reading for Graphics

- Learning Modern 3D Graphics Programming by Jason L. McKesson
  - http://www.arcsynthesis.org/gltut/
#It's Triangles All The Way Down

- Remember: Everything is a shell
- All of these shells are made of triangles
- Even surfaces that appear to be round are merely triangles if you look closely enough
- There are techniques that generate more triangles for objects that appear closer or larger, so that the viewer can almost never see the faceted silhouette of the object, but they are always made of triangles
- Note: Some rasterizers use planar quadrilaterals: four-sided objects, where all of the lines lie in the same plane. One of the reasons that hardware-based rasterizers always use triangles is that all of the lines of a triangle are guaranteed to be in the same plane. Knowing this makes the rasterization process less complicated.

![triangle](assets\triangle.png)

#Objects

- An object is made out of a collection of adjacent triangles that define the outer surface of the object
- Such a collection of triangles is often called:
    - a model
    - a mesh
    - geometry
    - **these terms are used interchangeably**

#Pipeline

- Rasterization has several phases ordered into a pipeline
- triangles enter from the left and a 2D image is filled in at the right
- A pipeline is very ammeneable to hardware acceleration
- it operates on each triangle one at a time, in a specific order
- triangles can be fed into the left of the pipeline while triangles that were sent earlier can still be in some phase of rasterization.

---

##OpenGL Pipeline

![http://goanna.cs.rmit.edu.au/~gl/teaching/Interactive3D/2011/lecture2.html](assets\pipeline01.png)

---

##Raster Ordering

- The order in which triangles and the various meshes are submitted to the rasterizer can affect its output
    - (if you are doing fancy stuff)
- No matter how you submit the triangular mesh data, the rasterizer will process each triangle in a specific order:
    - drawing the next one only when the previous triangle has finished being drawn

---

##Triangles and Vertices (in OpenGL)

- Triangles consist of 3 vertices
    - A vertex is a collection of arbitrary data
    - ???!!!???
    - For the sake of simplicity, in our context this data must contain a point in three dimensional space - it may contain other data (e.g. colour)
- Any 3 points that are not on the same line create a triangle
    - A triangle is defined by exactly 3 (three-dimensional) points - (X, Y, Z)


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





