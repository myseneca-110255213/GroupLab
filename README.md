# Group 5 - Group Lab

## <p style="text-align: center;">Table of Contents</p>
1. [**How the Game Works**](#game)
   
   * [**Functions**](#func)
   * [**Mechanics**](#mech)
   * [**Game Loop**](#loop)

2. [**Group Member Roles**](group)
    
    * [**Gitesh**](#G)
    * [**Simran**](#S)
    * [**Michael**](#M)

## <p style="text-align: center;"> How the Game Works </p> <a name="game"> </a>

### Functions <a name="func"> </a>
**clear():**

    Runs a system command to clear the terminal.

**rockpaperscissor_instructions():**

    Defines the rules for Rock, Paper, Scissors through a series of print statements.

### Mechanics <a name="mech"> </a>
*A special function will contain the majority of the games mechanics.*

**rockpaperscissor():**

    - First, define a list containing the titular "Rock, Paper, and Scissors."
    - Second create a user defined variable and check that variable to ensure it contains only an item matching the above list.
    - Using nested if statements, compare the user defined variable against the computer generated one:
    - Print out an appropriate statement for whether the user wins, the computer wins, or there is a draw.

### Game Loop <a name="loop"> </a>

**While True:**

    - print out a menu showing the player 3 options:
      - 1 to play,
      - 2 to quit,
      - 3 to view the instructions.
    - Use a try/except statement to ensure the player chooses a viable option.
    - If the player chooses 1:
      - Call clear() and rockpaperscissor().
    - If the player chooses 2:
      - End the loop.
    - If the player chooses 3:
      - Call clear() and rockpaperscissor_instructions().
    - Finally if the user inputs an invalid choice, return an error.

## <p style="text-align: center;"> Group Member Roles </p> <a name="group"> </a>

### Gitesh <a name="G"> </a>

### Simran <a name="S"> </a>

### Michael <a name="M"> </a>