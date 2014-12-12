#Textures

##Why use textures

- Textures are typically used to add visual detail to models without adding geometric detail
- Textures are in fact just data stores, much like VertexBufferObjects
    - we can use them to store all sort of things
    - access this data (fairly) arbitrarily from GLSL (unlike VBOs)
- It's possible to have 1D, 2D and even 3D textures
- We'll focus on using textures for images, and applying them to geometry

##Creating Textures and Binding

- Similarly to VertexBufferObjects, we have to ask OpenGL to create Textures (or texture objects) for us

```C++
GLuint textureID; //storage for a textureID
glGenTextures(1, &textureID); //create 1 texture id and store it in textureID
```

- In order to do things with a texture object, we have to bind it
    - we'll bind to GL\_TEXTURE_2D as images are 2D arrays of pixels

```C++
glBindTexture(GL_TEXTURE_2D, tex); //make textureID the active 2D texture
```

##Texture Coordinates

- When drawing we want to able to refer to parts of a texture
- We do this with **Texture Coordinates**
    - aka *UV Coordinates* or *ST Coordinates*
- Texture Coordinates range from `0.0` to `1.0`
- `(0,0)` is usually the bottom-left of the image
- `(1,1)` is usually the top-right of the image

##Getting data from textures

- **Sampling** is the process of retrieving data from a texture object
    - usually color data
- We can control how the sampling occurs, to match our circumstances

##Texture Wrapping

- What should happen if we try to sample a texture outside the `0.0` to `1.0` range?
    - we still want the sampler to return a value
    - ```GL_REPEAT``` - the integer part of the coordinate will be ignored and a repeating pattern is formed
    - ```GL_MIRRORED_REPEAT``` - the texture will also be repeated, but it will be **mirrored** when the integer part of the coordinate is odd
    - ```GL_CLAMP_TO_EDGE``` - coordinates will be **clamped** to the `0.0` to `1.0` range
    - ```GL_CLAMP_TO_BORDER``` - coordinates outside the range will be given a specific border color

##Texture Wrapping examples

- from https://open.gl/textures

![Texture Clamping](assets/textureClamping.png)

##S, T, R coordinates and wrapping

- texture coordinates are just vectors:
    - 1D texturing - `float`
    - 2D texturing - `vec2`
    - 3D texturing - `vec3`
- when using a `vec` for textures we call the coordinates `s`, `t`, and `r`
    - instead of `x`, `y`, and `z`
- coordinate wrapping can be set per coordinate
    - i.e. it can be different on each axis

##Setting texture wrapping

- texture parameters are set with the `glTexParameter*` command
    - the star refers to the `type` of value you wish to set

```C++
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
```

##Texture filtering

- texture coordinates are resolution independent
- usually, they don't always match a pixel exactly
    - so a texture image is stretched beyond its original size
    - or it's sized down

##Texture filtering options

- we can ask OpenGL to use specifics methods in deciding on the sampled color
    - ```GL_NEAREST``` - returns the pixel that is closest to the coordinates
    - ```GL_LINEAR``` - returns the weighted average of the 4 pixels surrounding the given coordinates
    - ```GL_NEAREST_MIPMAP_NEAREST``` - later
    - ```GL_LINEAR_MIPMAP_NEAREST``` - later
    - ```GL_NEAREST_MIPMAP_LINEAR``` - later
    - ```GL_LINEAR_MIPMAP_LINEAR``` - later

##Texture filtering example

- from https://open.gl/textures

![textureFiltering](assets/textureFiltering.png)

##Texture filtering example 2

- from http://www.proun-game.com/Oogst3D/index.php?file=CODING/Raytracer/History.txt

![textureFilteringZoomed](assets/textureFilteringZoomed.png)

##Specifying Texture Filtering

- we can specify the kind of interpolation separately for:
    - scaling the image down - "*minification*" - `GL_TEXTURE_MIN_FILTER`
    - scaling the image up - "*magnification*" - `GL_TEXTURE_MAG_FILTER`

```C++
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
```

##MipMaps !!!

- we previously mentioned Mipmaps for texturing, but didn't define them
- Mipmaps are smaller copies of your texture that have been sized down and filtered in advance
- It is recommended that you use them because they result in both a higher quality and higher performance

```C++
glGenerateMipmap(GL_TEXTURE_2D); //generate mipmaps for the present texture
```

##Mipmap Examples

![mipmapExample](assets/mipmapExample.jpg)

##Using mipmaps

