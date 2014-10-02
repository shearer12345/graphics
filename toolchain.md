% toolchain
% shearer12345

#Toolchain for graphics

- OpenGL - graphics rendering
- SDL2 - context creation, windowing, input handling
- C / C++ - programming
- premake - solution creation, supporting:
  - gmake
  - code::blocks
  - Visual Studio

#OpenGL

- a C library for graphics rendering
- usually utilises the underlying hardware graphics accelerator (graphics card)

#SDL2

- context creation, windowing, input handling
- OpenGL **only** does rendering, we need other tools for a number of jobs:
  - to setup a "context" that OpenGL can use
  - to create and manipulate windows
  - to handle input
  - ...

#C / C++

- OpenGL provides a C-style API (Application Program Interface)
- that API can be used from C or C++
- or the API can be wrapped for use from other languages (e.g. Java, Python)

#Premake


>Describe your software project just once, using Premake's simple and easy to read syntax, and build it everywhere. Generate project files for Visual Studio, GNU Make, Xcode, Code::Blocks, and more across Windows, Mac OS X, and Linux. Use the full featured Lua scripting engine to make build configuration tasks a breeze.
  - [http://industriousone.com/premake](http://industriousone.com/premake)

- using premake 4.4 (beta5), which supports upto Visual Studio 2012
  - later versions are supported by importing and upgrading the project in VS
  - [premake4.4-beta5](http://industriousone.com/topic/premake-44-beta5-now-available)

