# Game of Life

Python implementation of "Game of Life" according to John Conway rules with animation.

## Table of contents
* [General info](#general-info)
* [Implementation ideas](#implementation-ideas)
* [Run](#run)
* [Technologies](#technologies)
* [Examples of program effects](#examples-of-program-effects)
* [Status](#status)

## General info

This program is an implementation of Conway's "Game of Life". Its general principles:
At the beginning we have a board (in my case in the form of a square with length N). The board is divided into small squares: black and white - black means a dead person (OFF) and white means a living person (ON). Initially, we mark a certain number of living individuals on the board. 
"Next Generation" principles:
- a dead individual/person with exactly three living neighbors is reborn in the next unit of time
- a living individual/person remains alive for the next unit of time when it has two or three living neighbors.

## Implementation ideas

My main goal was to create an animated chart showing "The Game of Life". 
Taking this opportunity, I wanted to learn (and consolidate) aspects of the basics of libraries related to simple mathematical graphics and data analysis.

The variable "N" means the size of the board for me. The function related to animation is strongly related to the program itself, because each cycle (next generation) means another "frame" of the animation. I used modulo (%) expressions to count neighbors. This is due to the fact that if the "family" goes beyond our board, it will cycle on its opposite side (I used a similar mechanism in my "Snake" program).

At the beginning of the program (in the "main" function) we can select the available starting system for living individuals. I created my "figures.py" file with the available options: we can use a random alignment of living individuals (with any frequency of their occurrence: 0.3 by default) or we can choose from 16 popular models available.

Available models:
- [STILL LIFES] block, beehive, loaf, tub, boat
- [OSCILLATORS] blinker, vertical blinker, toad, beacon, pulsar, pentadecathlon
- [SPACESHIPS] glider, lightweight spaceship, heavyweight spaceship
- [GUNS] gosper glider gun, simkin glider gun.
## Run

If you haven't installed NumPy or Matplotlib, use the command:
```bash
   pip install numpy matplotlib
```
To get started with my program, navigate to a directory where you want to use the project, then clone it with:
```bash
   git clone https://github.com/wszlosek/Game-of-Life
```
If you don't want to use git clone for whatever reason, you can manually download it, and move the folder somewhere convenient. Then, open up your terminal, and go to the correct directory. 
Then just run the program:
```bash
   python3 main.py
```
## Technologies
The program was written in Python. Also needed were the "NumPy" and "Matplotlib" libraries which were used to generate the graph and the animation.

## Examples of program effects

The program can test by calling the appropriate functions in the "main".

Let's look at an example 1. In "main" we call the function from the file "figures.py" with the argument being our board ("grid" for me). In this example, a random pattern of living persons was used with an occurrence frequency of approximately 40%.

The remaining examples include the use of ready-made models. The name of the functions responsible for calling them is the name of the given model (see: "Implementation ideas" section in this README file). If the name consists of more than one word, the space is replaced with an underscore (for example: "gosper_glider_gun"). Each of these functions has three arguments: the first is the board (in my case "grid"), the second and third arguments are the place on the board where we want to place our "object". Look at Ex. 0. Such calling means inserting a gosper glider gun on the coordinate (X = 15, Y = 25) of our board:

#### Ex. 0
```python
    ''' fragment of the "main" function: '''

    fig.gosper_glider_gun(grid, 15, 25)
```

![example0](https://github.com/wszlosek/Game-of-Life/blob/main/GIFs/ex0.gif)

#### Ex. 1
```python
    fig.random_grid(grid, 0.4)
```
![example1](https://github.com/wszlosek/Game-of-Life/blob/main/GIFs/ex1.gif)

#### Ex. 2
```python
    fig.pulsar(grid, 10, 10)
    fig.pulsar(grid, 40, 40)
```
![example2](https://github.com/wszlosek/Game-of-Life/blob/main/GIFs/ex2.gif)

#### Ex. 3
Of course, we can combine various functions:
```python
    fig.gosper_glider_gun(grid, 10, 10)
    fig.blinker(grid, 20, 30)
    fig.loaf(grid, 50, 55)
    fig.heavyweight_spaceship(grid, 80, 80)
```
![example3](https://github.com/wszlosek/Game-of-Life/blob/main/GIFs/ex3.gif)

## Status
The project has been completed and all its assumptions have been made.
