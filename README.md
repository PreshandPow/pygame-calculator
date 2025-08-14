Pygame Calculator
I created a graphical calculator built with Python's Pygame library. This project implements a full-featured calculator with a friendly UI, designed to handle standard arithmetic operations, operator precedence, and parentheses using Reverse Polish Notation to handle calculations.

I believe the core of this calculator is its robust parsing engine, which uses the Shunting-yard algorithm to convert infix expressions to Reverse Polish Notation (RPN). This RPN expression is then evaluated using a stack-based algorithm, ensuring all calculations adhere to BIDMAS/PEMDAS rules.

Key Features
  - Operator Precedence: Correctly handles the order of operations for addition, subtraction, multiplication, division, and exponents.

  - Parentheses Support: Enables complex calculations by correctly parsing expressions within parentheses.

  - Error Handling: Catches common errors such as division by zero and mismatched parentheses, providing a better user experience.

  - Object-Oriented Design: The code is structured using classes for the calculator and buttons, which improved modularity and reduced redundancy.

What I Learned
  - This project was a deep dive into several fundamental computer science concepts. I gained practical experience with:

  - Algorithms: Implementing the Shunting-yard algorithm for expression parsing.

  - Data Structures: Gaining familiarity with using stacks and dictionaries for managing operators and precedence.

  - Object-Oriented Programming (OOP): Creating a modular design with a Button class and private attributes.

  - Testing and Debugging: Developing a systematic approach to identifying and fixing bugs to improve the overall user experience.

How to Run
  1. Clone the repository to your local machine.

  2. Install Pygame: pip install pygame

  3. Run the main.py file.

This project took approximately 5 hours to complete and served as an excellent exercise in building a complete, functional application from scratch.
