#Lincoln Graphics Coursework Assignment 2014-15 (Resit)

##Overview

**RESIT**

- The coursework assignment is be based around developing an interactive 3D scenario
    - this year, a walk-through of a 3D University Campus
- The assignment aims to assess practical capability in writing programs that:
  - generate 3D graphics
  - update the 3D scene based on human input (i.e. interactive 3D graphics)
- The specific assignment and its requirements are detailed below
  - the marking scheme is separately in the [Criterion Reference Grid](lincolnAssignmentResitCRG.html)

##Graphics Features - summary

The assignment will use the modern programmable graphics pipeline (e.g. OpenGL 3.1+) and will require a set of basic 3D graphics features, such as:

- 3D geometry
- 3D (perspective) projections
- moving/rotating objects
- moving/rotating view points
- coloured objects, along with a set of advanced features, such as lighting simulation
- texturing

##Primacy of CRG

- The CRG provides **most** of the detail for the coursework
- The specific is only the general outline
- You should view the CRG **literally**
    - It **is** the mark scheme
    - you should be able to *more-or-less* mark your assignment yourself
        - to have a good idea of what mark you'll likely achieve
- You should view the CRG **cynically**
    - for instance, the CRG says **nothing** about the consistency of the concept
        - i.e. the scene **doesn't have to make sense**
        - it can be a collection of graphical objects that meet the CRG

##Specification

- You should implement a walk-through of a 3D University Campus
- The specific geometry (shapes) that you use are not defined - they are up to you
- Your scene should contain the following
    - some kind of terrain/land - e.g. fields, mountains, pool
    - some kind of 2D content in the scene
        - e.g. some triangles
    - some kind of 3D vehicle
        - e.g. car, helicopter
    - the 3D vehicle can be moved by the user
    - other 3D objects of your choice to fulfil the CRG
    - other features to fulfil the CRG
- Note that 3D objects are **solid** 3D objects (e.g. cube)
    - not just triangles in 3-space

##Documentation

- summary document of features implemented
- reflection on the development process
- at least one screenshot of your assignment running
- see CRG

##Languages / Toolkit (what you can use)

- You can use any programming language that your choose
    - the in-class content has all been C++, but you don't have to follow this
    - BUT, if not using C++ you will need to support yourself significantly more
- You **MUST** makes the call into OpenGL yourself
- You **CAN** use appropriate support libraries (but can use alternates if you choose), such as:
    - SDL2
    - GLEW
    - GLM
- If in doubt - **ASK**
    - fundamentally, you should be writing the code that makes OpenGL calls, such as `glCreateShader()`

##Languages / Toolkit (what you cannot use)

- You **CANNOT** use a graphics engine (e.g. Ogre3D, Irrlicht, Three.js)
- You **CANNOT** use a games engine (e.g. Unity)
- If using C++, you **CANNOT** use an existing object-oriented wrapper (e.g. oglplus)
    - but you can write and use your own if you like ...
- If in doubt - **ASK**
    - fundamentally, you should be writing the code that makes OpenGL calls, such as `glCreateShader()`

##Submission

- Submit to Blackboard
- A single **.zip** file containing:
    - all your C++ source code
    - all your shader source code (if not in your C++ source)
    - files sufficient to create a working build environment (e.g. premake files, or just visual studio files)
    - all your assets (textures)
    - a compiled, running executable (it doesn't need to be able to run outside the IDE)
    - your documentation, as PDF

##Assessment

- The assignment will be assessed through a Blackboard download
  - it is therefore important that your submission includes the executable and all dependencies, and that it can be build/rebuilt.
  - your coursework will be tested on a machine equivalent to those it Lab A

##Feedback

- you will receive written feedback on Blackboard

##Optional Video

- You may **optionally** create a video of your assignment
- This would be valuable to yourself as portfolio work
- This would be valuable to the School
    - to illustrate to students in following years what they'll be doing in the module
    - to enhance recruitment and visibility of the School
    - to support external examiners in seeing what your assignment looked like, without having to run code

##CRG

- The CRG is in a separate document
  - [Assignment CRG](lincolnAssignmentCRG.html)
