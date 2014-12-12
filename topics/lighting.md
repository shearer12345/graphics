#Lighting

##What visual features are we looking for

- surfaces angled away from lights are less well lit
- curved surfaces show specular highlights
- objects obscure each other's light (shadows)

![lighting_none_per-vertex_and_per-fragment](assets/lighting_none_per-vertex_and_per-fragment.png)

##Diffuse vs Specular

![lighting_diffuseVsSpecular](assets/lighting_diffuseVsSpecular.gif)

##Phong lighting model

- aka *Phong reflection model*, *Phong illumination*
- **Bui Tuong Phong** at the University of Utah
   - **1973!!!**

- from http://en.wikipedia.org/wiki/Phong_reflection_model

![phongComponents](assets/phongComponents.png)

##Phong Vectors

![lighting_blinnVectors](assets/lighting_blinnVectors.png)

- direction of incident light
- direction of reflected light
- the importance of the viewing position
- normal to the surface

##Lighting per-vertex vs per-fragment

![lighting_none_per-vertex_and_per-fragment](assets/lighting_none_per-vertex_and_per-fragment.png)

  - computational cost

