# BookBot

BookBot is my first Boot.dev project! It is a simple Python command-line tool that analyses text files (like books) and generates statistical reports about their contents.

## Features

- Word Count: Calculates the total number of words in a given text file.

- Character Frequency: Counts the occurrences of each alphabetical character, ignoring case, and sorts them from most frequent to least frequent.

- Clean Output: Generates a formatted, easy-to-read report directly in your terminal.

## Prerequisites

- Python 3.x

## Usage

You can run BookBot from the command line by passing the path to the text file you want to analyse.

```
python3 main.py <path_to_book>
```

**Example:**
If you have a text file located at ```books/frankenstein.txt```, you would run:

```
python3 main.py books/frankenstein.txt
```


## Project Structure
- ```main.py```: The main entry point for the application. It handles user input, coordinates the analysis, and prints the formatted report.
- ```stats.py```: Contains the core logic and helper functions for reading files, counting words, and tallying character frequencies.
- ```.gitignore```: Configured to ignore the ```__pycache__``` directory and any text files stored in the ```/books``` folder.
