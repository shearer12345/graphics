#Apitrace - Vertex Shader creation

##glCreateShader (vertex)

- [main.cpp line 158 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L158)
```C++
GLuint shader = glCreateShader(eShaderType);
```

- [glCreateShader](https://www.opengl.org/sdk/docs/man4/html/glCreateShader.xhtml) Creates a shader object
- returns a non-zero value by which it can be referenced

![01_glCreateShaderVertex.png](assets/apitrace/02_glCreateShader_vertex/01_glCreateShaderVertex.png)

##glCreateShader (vertex) - context

- a new (empty) shader with ID=1 now exists in our context
- the shader is empty
- nothing else has changed

TODO - diagram of context, with a new vertex shader, based on ![assets/apitrace/context_draft.jpg](assets/apitrace/context_draft.jpg)

##glShaderSource (vertex)

- [main.cpp line 160 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L160)
```C++
glShaderSource(shader, 1, &strFileData, NULL);
```

- [glShaderSource](https://www.opengl.org/sdk/docs/man4/html/glShaderSource.xhtml) — Replaces the source code in a shader object

![02_glShaderSourceVertex.png](assets/apitrace/02_glCreateShader_vertex/02_glShaderSourceVertex.png)


##glShaderSource (vertex) - context

- the shader with ID=1 is now loaded with source
- nothing else has changed

TODO - diagram of context, with the vertex shader loaded with the source

##glCompileShader (vertex)

- [main.cpp line 162 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L162)
```C++
glCompileShader(shader);
```

- [glCompileShader](https://www.opengl.org/sdk/docs/man4/html/glCompileShader.xhtml) — Compiles a shader object

![03_glCompileShaderVertex.png](assets/apitrace/02_glCreateShader_vertex/03_glCompileShaderVertex.png)


##glCompileShader (vertex) - context

- the shader with ID=1 has now been compiled
- nothing else has changed

TODO - diagram of context, with the vertex shader loaded with the source, and compiled

##glGetShaderiv (vertex)

- [main.cpp line 165 in our C++ code](https://github.com/shearer12345/graphics_examples_in_git_branches/blob/glTraingleWhiteWithApiTrace/main.cpp#L165)
```C++
glGetShaderiv(shader, GL_COMPILE_STATUS, &status);
```

- [glGetShaderiv](https://www.opengl.org/sdk/docs/man4/html/glGetShader.xhtml) - returns a parameter from a shader object
- in this case the compile status, which is 1 (=ok)
- nothing has changed in the context, we just queried it
    - queries are **expensive** (relatively) operations

![04_glGetShaderivVertex.png](assets/apitrace/02_glCreateShader_vertex/04_glGetShaderivVertex.png)
