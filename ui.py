from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  #Parsing quizbrain alone, doesnt tell the program what type
        self.quiz = quiz_brain  # of file it is, so we import quizbrain and add :Quizbrain, so the only type
                                # of data that is parsed must be quiz brain. understand?
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzler")

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            width= 280,
            text="Sample Text",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, sticky="nsew")

        self.score_label = Label()
        self.score_label.config(text="Score: 0", font=("Arial", 15, "italic"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0, sticky="nsew")

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_button_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=lambda: self.answer_selected("false")
        )
        self.false_button.grid(column=1, row=2, pady=(20, 0))

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_button_image,
            bg=THEME_COLOR,
            highlightthickness=0, command=lambda: self.answer_selected("true")
        )
        self.true_button.grid(column=0, row=2, pady=(20, 0))

        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white", highlightcolor="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_selected(self, button_pressed):
        self.quiz.check_answer(button_pressed)
        score = self.quiz.score
        self.score_label.config(text=f"Score: {score}/10")
        answer = self.quiz.correct_answer
        if button_pressed == answer.lower():
            self.canvas.config(bg="green", highlightcolor="green")
        else:
            self.canvas.config(bg="red", highlightcolor="red")
        self.window.after(1000, self.get_next_question)


