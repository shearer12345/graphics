#Lincoln Graphics Workshop 02

- HelloTriangle

---

##glTriangleWhite

![glTriangleWhite](assets/examples/glTriangleWhite.png)

---

##Source and checkout

- source for examples:

https://github.com/shearer12345/graphics_examples_in_git_branches

```bash
git checkout glTriangleWhite ##the glTriangle example - a helloTriangle
```

#A heads-up

- The helloTriangle for modern OpenGL is **COMPLEX**
- It has a number of stages all of which must work in order to display **anything!**
- We'll go through the code in classes
    - but you'll want to work through each step and figure them out for yourself
    - likely you'll want to come back to this simple example
    - there are **lots** of new terms here, we'll cover them more later
    - the code will have some **sign-posts** where you might want to make changes/additions for the activities

---

##Preparatory stages to get a single Triangle!!

- This won't draw **anything** without the **loop** stages

1) Create a **Window** and a **GL context**
2) Load **GLSL shaders**
3) Link GLSL shaders in to **GLSL programs**
4) Create/Load **Geometry data** (vertices) CPU-side
5) Load **Geometry** data into OpenGL
6) Create **Vertex Array Objects**

---

##Loop stages to get a single Triangle!!

1) Clear the **Back Buffer**
2) Tell OpenGL to use a **GLSL program** that has already been created
3) Tell OpenGL to use some **geometry data** that has already been loaded
4) Tell OpenGL where in the **GLSL program** to put the **geometry data**
5) Tell OpenGL what format the **geometry data** is in - how it is stored / how to read it
6) Tell OpenGL to draw some type of **Primitive**, using some number of **Vertices**
7) Clean up some OpenGL stuff
8) Tell SDL to swap the **Back Buffer** and the **Front Buffer**

---

##Update the examples

- You should update all the examples from the git repository
    - or delete the examples directory and start again
    - the README for starting again is at:
    - [https://github.com/shearer12345/graphics_examples_in_git_branches](https://github.com/shearer12345/graphics_examples_in_git_branches)

```bash
#OPTIONAL: save any changes you may have made
git stash save WhatEverStashNameYouLike 

#TO UPDATE your local repository
git checkout master #make sure you're on the master branch
git pull #pull remote master locally
python .\branchAndTrack.py #run branchAndTrack to update all branches
##or
py .\branchAndTrack.py #if in Lincoln Lab A
```

---

##Run the examples

- checkout the examples following (next page) and run each
    - using build system of your choice
    - assuming Visual Studio here
```bash
git checkout EXAMPLE ##checkout example from the repository
.\premake4 vs2012
#load in Visual Studio
#build in Visual Studio
#run in Visual Studio
```

- Note that you each time you checkout a new example, you should re-run premake.
    - Visual Studio will detect this and ask if you want to reload the solution - say YES
    - If you using VS2013, you may need to right-click the solution and hit "re-target"
    - If you using VS2013, you may need to right-click the project ahd hit "Set As Startup Project"

---

###Examples to look through

1) glGlew
    - include the GLEW library, make SDL create an OpenGL context. **important changes here**
2) glCreateShadersAndProgram
    - load some GLSL shaders into OpenGL, compile and link them. **new stuff here**
3) glGenVertexBuffer
    - load some vertex data into OpenGL. **more new stuff here**
4) glTriangleWhite
    - this one is the first time you'll see anything rendered
    - **yet more new stuff here**
    - this one is the one to do the activities (later) on

---

##Diff the examples

- look at what's different between the examples
```bash
git diff EXAMPLE1 EXAMPLE2 ##will produce the **diff** for all files
```
- you can also diff just a single file
```bash
git diff EXAMPLE1 EXAMPLE2 .\fileName
##for example
git diff sdlHelloWorldWithFunctions glGlew .\main.cpp
```

---

##Activities

- You should try to **all of these** today. Work on them in your free-study time if you need
- Don't change the GLSL shaders to do this - that's for later!
- There are 5 main activities and 4 stretch activities
- If you want to make each of these activities as a separate `git branch` you can
    - if you fork my repo on github, and upload your own branches
    - then you can send pull requests - for feedback and as **student as producer**

---

##Activity 1 - make the background color something different

![glTriangleWhiteOnRedBackground](assets/examples/glTriangleWhiteOnRedBackground.png)

---

##Activity 2 - make the triangle a different shape

![glTriangleWhiteDifferentShape](assets/examples/glTriangleWhiteDifferentShape.png)

---

##Activity 3 - make the triangle appear somewhere else on the screen, but the original shape
- this is a **translation**

![glTriangleWhiteCPUTranslation](assets/examples/glTriangleWhiteCPUTranslation.png)

---

##Activity 4 - make the triangle larger than the original

- but still similar (the same shape)
- this is a **scale**

![glTriangleWhiteCPUScale](assets/examples/glTriangleWhiteCPUScale.png)

---

##Activity 5 - make the triangle **translate** or **scale** over time

- you'll need to add a loop to the main function
- you'll need to do quite a number of other things also
    - specifically, look at the `glBufferData` function

![glTriangleWhiteTranslationOverTimeAnimated](assets/examples/glTriangleWhiteTranslationOverTimeAnimated.gif)

---

##Stretch Activities

- If you've got through the standard activities then have a bash at these

1) make the triangle be in a rotated position
    - this is **rotation**
2) make the triangle rotate over time
3) make the triangle translate **and** scale, over time
4) make the triangle translate **and** rotate, over time!!!!!!!!!!
