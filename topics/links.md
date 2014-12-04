#Links about Graphics

- a general list
- and related interesting stuff
- peruse at your leisure

##OpenGL 3.0 onwards

- [http://open.gl/](http://open.gl/)
- [http://duriansoftware.com/joe/An-intro-to-modern-OpenGL.-Chapter-1%3a-The-Graphics-Pipeline.html](http://duriansoftware.com/joe/An-intro-to-modern-OpenGL.-Chapter-1%3a-The-Graphics-Pipeline.html)
- [http://www.arcsynthesis.org/gltut/](http://www.arcsynthesis.org/gltut/)
- http://antongerdelan.net/opengl/index.html
    - https://github.com/capnramses/antons_opengl_tutorials_book
    - Kindle Book (~£3.62) - http://www.amazon.co.uk/Antons-OpenGL-Tutorials-Anton-Gerdelan-ebook/dp/B00LAMQYF2
- [https://bitbucket.org/alfonse/gltut/src](https://bitbucket.org/alfonse/gltut/src)
- [http://en.wikibooks.org/wiki/OpenGL_Programming/Modern_OpenGL_Introduction](http://en.wikibooks.org/wiki/OpenGL_Programming/Modern_OpenGL_Introduction)
- [http://www.daveshreiner.com/SIGGRAPH/s11/Modern-OpenGL.pdf](http://www.daveshreiner.com/SIGGRAPH/s11/Modern-OpenGL.pdf)
- [http://fgiesen.wordpress.com/2011/07/09/a-trip-through-the-graphics-pipeline-2011-index/](http://fgiesen.wordpress.com/2011/07/09/a-trip-through-the-graphics-pipeline-2011-index/)

##OpenGL 3.0 onwards 2

- [http://gamedev.stackexchange.com/questions/32876/good-resources-for-learning-modern-opengl-3-0-or-later](http://gamedev.stackexchange.com/questions/32876/good-resources-for-learning-modern-opengl-3-0-or-later)
- [https://github.com/g-truc/ogl-samples](https://github.com/g-truc/ogl-samples)
- OpenGLSuperBible (6th edition) Examples [https://github.com/openglsuperbible/sb6code/tree/master/src](https://github.com/openglsuperbible/sb6code/tree/master/src)
- Open Media Engine OpenGL 4 Tutorials [http://openme.gl/opengl-4-tutorial-code/](http://openme.gl/opengl-4-tutorial-code/)
- OpenGL 4.3/4.4 example using SDL2 and GLM [http://openme.gl/opengl-4-x-example-using-sdl2-and-glm/](http://openme.gl/opengl-4-x-example-using-sdl2-and-glm/)
- Swiftless tutorials [http://www.swiftless.com/opengl4tuts.html](http://www.swiftless.com/opengl4tuts.html)
- http://www.tomdalling.com/blog/category/modern-opengl/

##Texturing

- http://www.tomdalling.com/blog/modern-opengl/02-textures/
- https://www.opengl.org/wiki/Texture
- http://ogldev.atspace.co.uk/www/tutorial16/tutorial16.html
- https://github.com/progschj/OpenGL-Examples/blob/master/03texture.cpp
- https://www.youtube.com/watch?v=UBxB8H4e_5I&list=UUL5m1_llmeiAdZMo_ZanIvg
- http://www.mbsoftworks.sk/index.php?page=tutorials&series=1&tutorial=9
- http://www.lighthouse3d.com/tutorials/glsl-core-tutorial/glsl-core-tutorial-texturing-with-images/

##Context Creation (mostly SDL2)

- https://open.gl/context
- [https://www.libsdl.org/index.php](https://www.libsdl.org/index.php)
- [https://www.youtube.com/watch?v=MeMPCSqQ-34](https://www.youtube.com/watch?v=MeMPCSqQ-34)
- [https://github.com/BennyQBD/ModernOpenGLTutorial](https://github.com/BennyQBD/ModernOpenGLTutorial)
- [https://www.youtube.com/watch?v=ftiKrP3gW3k&list=PLEETnX-uPtBXT9T-hD0Bj31DSnwio-ywh](https://www.youtube.com/watch?v=ftiKrP3gW3k&list=PLEETnX-uPtBXT9T-hD0Bj31DSnwio-ywh)
- Setting up SDL2 in Visual Studio (2013 or any other) [http://www.programmersranch.com/2014/02/sdl2-setting-up-sdl2-in-visual-studio.html](http://www.programmersranch.com/2014/02/sdl2-setting-up-sdl2-in-visual-studio.html)
- 2D tutorials with SDL2 [http://lazyfoo.net/tutorials/SDL/index.php](http://lazyfoo.net/tutorials/SDL/index.php)
- SDL2 migration guide [https://wiki.libsdl.org/MigrationGuide](https://wiki.libsdl.org/MigrationGuide)

##Context Creation (non-SDL)

- Unofficial OpenGL Software Development Kit [http://glsdk.sourceforge.net/docs/html/index.html](http://glsdk.sourceforge.net/docs/html/index.html)
- FreeGlut [http://freeglut.sourceforge.net/](http://freeglut.sourceforge.net/)
- Simple and Fast Multimedia Library [http://www.sfml-dev.org/](http://www.sfml-dev.org/)
- GLFW [http://www.glfw.org/](http://www.glfw.org/)

##platform-specific Context Creation

```C
#include <windows.h>
#include <GL/GL.h>

#pragma comment (lib, "opengl32.lib")

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam);

int WinMain( __in HINSTANCE hInstance, __in_opt HINSTANCE hPrevInstance, __in_opt LPSTR lpCmdLine, __in int nShowCmd )
{
        MSG msg          = {0};
        WNDCLASS wc      = {0}; 
        wc.lpfnWndProc   = WndProc;
        wc.hInstance     = hInstance;
        wc.hbrBackground = (HBRUSH)(COLOR_BACKGROUND);
        wc.lpszClassName = L"oglversionchecksample";
        wc.style = CS_OWNDC;
        if( !RegisterClass(&wc) )
                return 1;
        CreateWindowW(wc.lpszClassName,L"openglversioncheck",WS_OVERLAPPEDWINDOW|WS_VISIBLE,0,0,640,480,0,0,hInstance,0);

        while( GetMessage( &msg, NULL, 0, 0 ) > 0 )
                DispatchMessage( &msg );

        return 0;
}
```

##platform-specific Context Creation 2

```C
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
        switch(message)
        {
        case WM_CREATE:
                {
                PIXELFORMATDESCRIPTOR pfd =
                {
                        sizeof(PIXELFORMATDESCRIPTOR),
                        1,
                        PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER,    //Flags
                        PFD_TYPE_RGBA,            //The kind of framebuffer. RGBA or palette.
                        32,                        //Colordepth of the framebuffer.
                        0, 0, 0, 0, 0, 0,
                        0,
                        0,
                        0,
                        0, 0, 0, 0,
                        24,                        //Number of bits for the depthbuffer
                        8,                        //Number of bits for the stencilbuffer
                        0,                        //Number of Aux buffers in the framebuffer.
                        PFD_MAIN_PLANE,
                        0,
                        0, 0, 0
                };
```

##platform-specific Context Creation 3

```C
                HDC ourWindowHandleToDeviceContext = GetDC(hWnd);

                int  letWindowsChooseThisPixelFormat;
                letWindowsChooseThisPixelFormat = ChoosePixelFormat(ourWindowHandleToDeviceContext, &pfd); 
                SetPixelFormat(ourWindowHandleToDeviceContext,letWindowsChooseThisPixelFormat, &pfd);

                HGLRC ourOpenGLRenderingContext = wglCreateContext(ourWindowHandleToDeviceContext);
                wglMakeCurrent (ourWindowHandleToDeviceContext, ourOpenGLRenderingContext);

                MessageBoxA(0,(char*)glGetString(GL_VERSION), "OPENGL VERSION",0);

                wglDeleteContext(ourOpenGLRenderingContext);
                PostQuitMessage(0);
                }
                break;
        default:
                return DefWindowProc(hWnd, message, wParam, lParam);
        }
        return 0;

}
```

##Extensions Wrangling

- Manual function loading! [https://open.gl/context#Onemorething](https://open.gl/context#Onemorething)
- OpenGl Extension Wrangler Library (GLEW) [http://glew.sourceforge.net/](http://glew.sourceforge.net/)
- gl3w [https://github.com/skaslev/gl3w](https://github.com/skaslev/gl3w)
- gl3w with SDL2 example [https://github.com/progschj/OpenGL-Windowing-Examples/blob/master/sdl2.cpp](https://github.com/progschj/OpenGL-Windowing-Examples/blob/master/sdl2.cpp)
- Lazy Foo on Modern OpenGL [http://lazyfoo.net/tutorials/SDL/51_SDL_and_modern_opengl/index.php](http://lazyfoo.net/tutorials/SDL/51_SDL_and_modern_opengl/index.php)

##Object-orientated OpenGL (OGLplus, C++)

- [http://oglplus.org/](http://oglplus.org/)
- OGLplus tutorials [http://oglplus.org/oglplus/html/oglplus_tutorials.html](http://oglplus.org/oglplus/html/oglplus_tutorials.html)

##using git

- [http://programmaticallyspeaking.com/code-demo-using-git.html](http://programmaticallyspeaking.com/code-demo-using-git.html)
- Try Github [https://try.github.io/levels/1/challenges/1](https://try.github.io/levels/1/challenges/1)
- Git: the simple guide [http://rogerdudler.github.io/git-guide/](http://rogerdudler.github.io/git-guide/)
- Git Immersion [http://gitimmersion.com/](http://gitimmersion.com/)
- Github Guides [https://guides.github.com/](https://guides.github.com/)
- Ungit [https://github.com/FredrikNoren/ungit](https://github.com/FredrikNoren/ungit)
    - Ungit Introduction Video [https://www.youtube.com/watch?v=hkBVAi3oKvo&feature=youtu.be](https://www.youtube.com/watch?v=hkBVAi3oKvo&feature=youtu.be)
- git-big-picture (for summarising git trees) [https://github.com/esc/git-big-picture](https://github.com/esc/git-big-picture)


##Debugging tools

- [apitrace - http://apitrace.github.io/](http://apitrace - http://apitrace.github.io/)
- VOGL:
    - [http://richg42.blogspot.de/2014/01/vogl-opengl-tracerdebugger-bonus-content.html](http://richg42.blogspot.de/2014/01/vogl-opengl-tracerdebugger-bonus-content.html)
    - [https://github.com/ValveSoftware/vogl](https://github.com/ValveSoftware/vogl)
    - [https://www.youtube.com/watch?v=45O7WTc6k2Y -Moving Your Games to OpenGL](https://www.youtube.com/watch?v=45O7WTc6k2Y)

##Build tools (Premake)

- Premake Website (a little out of date) [http://industriousone.com/premake](http://industriousone.com/premake)
- Premake repositories [https://bitbucket.org/premake/](https://bitbucket.org/premake/)
- Premake Meta (Premake quickstart scripts) [https://github.com/d-led/premake-meta-cpp](https://github.com/d-led/premake-meta-cpp)
- Example complex-ish Premake script from gltut [https://bitbucket.org/alfonse/gltut/src/1d1479cc7027f1e32c5adff748f3b296f1931d84/framework/framework.lua?at=default](https://bitbucket.org/alfonse/gltut/src/1d1479cc7027f1e32c5adff748f3b296f1931d84/framework/framework.lua?at=default)

##Matrices

- [http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/](http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/)

##Coordinate Systems

- http://www.matrix44.net/cms/notes/opengl-3d-graphics/coordinate-systems-in-opengl

##Homogeneous Coordinates

- http://www.tomdalling.com/blog/modern-opengl/explaining-homogenous-coordinates-and-projective-geometry/
http://www.songho.ca/math/homogeneous/homogeneous.html

##Timing

- http://headerphile.blogspot.co.uk/2014/07/part-9-no-more-delays.html
- https://wiki.libsdl.org/SDL_GetPerformanceCounter
- http://gafferongames.com/game-physics/fix-your-timestep/

##Engines

- unreal engine 4 on linux (and steamOS and windows and maybe xbox one)
    - [https://www.unrealengine.com/blog/unreal-engine-4-and-linux](https://www.unrealengine.com/blog/unreal-engine-4-and-linux)
    - [http://www.extremetech.com/gaming/179802-windows-apps-announced-for-xbox-one-is-steam-in-the-cards](http://www.extremetech.com/gaming/179802-windows-apps-announced-for-xbox-one-is-steam-in-the-cards)
- Open Media Engine [http://openme.gl/](http://openme.gl/)
    - A simple to use, general purpose, 3D media framework using OpenGL, OpenAL and OpenDE
- OGRE – Open Source 3D Graphics Engine [http://www.ogre3d.org/](http://www.ogre3d.org/)
- Crystal Space [http://www.crystalspace3d.org/main/Main_Page](http://www.crystalspace3d.org/main/Main_Page)
- Horde3D [http://www.horde3d.org/](http://www.horde3d.org/)

##Asset importing

**Note that SDL2 can load standard `.bmp` files on its own, but no other image formats**

- Open Asset Import Library [http://assimp.sourceforge.net/index.html](http://assimp.sourceforge.net/index.html)
- Resilient Image Library [http://sourceforge.net/projects/resil/](http://sourceforge.net/projects/resil/)
- Simple OpenGL Image Library [http://www.opengl-tutorial.org/miscellaneous/useful-tools-links/](http://www.opengl-tutorial.org/miscellaneous/useful-tools-links/)

##other

- unreal engine 4 to linux
    - [https://www.unrealengine.com/blog/41-update-preview](https://www.unrealengine.com/blog/41-update-preview)
- [http://pyopengl.sourceforge.net/context/tutorials/shader_1.html](http://pyopengl.sourceforge.net/context/tutorials/shader_1.html)
- [http://www.networkedgraphics.org/sigasia2011/part3.pdf](http://www.networkedgraphics.org/sigasia2011/part3.pdf)
- [http://goanna.cs.rmit.edu.au/~gl/teaching/Interactive3D/2011/lecture2.html](http://goanna.cs.rmit.edu.au/~gl/teaching/Interactive3D/2011/lecture2.html)
- [http://graphics.cs.illinois.edusvn/kcrane/web/index.html](http://graphics.cs.illinois.edusvn/kcrane/web/index.html)
- [http://www.ogre3d.org/index.php?option=com_content&task=view&id=17&Itemid=70](http://www.ogre3d.org/index.php?option=com_content&task=view&id=17&Itemid=70)
- [http://www.opengl.org/](http://www.opengl.org/)
- [https://software.intel.com/en-us/articles/quake-wars-gets-ray-traced/?wapkw=%28ray+tracing%29](https://software.intel.com/en-us/articles/quake-wars-gets-ray-traced/?wapkw=%28ray+tracing%29)

##other 2

- [https://www.youtube.com/watch?v=hapCuhAs1nA](https://www.youtube.com/watch?v=hapCuhAs1nA)
- [https://www.youtube.com/watch?v=VUxcVzpeFqc](https://www.youtube.com/watch?v=VUxcVzpeFqc)
- [http://www.mesa3d.org/llvmpipe.html](http://www.mesa3d.org/llvmpipe.html)


- [http://www.willusher.io/sdl2%20tutorials/2013/08/15/lesson-0-linux-command-line/](http://www.willusher.io/sdl2%20tutorials/2013/08/15/lesson-0-linux-command-line/)
