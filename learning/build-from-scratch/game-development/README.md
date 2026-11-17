---
id: build-from-scratch.game-development
title: "Build a 2D Game"
content_type: project
locale: en
domain: web-and-app-development
level: beginner
status: draft
learning_objectives:
  - "Explain the stages of a game loop."
  - "Implement frame-rate-independent movement."
  - "Model rectangle collisions and game states."
  - "Build a game that can start, finish, and restart."
prerequisites:
  - "Variables, conditions, loops, and functions"
  - "Basic two-dimensional coordinates"
milestones:
  - "Draw the player in a window."
  - "Add keyboard movement."
  - "Use elapsed time for movement."
  - "Add a collectible and collision."
  - "Add score, restart, and finish state."
  - "Document asset licences."
---

# Build a 2D Game

**Level:** Beginner–Intermediate · **Languages:** Python, JavaScript, or C++ · **Track:** `game`

## Goal
Build a small game where a player moves, collects objects, avoids simple obstacles, and reaches a score or finish condition.

## Prerequisites
Variables, conditions, loops, functions, and basic 2D coordinates.

## Lesson 1 — The game loop
A typical real-time game repeatedly:
1. reads input,
2. updates game state,
3. checks collisions and events,
4. renders the current state,
5. repeats.

Use elapsed time (delta time) for movement so the game does not become faster on machines that render more frames per second.

## Lesson 2 — Position and movement
Represent position with x and y. Velocity describes how position changes over time:

`new_position = old_position + velocity × delta_time`

Keep input handling, update logic, and drawing in separate functions. This separation makes the program easier to debug and test.

## Lesson 3 — Collision and state
Start with axis-aligned rectangles. Two rectangles overlap when their horizontal intervals and vertical intervals both overlap. When a collision occurs, update the game state—for example, increment the score or mark a collectible as taken.

Use explicit states such as `menu`, `playing`, `paused`, and `finished` rather than mixing every rule into one large conditional.

## Build milestones
- **M1:** Open a window and draw the player.
- **M2:** Move the player using keyboard input.
- **M3:** Use delta time for frame-rate-independent movement.
- **M4:** Add a collectible and rectangle collision.
- **M5:** Add score, restart, and a finish condition.
- **M6:** Add an instruction screen and polish the interface.

## Exercises
1. What happens if movement is updated once per rendered frame?
2. Explain position versus velocity.
3. Describe rectangle overlap in your own words.
4. Add a pause state without changing collision detection.

## Acceptance criteria
- Controls are explained to the player.
- The game can start, finish, and restart.
- Movement is not tied to a fixed rendering frame rate.
- Collision and scoring are reproducible.
- All images and sounds have compatible licences.

## Further study
- [Handmade Hero](https://handmadehero.org/)
- [Lazy Foo' SDL tutorials](http://lazyfoo.net/tutorials/SDL/)
- [LearnOpenGL: Breakout](https://learnopengl.com/In-Practice/2D-Game/Breakout)

External tutorials are linked, not copied.
