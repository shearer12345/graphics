#Apitrace - GLSL program creation

##glCreateProgram

- [main.cpp line 191 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L191)
```C++
GLuint program = glCreateProgram();
```

- [glCreateProgram](https://www.opengl.org/sdk/docs/man4/html/glCreateProgram.xhtml) Creates a program object
- returns a non-zero value by which it can be referenced
- in this case the ID is **3**

![01_glCreateProgram.png](assets/apitrace/04_glCreateProgram/01_glCreateProgram.png)

##glCreateProgram - context

- a new GLSL program with ID=**3** now exists in our context
- the program is empty
- nothing else has changed

TODO - diagram of context, with a new GLSL program, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glAttachShader (vertex)

- [main.cpp line 194 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L194)
```C++
glAttachShader(program, shaderList[iLoop]);
```

- [glCreateProgram](https://www.opengl.org/sdk/docs/man4/html/glAttachShader.xhtml) Attaches a shader object to a program object
- in this case we are attaching to the program with ID=**3**, the shader with ID=**1 (our vertex shader)**

![02_glAttachShaderVertex.png](assets/apitrace/04_glCreateProgram/02_glAttachShaderVertex.png)

##glAttachShader (vertex) - context

- our GLSL program with ID=**3** now has our shader with ID=**1 (vertex)** attached
- the program is still empty
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glAttachShader (fragment)

- [main.cpp line 194 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L194)
```C++
glAttachShader(program, shaderList[iLoop]);
```

- [glCreateProgram](https://www.opengl.org/sdk/docs/man4/html/glAttachShader.xhtml) Attaches a shader object to a program object
- in this case we are attaching to the program with ID=**3**, the shader with ID=**2 (our fragment shader)**

![03_glAttachShaderFragment.png](assets/apitrace/04_glCreateProgram/03_glAttachShaderFragment.png)

##glAttachShader (fragment) - context

- our GLSL program with ID=**3** now has our shader with ID=**2 (fragment)** attached
- the program is still empty
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glBindAttribLocation

- this call doesn't actually exist in our program - it's been inserted by either SDL or a higher-level part of OpenGL
- **but**, we could have called it ourselves, if we wanted to choose the AttribLocation

- [glBindAttribLocation](https://www.opengl.org/sdk/docs/man4/html/glBindAttribLocation.xhtml) Associates a generic vertex attribute index with a named attribute variable
- in this case associates attribute index **0**, on our program with ID=3, with the GLSL name **position**

![04_glBindAttribLocation.png](assets/apitrace/04_glCreateProgram/04_glBindAttribLocation.png)

##glBindAttribLocation - context

- our GLSL program with ID=**3** now has **position** associated with attribute index **0**
- the program is still empty
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glLinkProgram

- [main.cpp line 196 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L196)
```C++
glLinkProgram(program);
```

- [glLinkProgram](https://www.opengl.org/sdk/docs/man4/html/glBindAttribLocation.xhtml) Links a program object
- in this case out GLSL program with ID=**3**
- status of the link operation will be stored as part of the program object's state

![05_glLinkProgram.png](assets/apitrace/04_glCreateProgram/05_glLinkProgram.png)

##glLinkProgram - context

- our GLSL program now has a **linked program** in it, which we need to check the link status of
- this program exists separately from the attached shaders
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glGetProgramiv

- [main.cpp line 199 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L199)
```C++
glGetProgramiv(program, GL_LINK_STATUS, &status););
```

- [glGetProgramiv](https://www.opengl.org/sdk/docs/man4/html/glGetProgram.xhtml) Returns a parameter from a program object
- in this case get the GL_LINK_STATUS - if the linking worked

![06_glGetProgramiv.png](assets/apitrace/04_glCreateProgram/06_glGetProgramiv.png)

##glGetProgramiv - context

- no context change - this is a **get** function
- remember: **get** functions tend to be relatively expensive

##glDetachShader (vertex)

- [main.cpp line 212 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L212)
```C++
glDetachShader(program, shaderList[iLoop]);
```

- [glDetachShader](https://www.opengl.org/sdk/docs/man4/html/glDetachShader.xhtml) Detaches a shader object from a program object to which it is attached
- in this case we are detaching from the program with ID=**3**, the shader with ID=**1 (our vertex shader)**

![07_glDetachShaderVertex.png](assets/apitrace/04_glCreateProgram/07_glDetachShaderVertex.png)

##glDetachShader (vertex) - context

- our GLSL program with ID=**3** no longer has our shader with ID=**1 (vertex)** attached
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glDetachShader (fragment)

- [main.cpp line 212 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L212)
```C++
glDetachShader(program, shaderList[iLoop]);
```

- [glDetachShader](https://www.opengl.org/sdk/docs/man4/html/glDetachShader.xhtml) Detaches a shader object from a program object to which it is attached
- in this case we are detaching from the program with ID=**3**, the shader with ID=**2 (our fragment shader)**

![08_glDetachShaderFragment.png](assets/apitrace/04_glCreateProgram/08_glDetachShaderFragment.png)

##glDetachShader (fragment) - context

- our GLSL program with ID=**3** no longer has our shader with ID=**2 (fragment)** attached
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glGetAttribLocation (position)

- [main.cpp line 235 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L235)
```C++
positionLocation = glGetAttribLocation(theProgram, "position");
```

- [glGetAttribLocation](https://www.opengl.org/sdk/docs/man4/html/glGetAttribLocation.xhtml) Returns the location of an attribute variable
- in this case we are getting the location of attribute **position** in the program with ID=**3**
- which is 0

![09_glGetAttribLocation.png](assets/apitrace/04_glCreateProgram/09_glGetAttribLocation.png)

##glGetAttribLocation (position) - context

- this is a **get** function, nothing has changed in the context

##glGetUniformLocation (offset)

- [main.cpp line 236 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L236)
```C++
offsetLocation = glGetUniformLocation(theProgram, "offset");
```

- [glGetAttribLocation](https://www.opengl.org/sdk/docs/man4/html/glGetAttribLocation.xhtml) Returns the location of a uniform variable
- in this case we are getting the location of uniform **offset** in the program with ID=**3**
- which is 0

![10_glGetUniformLocation.png](assets/apitrace/04_glCreateProgram/10_glGetUniformLocation.png)

##glGetUniformLocation (offset) - context

- this is a **get** function, nothing has changed in the context


##glDeleteShader (vertex)

- [main.cpp line 238 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L238)
```C++
for_each(shaderList.begin(), shaderList.end(), glDeleteShader);
```

- [glDeleteShader](https://www.opengl.org/sdk/docs/man4/html/glDeleteShader.xhtml) Deletes a shader object
- frees the memory and invalidates the name associated with the shader object specified by shader.
- in this case our shader with ID=**1** (the vertex shader) is deleted

![11_glDeleteShaderVertex.png](assets/apitrace/04_glCreateProgram/11_glDeleteShaderVertex.png)

##glDeleteShader (vertex) - context

- the shader with ID=**1** no longer exists
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)

##glDeleteShader (fragment)

- [main.cpp line 238 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L238)
```C++
for_each(shaderList.begin(), shaderList.end(), glDeleteShader);
```

- [glDeleteShader](https://www.opengl.org/sdk/docs/man4/html/glDeleteShader.xhtml) Deletes a shader object
- frees the memory and invalidates the name associated with the shader object specified by shader.
- in this case our shader with ID=**2** (the fragment shader) is deleted

![12_glDeleteShaderFragment.png](assets/apitrace/04_glCreateProgram/12_glDeleteShaderFragment.png)

##glDeleteShader (fragment) - context

- the shader with ID=**2** (our fragment shader) no longer exists
- nothing else has changed

TODO - diagram of context, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg_hide)
