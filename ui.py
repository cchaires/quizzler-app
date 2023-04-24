import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(345, 490)
        # Canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Text so long to see if theres wrapping the text",
                                                     font=("arial", 20, "italic"),
                                                     width=290,
                                                     justify="center"
                                                     )
        # Label
        self.score = tkinter.Label(text="Score: 0",
                                   font=("arial", 14, "normal"),
                                   bg=THEME_COLOR,
                                   fg="white",
                                   anchor="e"
                                   )
        self.score.grid(column=1, row=0, pady=(0, 20))
        # Images
        img_true = tkinter.PhotoImage(file="images/true.png")
        img_false = tkinter.PhotoImage(file="images/false.png")
        # Buttons
        self.true_button = tkinter.Button(image=img_true,
                                          highlightthickness=0,
                                          bg=THEME_COLOR,
                                          command=lambda: self.check_button(0)
                                          )
        self.true_button.grid(column=0, row=2, pady=(40, 20), padx=(0, 20))
        self.false_button = tkinter.Button(image=img_false,
                                           highlightthickness=0,
                                           bg=THEME_COLOR,
                                           command=lambda: self.check_button(1)
                                           )
        self.false_button.grid(column=1, row=2, pady=(40, 20), padx=(20, 0))
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.window.config(bg=THEME_COLOR)
        self.score_method()
        self.finish()

    def check_button(self, button):
        answer = "True" if button == 0 else "False"
        if self.quiz.check_answer(answer):
            self.change_color(True)
        else:
            self.change_color(False)
        self.window.after(1000, self.get_next_question)

    def change_color(self, feedback):
        if feedback:
            self.window.config(bg="green")
            self.score.config(bg="green")
        else:
            self.window.config(bg="red")
            self.score.config(bg="red")

    def score_method(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.score.config(bg=THEME_COLOR)

    def finish(self):
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\nYour Final Score was: "
                                                            f"{self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button["state"] = tkinter.DISABLED
            self.false_button["state"] = tkinter.DISABLED
