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
- **NOT** the only lighting model, but used very frequently in Games
- from http://en.wikipedia.org/wiki/Phong_reflection_model

![phongComponents](assets/phongComponents.png)


##Phong lighting model 2

- **model** of **local** illumination
    - model?
    - local?
- describes the way a surface reflects light as a combination of
    - the diffuse reflection of rough surfaces
    - the specular reflection of shiny surfaces
- also an ambient term to model light that is scattered about the entire scene

##Phong lighting model 3

- you specify these three "types" of lighting separately
    - this is **NOT** connected to reality!
    - but does keep things relatively simple
- you also have to specify properties of lights and surfaces
- i.e. it ends up as a **large** number of parameters

##Phong Vectors

![lighting_blinnVectors](assets/lighting_blinnVectors.png)

- direction of incident light = $\hat{L}_m$
- direction of reflected light = $\hat{R}_m$
- the importance of the viewing position = $\hat{V}$
- normal to the surface = $\hat{N}$

##Light Sources

- each light source in the scene has an **intensity** for
    - specular component - $i_\text{s}$
    - diffuse components - $i_\text{d}$
    - usually RGB values
- there is (in this model) a single term that controls the ambient lighting
    - can be computed as a sum of contributions from all light sources
    - $i_\text{a}$

##Materials

- each surface in the scene has an associated material specifying how that surface reflects the various **"types"** of light.
    - this **may** be stored in textures for more lighting detail
    - specular reflection coefficient - what proportion of incoming "specular" light is reflected
        - $k_\text{s}$
    - diffuse reflection coefficient - $k_\text{d}$
    - ambient reflection coefficient - $k_\text{a}$
- plus a **shininess** constant for the material - $\alpha$

##Phong reflection model

- $\hat{L}_m$ - direction of incident light
- $\hat{R}_m$ - direction of reflected light
- $\hat{V}$ - the importance of the viewing position
- $\hat{N}$ - normal to the surface

- $i_\text{s}$ - specular component
- $i_\text{d}$ - diffuse component
- $i_\text{a}$ - ambient component

- $k_\text{s}$ - specular reflection coefficient
- $k_\text{d}$ - diffuse reflection coefficient
- $k_\text{a}$ - ambient reflection coefficient
- $\alpha$ - shininess

- $I_\text{p}$ = illumination of each surface point

##Phong reflection model 2

$I_\text{p} = k_\text{a} i_\text{a} + \sum_{m\;\in\;\text{lights}} (k_\text{d} (\hat{L}_m \cdot \hat{N}) i_{m,\text{d}} + k_\text{s} (\hat{R}_m \cdot \hat{V})^{\alpha}i_{m,\text{s}})$

##Reflection vector

direction vector $$$\hat{R}_m$$$ is calculated as the reflection of $$$\hat{L}_m$$$ on the surface characterized by the surface normal $$$\hat{N}$$$ using

$\hat{R}_m = 2(\hat{L}_m\cdot \hat{N})\hat{N} - \hat{L}_m$

   - hats indicate that the vectors are normalized

##Phong reflection model properties

- diffuse term is not affected by the viewer direction ($\hat{V}$)
- specular term is large only when the viewer direction ($\hat{V}$) is aligned with the reflection direction $\hat{R}_m$
    - their alignment is measured by the $\alpha$ power of the cosine of the angle between them
    - the cosine of the angle between the normalized vectors $\hat{R}_m$ and $\hat{V}$ is equal to their **dot product**
    - when $\alpha$ is large, in the case of a nearly mirror-like reflection, the specular highlight will be small
        - because any viewpoint not aligned with the reflection will have a cosine less than one which rapidly approaches zero when raised to a high power

##Phong reflection model summary

![lighting_blinnVectors](assets/lighting_blinnVectors.png)
![phongComponents](assets/phongComponents.png)

##Lighting per-vertex vs per-fragment

- we can apply the lighting model at
    - each **vertex**
    - or each **fragment**

![lighting_none_per-vertex_and_per-fragment](assets/lighting_none_per-vertex_and_per-fragment.png)

- computational cost

