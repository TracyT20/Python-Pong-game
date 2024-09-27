# Python-Pong-game
Classic pong game built entirely in python using object oriented programming and the turtle library

## Game overview

Paddles: Each player controls a rectangular paddle that can move vertically up or down. The paddles are positioned on the left and right sides of the screen.

Ball: A small "ball" continuously moves around the screen. The ball bounces off the top and bottom edges of the screen and the paddles.

Goal: The goal is to prevent the ball from passing your paddle and reaching the edge of your side of the screen. When a player misses the ball, the opponent scores a point.

Scoring: The game keeps track of the score, displayed at the top of the screen. 

## Game Mechanics

Paddle Movement: The paddle on the left is contolled using the "w" key to move up and the "s" key to move down, while the right player uses the "UP arrow key" to move up and "down arrow key to move down". (Note that you might not be able to do a long press) 

Ball movement: The ball speeds up after each hit, making it progressively harder to intercept. The angle of the ball’s bounce can change depending on where it hits the paddle.

## Installation Guide
### 1. Clone the Repository
Clone the repository using Git:

```bash
git clone https://github.com/TracyT20/Python-Pong-game.git

```

### 2. Change into the project directory

```bash
cd Python-Pong-game
```
### 3. Install dependencies:
The project dependencies are listed in the requirements.txt file. To install them, run the following command:

```bash
pip install -r requirements.txt
```

### 4. Run program:
You can run the application using the following command:

```bash
python main.py
```

## Contributing

Contributions are always welcome!

If you'd like to contribute to this project, follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push the changes to your fork (git push origin feature-name).

Submit a pull request.
