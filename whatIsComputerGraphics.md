%WhatIsComputerGraphics
%shearer12345

#The purpose of graphics

- The purpose of graphics of any kind is to determine what color to put in what pixels
- This determination is what makes text look like text, windows look like windows, and so forth

![Examples of Graphics](assets/exampleOfGraphics.png)

#3D Graphics?

- Images are just a two-dimensional array of pixels
  - So, how does 3D work?
- 3D graphics is some system of producing colors for pixels that convince you that the scene you are looking at is a 3D world rather than a 2D image
- The process of converting a 3D world into a 2D image of that world is called rendering

#Rasterization

- There are several methods for rendering a 3D world
- Real-time graphics hardware, such as that found in your computer, involves a very great deal of fakery
- This approach is called rasterization  and has some constraints:
  - all objects that you see are empty shells (surfaces only)
  - **Everything is a shell**
  - Techniques exists to cut open these empty shells, but they simply replace parts of the shell with more shells that shows what the inside looks like
