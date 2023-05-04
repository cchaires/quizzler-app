# Quizzler

This is a simple quiz game where questions with True/False answers are asked to the user, and the user can select either of the answers.

The project is composed of four modules: `main`, `data`, `question_model`, and `quiz_brain`. Also, it has an `ui` module that manages the user interface.

## Modules

### main
This module runs the main script of the game, which creates a `QuizBrain` instance and a `QuizInterface` instance. 

It creates a question bank by iterating over the questions provided by the `question_data` list in the `data` module. It also imports `Question` from the `question_model` module.

After that, it instantiates a `QuizBrain` object with the `question_bank` and a `QuizInterface` object with the `quiz`.

### data
This module uses the `requests` library to fetch questions from the Open Trivia Database API. It cleans the response data and stores it in a `question_data` list.

### question_model
This module defines the `Question` class with two attributes: `text` and `answer`. It initializes a question object with these attributes.

### quiz_brain
This module defines the `QuizBrain` class, which manages the questions and user answers.

It initializes the quiz with `question_number` and `score` variables, `question_list` list, and `current_question` variable.

It also has two methods: `still_has_questions` and `next_question`. The `still_has_questions` method returns a boolean indicating if there are still questions left to answer. The `next_question` method updates the `current_question` and returns the formatted string that represents the question number and text.

### ui
This module handles the graphical user interface using `tkinter` library. It defines a `QuizInterface` class that initializes the interface with the `QuizBrain` object.

It creates a `canvas` object to display the questions and two `buttons` for selecting the answers. It also defines other helper methods like `check_button`, `change_color`, `score_method`, and `finish`.

The `check_button` method checks whether the answer selected by the user is correct or not. It updates the `score` label's background color depending on whether the answer is correct or not.

The `change_color` method changes the background color of the window and `score` label depending on the feedback.

The `score_method` method updates the score displayed in the `score` label.

The `finish` method checks whether the quiz is completed or not. If completed, it disables the `buttons` and displays the final score.

## How to play
To play the game, simply run the `main` module in your Python environment. A window will pop up with the first question, and you can click on the `True` or `False` button to answer the question. After answering the question, the next question will appear. Once you've answered all the questions, the final score will be displayed.
