#Lincoln Graphics Workshop 02

- HelloTriangle
- source for examples:

https://github.com/shearer12345/graphics_examples_in_git_branches

```bash
git checkout glTriangle ##the glTriangle example - a helloTriangle
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
    - https://github.com/shearer12345/graphics_examples_in_git_branches

```bash
git stash save WhatEverStashNameYouLike #OPTIONAL: save any changes you may have made
git checkout master #make sure you're on the master branch
git pull #pull remote master locally
python .\branchAndTrack.py #run branchAndTrack to update all branches
##or
py .\branchAndTrack.py #if in Lincoln Lab A
```

---

##Run the examples

- checkout the following examples and run each
    - using build system of your choice
    - assuming Visual Studio here
```bash
git checkout EXAMPLE ##checkout example from the repository
.\premake4 vs2012
#load in Visual Studio
#build in Visual Studio
#run in Visual Studio
```
    1) glIncluded
    2)

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
git diff master sdlCreateContext .\main.cpp
```

---

##Activities

- You should try to **all of these** today. Work on them in your free-study time if you need
- Don't change the GLSL shaders to do this - that's for later!

1) make the background color something different
2) make the triangle a different shape
3) make the triangle appear somewhere else on the screen, but the original shape
    - this is a **translation**
4) make the triangle larger than the original, but still similar
    - http://www.mathsisfun.com/geometry/triangles-similar.html
    - don't rotate it, only change the size
    - this is a **scale**
5) make the triangle **translate** or **scale** over time
    - you'll need to add a loop to the main function

---

##Stretch Activities

- If you've got through the standard activities then have a bash at these

1) make the triangle be in a rotated position
    - this is **rotation**
2) make the triangle rotate over time
3) make the triangle translate **and** scale, over time
4) make the triangle translate **and** rotate, over time!!!!!!!!!!
