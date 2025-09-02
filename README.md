# Python Practice Projects

A collection of small Python projects for practicing programming concepts and building simple applications.

## Included Projects

- **ticTacToe.py**  
  Classic Tic-Tac-Toe game in the console.

- **textCalculator.py**  
  Converts numbers written in words into digits and performs calculations.

- **quizz.py + questions.json**  
  A simple quiz system that loads questions from JSON and tracks user answers.

- **management.py + contacts.json**  
  Basic management system for handling simple data records.

- **basicGameFlow.py**  
  A minimal game loop with control flow and interaction handling.

- **image_to_pdf_gui.py**  
  Converts images to PDF through a graphical user interface (PyInstaller spec included).

- **PDF-to-Images Tool**  
  A desktop program that converts PDF files into images, useful for document processing workflows.

## Repository Structure
├─ basicGameFlow.py # Basic game loop with control handling

├─ contacts.json # Sample data for management system

├─ image_to_pdf_gui.py # Image to PDF converter with GUI

├─ image_to_pdf_gui.spec # PyInstaller build spec for the GUI app

├─ management.py # Simple management system

├─ questions.json # Question bank for quiz system

├─ quizz.py # Quiz app

├─ textCalculator.py # Word-to-number calculator

├─ ticTacToe.py # Tic-Tac-Toe game

├─ dist/image_to_pdf_gui/ # PDF to Images desktop tool

└─ README.md

## Requirements

- Python 3.10+  
- Standard library only (no external dependencies, except GUI projects which may use Tkinter/PyInstaller)

## How to Run

Run any project directly with Python:

```bash
python ticTacToe.py
python textCalculator.py
python quizz.py
python management.py