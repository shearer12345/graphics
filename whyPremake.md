#Why Premake?

- Creating Build systems is surprisingly hard and fiddley
- Want to be able to build our code on multiple platforms and perhaps automatically
- Want to be able to version the build system (and understand it?)
- Premake is a tool that helps with this
- Other tools exist, such as:
    - Gradle
    - Ant
    - Make

##Counter-Example - setting up for Visual Studio

- http://www.programmersranch.com/2014/02/sdl2-setting-up-sdl2-in-visual-studio.html
- it takes 10 very specific steps
    - that's just setting up **one** platform, for **one** library

##Where to get Premake

- Premake 4.3 supports Make, CodeBlocks, XCode 3, and Visual Studio up to (and including) VS2010
    - http://industriousone.com/premake/download
- Premake 4.4 (in beta) supports Make, CodeBlocks, XCode 3, and Visual Studio up to (and including) VS2012
    - http://industriousone.com/premake/download
- Premake 5 (alpha)
    - https://bitbucket.org/premake/premake-dev
    - roadmap at https://bitbucket.org/premake/premake-dev/wiki/Development_Roadmap
