# Iran Provinces Game

A simple Python game for learning the provinces of Iran using Turtle and Pandas.

## Features

* Guess the names of Iran's provinces
* Display correctly guessed provinces on the map
* Track the number of correct guesses
* Handle different Persian/Arabic character forms
* Save the provinces that were not guessed correctly
* Use a map of Iran as the game background

## Technologies

* Python
* Turtle
* Pandas
* CSV
* File I/O

## Project Structure

```text
iran-provinces-game/
├── main.py
├── province.csv
├── Iran.gif
├── .gitignore
└── README.md
```

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Install Pandas:

```bash
pip install pandas
```

4. Run the game:

```bash
python main.py
```

## How to Play

* Enter the name of an Iranian province in the input box.
* If the answer is correct, the province name will appear on the map.
* Continue guessing until all provinces are found.
* Type `Exit` to stop the game.
* When the game is exited, the provinces that were not guessed are saved in `provinces_to_learn.csv`.

## Data

The `province.csv` file contains:

* Province names
* X coordinates
* Y coordinates

These coordinates are used to place each province name in the correct position on the map.

## What I Practiced

This project helped me practice:

* Reading CSV files with Pandas
* Working with DataFrames
* Filtering DataFrame rows
* Working with lists
* Loops and conditions
* Functions
* String normalization
* File handling
* Using the Turtle library
* Basic data processing
* Separating data from program logic
