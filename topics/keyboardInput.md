#Keyboard Input

##Keyboard Input

- we'll focus on Keyboard Input here
- Mice, Joysticks, and Joypads are **all** supported by SDL
- Input is **outside the scope** of OpenGL
    - remember: **OpenGL just does rendering**

##Polling or Event-based

- There are two fundamental approaches to input (from a user or otherwise)
    - Polling
        - Ask what the state is right now
    - Event-based
        - Every time something changes, an event is raised
        - or written to an event list

##Polling or Event-based - Pros/Cons

- Polling vs Event-based
    - what do you think?

##Polling or Event-based - Pros/Cons

- Event-based
    - Con = more complex than Polling
    - Pro = very flexible
    - Pro = don't miss events
        - important if we undo things on key-up
        - see branch```sdlKeyboardInputEventBased```
    - Pro = get events in order
    - Pro = Polling always uses event-based underneath
        - the **hardware** is event-based (USB, etc)
- Polling
    - the opposite

##Keyboard limitations (hardware, usually)

![http://en.wikipedia.org/wiki/File:Inside_Computer_keyboard.jpg](assets/1280px-Inside_Computer_keyboard.jpg)

##Keyboard limitations (hardware, usually) 2

![http://en.wikipedia.org/wiki/File:Keyboard_Construction_Button_Press.JPG](assets/Keyboard_Construction_Button_Press.jpg)

##Keyboard limitations (hardware, usually) 3

- in most keyboards, this leads to a limit on detecting 3 or 4 unique key presses concurrently

##Keyboard input with SDL - Polling

- we can get a snapshot of the current state of the keyboard
    - SDL constructs this state array for us
    - ```SDL_GetKeyboardState()```
    - https://wiki.libsdl.org/SDL_GetKeyboardState
- gives you the current state **after** all events have been processed
    - we **MUST** process all the events **first**
    - with ```SDL_PumpEvents()```
    - https://wiki.libsdl.org/SDL_PumpEvents
- we can then check the state array for scancodes that we're interested in
    - and do **whatever** we like with them
    - this can be complex and is up to you

##Keyboard input with SDL - Polling, example 1

- branch ```sdlKeyboardInputPollBased```
- called **every** frame

```C++
void handleInput()
{
	SDL_PumpEvents();

	const Uint8 *state = SDL_GetKeyboardState(NULL); //somewhere to store an event

	if (state[SDL_SCANCODE_ESCAPE])
		done = true; //hit escape to exit

	if (state[SDL_SCANCODE_LEFT] != state[SDL_SCANCODE_RIGHT]) //just one pressed
	{
		if (state[SDL_SCANCODE_LEFT]) //left pressed
			translateSpeed.x = translateSpeedDefault.x - translateAcceleration.x;
		else //right pressed
			translateSpeed.x = translateSpeedDefault.x + translateAcceleration.x;
	}
	else
		translateSpeed.x = translateSpeedDefault.x;
```

- what about up and down?

##Keyboard input with SDL - Polling, example 2

```C++
	if (state[SDL_SCANCODE_UP] != state[SDL_SCANCODE_DOWN]) //just one pressed
	{
		if (state[SDL_SCANCODE_DOWN]) //left pressed
			translateSpeed.y = translateSpeedDefault.y - translateAcceleration.y;
		else //right pressed
			translateSpeed.y = translateSpeedDefault.y + translateAcceleration.y;
	}
	else
		translateSpeed.y = translateSpeedDefault.y;
}
```

##Keyboard input with SDL - Event-based

- SDL maintains a list of events
    - from the keyboard, mouse, window, ...
- we can pull an **event** off this list, look at it and decide what to do
- there **may** be multiple events between frames
    - make sure the pull off **all** events every frame
    - otherwise wierd stuff can happen, especially with mouse input
    - a while loop
- we get **separate** events for KeyDown and KeyUp


##Keyboard input with SDL - Event-based, example 1

- branch ```sdlKeyboardInputEventBased```
- called **every** frame

```C++
    SDL_Event event; //somewhere to store an event

    //loop until SDL_PollEvent returns 0 (meaning no more events)
    while (SDL_PollEvent(&event)) {
        switch (event.type)
        {
        case SDL_QUIT:
            //set done flag if SDL wants to quit
            done = true;
            break;
```

##Keyboard input with SDL - Event-based, example 2

```C++
        case SDL_KEYDOWN:
            //  - a "repeat" flag is set on the keyboard event, if this is a repeat event
            //  - https://wiki.libsdl.org/SDL_KeyboardEvent
            if (!event.key.repeat)
            switch (event.key.keysym.sym)
            {
                //hit escape to exit
                case SDLK_ESCAPE: done = true;

                case SDLK_LEFT:  translateSpeed.x -= translateAcceleration.x; break;
                case SDLK_RIGHT: translateSpeed.x += translateAcceleration.x; break;

                case SDLK_UP:    translateSpeed.y += translateAcceleration.y; break;
                case SDLK_DOWN:  translateSpeed.y -= translateAcceleration.y; break;
            }
            break;
```

- KeyUp handling?

##Keyboard input with SDL - Event-based, example 3

```C++
        //Do the opposite of keyDown (in this case)
        case SDL_KEYUP:
            switch (event.key.keysym.sym)
            {
                case SDLK_LEFT:  translateSpeed.x += translateAcceleration.x; break;
                case SDLK_RIGHT: translateSpeed.x -= translateAcceleration.x; break;

                case SDLK_UP:    translateSpeed.y -= translateAcceleration.y; break;
                case SDLK_DOWN:  translateSpeed.y += translateAcceleration.y; break;
            }
            break;
```
