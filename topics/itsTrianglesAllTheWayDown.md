#It's Triangles All The Way Down

![triangle](assets\triangle.png)

##It's Triangles All The Way Down

- Remember: Everything is a shell
- All of these shells are made of **triangles**
- Even surfaces that appear to be round are merely **triangles** if you look closely enough
- There are techniques that generate **more triangles** for objects that appear closer or larger, so that the viewer can almost never see the faceted silhouette of the object, but they are **always made of triangles**

##It's Triangles All The Way Down

- Note: Some rasterizers use planar quadrilaterals: four-sided objects, where all of the lines lie in the same plane. One of the reasons that hardware-based rasterizers always use triangles is that all of the lines of a triangle are guaranteed to be in the same plane. Knowing this makes the rasterization process less complicated.

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

##OpenGL Pipeline

![http://goanna.cs.rmit.edu.au/~gl/teaching/ Interactive3D/2011/lecture2.html](assets\pipeline01.png)

##Raster Ordering

- The order in which triangles and the various meshes are submitted to the rasterizer can affect its output
    - (if you are doing fancy stuff)
- No matter how you submit the triangular mesh data, the rasterizer will process each triangle in a specific order:
    - drawing the next one only when the previous triangle has finished being drawn

##Triangles and Vertices (in OpenGL)

- Triangles consist of 3 vertices
    - A vertex is a collection of arbitrary data
    - ???!!!???
    - For the sake of simplicity, in our context this data must contain a point in three dimensional space - it may contain other data (e.g. colour)
- Any 3 points that are not on the same line create a triangle
    - A triangle is defined by exactly 3 (three-dimensional) points - (X, Y, Z)

