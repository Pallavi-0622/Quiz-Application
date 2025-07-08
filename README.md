Quiz-Application

This repository contains a simple Python-based quiz application, along with some additional Python scripts. It is designed for basic practice and experimentation with Python file handling, database usage, and modular coding.

## 📁 Project Structure

test_code/
├── quiz/
│   ├─ quiz.py                    
│   ├─ quiz.db                    
│   └─ output-onlinepnftools.png  
│
├── app.py                         
├── file.py                        
├── pass.py                        
└── README.md                     

## 🎯 Features

- Console-based quiz game
- Questions are fetched from a SQLite database (`quiz.db`)
- Modular code split across multiple Python files
- Example UI image provided

## 🚀 How to Run

### 1. Run the quiz:
cd quiz
python quiz.py

> Make sure `quiz.db` exists in the same folder.

### 2. Run other scripts:
From the root directory:
python app.py
python file.py
python pass.py

## 🛠️ Tech Stack

- Python 3.x
- SQLite (for storing quiz questions)
- Command-line interface

## 🧾 Notes

- `output-onlinepnftools.png` likely shows a sample output or reference for the UI.
- If you want to modify questions, use any SQLite editor to edit `quiz.db`.

## 👩‍💻 Author

- [Pallavi-0622](https://github.com/Pallavi-0622)