- just set the filtering method
    - ```GL_NEAREST_MIPMAP_NEAREST``` - use the mipmap that most closely matches the size of the pixel being textured and sample it with nearest neighbour interpolation
    - ```GL_LINEAR_MIPMAP_NEAREST``` - samples the closest mipmap with linear interpolation
    - ```GL_NEAREST_MIPMAP_LINEAR``` - uses the two mipmaps that most closely match the size of the pixel being textured and samples with nearest neighbour interpolation
    - ```GL_LINEAR_MIPMAP_LINEAR` - samples closest two mipmaps with linear interpolation

##Loading texture images

Now that the texture object has been configured it's time to load the texture image. This is done by simply loading an array of pixels into it:

// Black/white checkerboard
float pixels[] = {
    0.0f, 0.0f, 0.0f,   1.0f, 1.0f, 1.0f,
    1.0f, 1.0f, 1.0f,   0.0f, 0.0f, 0.0f
};
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 2, 2, 0, GL_RGB, GL_FLOAT, pixels);

The first parameter after the texture target is the level-of-detail, where 0 is the base image. This parameter can be used to load your own mipmap images. The second parameter specifies the internal pixel format, the format in which pixels should be stored on the graphics card. Many different formats are available, including compressed formats, so it's certainly worth taking a look at all of the options. The third and fourth parameters specify the width and height of the image. The fifth parameter should always have a value of 0 per the specification. The next two parameter describe the format of the pixels in the array that will be loaded and the final parameter specifies the array itself. The function begins loading the image at coordinate (0,0), so pay attention to this.

But how is the pixel array itself established? Textures in graphics applications will usually be a lot more sophisticated than simple patterns and will be loaded from files. Best practice is to have your files in a format that is natively supported by the hardware, but it may sometimes be more convenient to load textures from common image formats like JPG and PNG. Unfortunately OpenGL doesn't offer any helper functions to load pixels from these image files, but that's where third-party libraries come in handy again! The SOIL library will be discussed here along with some of the alternatives.
SOIL

SOIL (Simple OpenGL Image Library) is a small and easy-to-use library that loads image files directly into texture objects or creates them for you. You can start using it in your project by linking with SOIL and adding the src directory to your include path. It includes Visual Studio project files to compile it yourself.

Although SOIL includes functions to automatically create a texture from an image, it uses features that aren't available in modern OpenGL. Because of this we'll simply use SOIL as image loader and create the texture ourselves.

int width, height;
unsigned char* image =
    SOIL_load_image("img.png", &width, &height, 0, SOIL_LOAD_RGB);
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB,
              GL_UNSIGNED_BYTE, image);

You can start configuring the texture parameters and generating mipmaps after this.

SOIL_free_image_data(image);

You can clean up the image data right after you've loaded it into the texture.
Alternative options

Other libraries that support a wide range of file types like SOIL are DevIL and FreeImage. If you're just interested in one file type, it's also possible to use libraries like libpng and libjpeg directly. If you're looking for more of an adventure, have a look at the specification of the BMP and TGA file formats, it's not that hard to implement a loader for them yourself.
Using a texture

As you've seen, textures are sampled using texture coordinates and you'll have to add these as attributes to your vertices. Let's modify the last sample from the previous chapter to include these texture coordinates. The new vertex array will now include the s and t coordinates for each vertex:

float vertices[] = {
//  Position      Color             Texcoords
    -0.5f,  0.5f, 1.0f, 0.0f, 0.0f, 0.0f, 0.0f, // Top-left
     0.5f,  0.5f, 0.0f, 1.0f, 0.0f, 1.0f, 0.0f, // Top-right
     0.5f, -0.5f, 0.0f, 0.0f, 1.0f, 1.0f, 1.0f, // Bottom-right
    -0.5f, -0.5f, 1.0f, 1.0f, 1.0f, 0.0f, 1.0f  // Bottom-left
};

The vertex shader needs to be modified so that the texture coordinates are interpolated over the fragments:

...

in vec2 texcoord;

out vec3 Color;
out vec2 Texcoord;

...

