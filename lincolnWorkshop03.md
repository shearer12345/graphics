#Lincoln Graphics Workshop 03 - HelloGLSL

##glTriangleWhite

![glTriangleWhite](assets/examples/glTriangleWhite.png)

##Source and checkout

- source for examples:

https://github.com/shearer12345/graphics_examples_in_git_branches

```bash
git checkout glTriangleWhite ##the glTriangle example - a helloTriangle
```

#Strangely Familiar ...

##Strangely Familiar ...

- Activities are mainly the same as Workshop 02
- but you'll be doing the **transformations** in **GLSL**
    - so they'll run on the GPU, rather than the CPU
    - which makes debugging a challenge

#What Is GLSL?

##What Is GLSL?

- a high-level shading language
- based on the syntax of the C programming language
    - importantly **different** from C
- https://www.opengl.org/documentation/glsl/

##GLSL and the OpenGL pipeline

- GLSL is how you **program** the OpenGL pipeline
    - for the DirectX pipeline you use HLSL
    - there are other tools also
- GLSL programs are compiled at **run-time**
    - by **your** program
    - you've already been **unknowingly** doing this ...
- GLSL programs are also called **shaders**

##GLSL and the OpenGL pipeline 2

- GLSL programs run in very **specific** points in the OpenGL pipeline
- Each point in the pipeline takes a different **type** of GLSL program
    - what **types** of GLSL programs are there
    - **where** (in the pipeline) does each run?
    - what are the **inputs** and **outputs** of each?

##The inescapable GLSL

- Modern OpenGL (i.e. 3.0 upwards) **REQUIRES** you to use **GLSL programs**
- You **must** provide at least one **vertex program** and one **fragment program**

#Version fun ;-)

##Version fun ;-)

- Just like OpenGL there are many versions of GLSL
- You have to match your GLSL version to your OpenGL version
    - i.e. if you create an OpenGL 3.3 context then you **must** use GLSL 3.3
        - for *limited* values of *must*. Some drivers are quite tolerant

##GL vs GLSL version numbering

> GLSL versions have evolved alongside specific versions of the OpenGL API.
> It is only with OpenGL versions 3.3 and above that the GLSL and OpenGL major and minor version numbers match.
> These versions for GLSL and OpenGL are related in the following table.

    - http://en.wikipedia.org/wiki/OpenGL_Shading_Language#Versions

##

| GLSL Version | OpenGL Version | Date           | Shader Preprocessor |
|--------------|----------------|----------------|---------------------|
| 1.10.59      | 2.0            | April 2004     | #version 110        |
| 1.20.8       | 2.1            | September 2006 | #version 120        |
| 1.30.10      | 3.0            | August 2008    | #version 130        |
| **1.40.08**  | **3.1**        | March 2009     | **#version 140**    |
| 1.50.11      | 3.2            | August 2009    | #version 150        |
| 3.30.6       | 3.3            | February 2010  | #version 330        |
| 4.00.9       | 4.0            | March 2010     | #version 400        |
| 4.10.6       | 4.1            | July 2010      | #version 410        |
| 4.20.11      | 4.2            | August 2011    | #version 420        |
| 4.30.8       | 4.3            | August 2012    | #version 430        |
| 4.40         | 4.4            | July 2013      | #version 440        |
| 4.50         | 4.5            | August 2014    | #version 450        |

http://en.wikipedia.org/wiki/OpenGL_Shading_Language#Versions




#Debugging GLSL

##Debugging GLSL

- GLSL is compiled at run-time, from your code
- Your program can obtain compile errors for the GLSL compiler
- Sometimes using debugging tools for GLSL can be helpful - see tools (later)

##Debugging GLSL Tools

- Apitrace [http://apitrace.github.io/](http://apitrace.github.io/)
- synthclipse [http://devmaster.net/p/24392/synthclipse-open-source-glsl-shader-prototyping-tool-based-on-eclipse-ide](http://devmaster.net/p/24392/synthclipse-open-source-glsl-shader-prototyping-tool-based-on-eclipse-ide)
- GLSL-Debugger [https://github.com/GLSL-Debugger/GLSL-Debugger](https://github.com/GLSL-Debugger/GLSL-Debugger)
- shdr [http://bkcore.com/blog/3d/shdr-online-glsl-shader-editor-viewer-validator.html](http://bkcore.com/blog/3d/shdr-online-glsl-shader-editor-viewer-validator.html)
- VOGL [https://github.com/ValveSoftware/vogl](https://github.com/ValveSoftware/vogl)
- GLIntercept [https://code.google.com/p/glintercept/](https://code.google.com/p/glintercept/)
- AMD codexl [http://developer.amd.com/tools-and-sdks/opencl-zone/codexl/](http://developer.amd.com/tools-and-sdks/opencl-zone/codexl/)
- NVidia Nsight [http://www.nvidia.com/object/nsight.html](http://www.nvidia.com/object/nsight.html)


#Activities

##Activities

- You should try to **all of these** today. Work on them in your free-study time if you need
- You should mainly only change the GLSL shaders to do this!
    - You **should not** alter the vertices in the C/C++ program.
    - Only alter the vertices with GLSL
- You may find the GLSL reference card useful
    - http://www.khronos.org/files/opengl-quick-reference-card.pdf
    - GLSL 3.2 and 3.3 are close-enough for us
- If you want to make each of these activities as a separate `git branch` you can
    - if you fork my repo on github, and upload your own branches
    - then you can send pull requests - for feedback and as **student as producer**

##GLSL sources

- There are **lots** of GLSL examples online
- These are a **great** place to start
- There are also examples on arcsynthesis and in the OpenGLSuperBible

##Activity List

1) GLSL is **NOT** C. What are the key differences?
2) make the triangle color something different
3) make the triangle appear somewhere else on the screen, but the original shape
4) make the triangle larger than the original
5) make the position of the triangle controlled by a **variable** that you pass in from C/C++
    - look **uniform** and **varying**
6) make the position change over time, by changing that **variable** in C/C++

##Stretch Activities

- If you've got through the standard activities then have a bash at these

1) make the triangle be in a rotated position
    - this is **rotation**
2) make the triangle rotate over time
3) make the triangle translate **and** scale, over time
4) make the triangle translate **and** rotate, over time!!!!!!!!!!
