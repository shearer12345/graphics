#Depth Testing

##Why depth testing

- without depth testing each triangle rendered draws on top of previous pixels
- this causes problems (```glmRotateColorCubeNoCullingNoDepthTest```)
- we could try to draw all far away triangles first
- then draw nearer ones
    - requires **sorting** the triangles
    - doesn't work for all cases ...

##What is Depth Testing

- depth test is a per-sample operation performed conceptually after the Fragment Shader
    - under some circumstances it can occur **before** frag shader, but ...
- output depth may be tested against the depth of the sample being written to
- if the test fails, the fragment is discarded
- if the test passes, the depth buffer may be written to
- writing to the depth/colour buffer is a relatively slow operation, so minimizing writes is a good optimization
    - how could depth testing support this?

##Depth Test Example Branches

- ```glmRotateColorCubeNoCullingWithDepthTest```
- ```glmRotateColorCubeWithCullingWithDepthTest```

- setup depth testing - anywhere before rendering
```C++
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LESS); //only write if z is less (nearer)
```

- //clear depth buffer before rendering
```C++
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
```