void main()
{
    Texcoord = texcoord;

Just like when the color attribute was added, the attribute pointers need to be adapted to the new format:

glVertexAttribPointer(posAttrib, 2, GL_FLOAT, GL_FALSE,
                       7*sizeof(float), 0);
glVertexAttribPointer(colAttrib, 3, GL_FLOAT, GL_FALSE,
                       7*sizeof(float), (void*)(2*sizeof(float)));

GLint texAttrib = glGetAttribLocation(shaderProgram, "texcoord");
glEnableVertexAttribArray(texAttrib);
glVertexAttribPointer(texAttrib, 2, GL_FLOAT, GL_FALSE,
                       7*sizeof(float), (void*)(5*sizeof(float)));

As two floats were added for the coordinates, one vertex is now 7 floats in size and the texture coordinate attribute consists of 2 of those floats.

Now just one thing remains: providing access to the texture in the fragment shader to sample pixels from it. This is done by adding a uniform of type sampler2D, which will have a default value of 0. This only needs to be changed when access has to be provided to multiple textures, which will be considered in the next section.

For this sample, the image of the kitten used above will be loaded using the SOIL library. Make sure that it is located in the working directory of the application.

int width, height;
unsigned char* image =
    SOIL_load_image("sample.png", &width, &height, 0, SOIL_LOAD_RGB);
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB,
              GL_UNSIGNED_BYTE, image);
SOIL_free_image_data(image);

To sample a pixel from a 2D texture using the sampler, the function texture can be called with the relevant sampler and texture coordinate as parameters. We'll also multiply the sampled color with the color attribute to get an interesting effect. Your fragment shader will now look like this:

#version 150

in vec3 Color;
in vec2 Texcoord;

out vec4 outColor;

uniform sampler2D tex;

void main()
{
    outColor = texture(tex, Texcoord) * vec4(Color, 1.0);
}

When running this application, you should get the following result:

If you get a black screen, make sure that your shaders compiled successfully and that the image is correctly loaded. If you can't find the problem, try comparing your code to the sample code.
Texture units

The sampler in your fragment shader is bound to texture unit 0. Texture units are references to texture objects that can be sampled in a shader. Textures are bound to texture units using the glBindTexture function you've used before. Because you didn't explicitly specify which texture unit to use, the texture was bound to GL_TEXTURE0. That's why the default value of 0 for the sampler in your shader worked fine.

The function glActiveTexture specifies which texture unit a texture object is bound to when glBindTexture is called.

glActiveTexture(GL_TEXTURE0);

The amount of texture units supported differs per graphics card, but it will be at least 48. It is safe to say that you will never hit this limit in even the most extreme graphics applications.

To practice with sampling from multiple textures, let's try blending the images of the kitten and one of a puppy to get the best of both worlds! Let's first modify the fragment shader to sample from two textures and blend the pixels:

...

uniform sampler2D texKitten;
uniform sampler2D texPuppy;

void main()
{
    vec4 colKitten = texture(texKitten, Texcoord);
    vec4 colPuppy = texture(texPuppy, Texcoord);
    outColor = mix(colKitten, colPuppy, 0.5);
}

The mix function here is a special GLSL function that linearly interpolates between two variables based on the third parameter. A value of 0.0 will result in the first value, a value of 1.0 will result in the second value and a value in between will result in a mixture of both values. You'll have the chance to experiment with this in the exercises.

Now that the two samplers are ready, you'll have to assign the first two texture units to them and bind the two textures to those units. This is done by adding the proper glActiveTexture calls to the texture loading code.

GLuint textures[2];
glGenTextures(2, textures);

int width, height;
unsigned char* image;

glActiveTexture(GL_TEXTURE0);
glBindTexture(GL_TEXTURE_2D, textures[0]);
image = SOIL_load_image("sample.png", &width, &height, 0, SOIL_LOAD_RGB);
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB,
              GL_UNSIGNED_BYTE, image);
SOIL_free_image_data(image);
glUniform1i(glGetUniformLocation(shaderProgram, "texKitten"), 0);

glActiveTexture(GL_TEXTURE1);
glBindTexture(GL_TEXTURE_2D, textures[1]);
image = SOIL_load_image("sample2.png", &width, &height, 0, SOIL_LOAD_RGB);
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB,
              GL_UNSIGNED_BYTE, image);
SOIL_free_image_data(image);
glUniform1i(glGetUniformLocation(shaderProgram, "texPuppy"), 1);

The texture units of the samplers are set using the glUniform function you've seen in the previous chapter. It simply accepts an integer specifying the texture unit. This code should result in the following image.

As always, have a look at the sample source code if you have trouble getting the program to work.

Now that texture sampling has been covered in this chapter, you're finally ready to dive into transformations and ultimately 3D. The knowledge you have at this point should be sufficient for producing most types of 2D games, except for transformations like rotation and scaling which will be covered in the next chapter.