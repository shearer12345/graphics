#Why Is Computer Graphics Hard?

##Why do you think?

##What do we mean by Computer Graphics

- ???

##What do we mean by Computer Graphics

- interactive
- 3D
- generating of a sequence of static 2D projections of 3D scenes fast enough and realistically enough to trick the human eye into "seeing" smooth 3D motion

#What Kinds of Factors

- human-ones
- physical ones (about the real world)
- computational ones

##Some things that make it hard

- Needing to do lots fast
- the maths etc
- the algorithms
- computational limits
    - cpu time
    - ram?
- program limits (api or other)
- the cpu/api/gpu boundaries etc

#Let's do some back of the envelope Maths

- ...
- how much "work" do we need to do?

##Let's do some back of the envelope Maths

- how many pixels per frame
    - to look ok/good
    - projector?
    - HD?
    - ...
- how many frames per second
    - to trick our eyes into seeing motion

##How many pixels per frame

- to look ok/good
- normal projector = 1024 x 768 ~= 750,000 pixels
- FullHD = 1920 x 1080 ~= **2,000,000 pixels**

Note: for appproximation using 2 million pixels

##How many frames per second

- to trick our eyes into seeing motion
    - 25fps -> 100fps
    - aim for **50fps** or 60fps
 Note: for appproximation using 50fps

##How many pixels per second?

- ????

##How many pixels per second?

- 2,000,000 pixels per frame
- times
- 50 frames per second

##How many pixels per second?

- 2,000,000 pixels per frame
- times
- 50 frames per second
- = 100,000,000 pixels per second

##How much computational processing is needed?

- ???


