from importlib.resources import contents
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql 
import random as r
import re 
from database import create_connection
from tkinter import *
from tkinter import ttk
from merge import merge_sort
from BinarySearch import binary_search
session = None
conn = create_connection("database.db")
cur = conn.cursor()
LARGEFONT =("Verdana", 35)

def passwordcheck(passw):
    status = False
    if len(passw) < 8:
        print("Password must be 8 or more characters long")
    elif re.search("[0-9]",passw) is None:
        print("Password must have a number")
    elif re.search("[A-Z]",passw) is None:
        print("Password must have a capital letter")
    elif re.search("[^a-zA-z0-9]",passw) is None:
        print("Password must have a special character")
    else:
        print("Password meets requirements")
        status = True
    return status

def usernamecheck(usern):
    status = False
    if len(usern) <1:
        print("Username must not be blank!")
    else:
        print("Username meets requirements")
        status = True
    return status

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self)

        self.geometry("450x500")
        
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (args):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(args[0])
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.update()
        frame.tkraise()
  
# first window frame startpage


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.resizable(width=tk.FALSE, height=tk.FALSE)
        self.configure(bg="#FFFFFF")
        # controller.title("Login")

        label = tk.Label(
            self,
            text="The Wright Tool",
            width="35",
            bg="#FFFFFF",
            height="2",
            font=("Arial", 16),
        )
        label.grid(row=0, column=0)

        # create Login Button
        login_button = tk.Button(
            self,
            text="Teacher Login",
            bg="#31AFD4",
            height="2",
            width="30",
            font=("Arial",14),
            command=lambda: controller.show_frame(TeacherLogin),
        )
        login_button.grid(row=1, column=0, padx=0, pady=10)

        # create a register button
        register_button = tk.Button(
            self,
            text="Teacher Register",
            bg="#31AFD4",
            height="2",
            width="30",
            font=("Arial",14),
            command=lambda: controller.show_frame(TeacherRegister),
        )
        register_button.grid(row=2, column=0, padx=0, pady=10)

        student_login = tk.Button(
            self,
            text="Student Login",
            bg="#31AFD4",
            height="2",
            width="30",
            font=("Arial",14),
            command=lambda: controller.show_frame(StudentLogin),
        )
        student_login.grid(row=3, column=0, padx=0, pady=10)
        
        # create a quit button
        quit_button = tk.Button(
            self, 
            text="Quit",
            height="2",
            width="30",
            bg="#DD6E42",
            font=("Arial",14),
            command=controller.destroy,
        )
        quit_button.grid(row=4, column=0, padx=0, pady=50)


class TeacherLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#FFFFFF")
        label = tk.Label(
            self,
            text="Please login below!",
            bg="#FFFFFF",
            height="2",
        )
        label.grid(row=0, column=1, padx=10, pady=10)

        # Creating the username & password entry boxes
        self.username_text = tk.Label(self, text="Username:", font=("Arial", 13),bg="#FFFFFF")
        self.username_guess = tk.Entry(self, bg="#EEEEEE")
        self.password_text = tk.Label(self, text="Password:", font=("Arial", 15),bg="#FFFFFF")
        self.password_guess = tk.Entry(self, bg="#EEEEEE",
                                       show="✈")

        # Attempt to login button
        self.attempt_login = tk.Button(
            self,
            text="Login",
            width="10",
            height="1",
            bg="#99C24D",
            command=lambda: self.try_login(controller),
        )

        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 13),
            command=lambda: controller.show_frame(MainMenu),
        )

        self.username_text.grid(row=1, column=0, padx=10, pady=10)
        self.username_guess.grid(row=1, column=1, padx=10, pady=10)
        self.password_text.grid(row=2, column=0, padx=10, pady=10)
        self.password_guess.grid(row=2, column=1, padx=10, pady=10)
        self.attempt_login.grid(row=3, column=0, padx=10, pady=10)
        self.back_button.grid(row=4, column=0, sticky="w")

    def try_login(self, controller):  # checks if credentials are correct
        print("Trying to login...")
        statement = f"SELECT teachername FROM teachers WHERE teachername='{self.username_guess.get()}' AND password = '{self.password_guess.get()}';"
        cur.execute(statement)
        if not cur.fetchone():
            print("Login Failed")
        else:
            print("Welcome")
            teacher_iden = f"SELECT teacherid FROM teachers WHERE teachername='{self.username_guess.get()}' AND password = '{self.password_guess.get()}';"
            app = tkinterApp(TeacherMainMenu, Student_teacher, leader_board, Plane_menu, Class_menu, Quiz_add)
            app.mainloop()
 

class TeacherRegister(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self,
            text="Please Register below!",
            height="2",
            font=("Arial", 16),
        )
        label.grid(row=0, column=0)

        self.attempt_register = tk.Button(
            self,
            text="Register",
            width="10",
            height="1",
            font=("Arial", 13),
            command=lambda: self.try_register(controller),
        )
        label.grid(row=0, column=1)

                # Creating the username & password entry boxes
        self.username_text = tk.Label(self, text="Username:", font=("Arial", 13))
        self.username_input = tk.Entry(self)
        self.password_text = tk.Label(self, text="Password:", font=("Arial", 13))
        self.password_input = tk.Entry(self, show="*")

        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 13),
            command=lambda: controller.show_frame(MainMenu),
        )

        self.username_text.grid(row=1, column=0, padx=10, pady=10)
        self.username_input.grid(row=1, column=1, padx=10, pady=10)
        self.password_text.grid(row=2, column=0, padx=10, pady=10)
        self.password_input.grid(row=2, column=1, padx=10, pady=10)
        self.attempt_register.grid(row=3, column=0, padx=10, pady=10)
        self.back_button.grid(row=4, column=0, sticky="w")

    def try_register(self, controller):
        print("Trying to register...")
        iden = r.randint(0,9999)
        passw = self.password_input.get()
        usern = self.username_input.get()
        status = passwordcheck(passw)
        status2 = usernamecheck(usern)
        if status == True and status2 == True:
            statement = f"INSERT INTO teachers VALUES('{iden}','{self.username_input.get()}','{self.password_input.get()}','0');"
            cur.execute(statement)
            print("Registered!")
            conn.commit()
        else:
            print("Re-enter username and/or password")


class StudentLogin(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
            self,
            text="Please Login below!",
            height="2",
            font=("Arial", 16),
        )
        label.grid(row=0, column=0)

        self.attempt_student_login = tk.Button(
            self,
            text="Login",
            width="10",
            height="1",
            font=("Arial", 13),
            command=lambda: self.try_student_login(controller),
        )
        label.grid(row=0, column=1)
                # Creating the username & password entry boxes
        self.username_text = tk.Label(self, text="Username:", font=("Arial", 13))
        self.username_guess = tk.Entry(self)
        self.password_text = tk.Label(self, text="Password:", font=("Arial", 13))
        self.password_guess = tk.Entry(self, show="*")
  
        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 13),
            command=lambda: controller.show_frame(MainMenu),      
        )

        self.username_text.grid(row=1, column=0, padx=10, pady=10)
        self.username_guess.grid(row=1, column=1, padx=10, pady=10)
        self.password_text.grid(row=2, column=0, padx=10, pady=10)
        self.password_guess.grid(row=2, column=1, padx=10, pady=10)
        self.attempt_student_login.grid(row=3, column=0, padx=10, pady=10)
        self.back_button.grid(row=4, column=0, sticky="w")

    def try_student_login(self, controller):
        global session
        # checks if credentials are correct
        print("Trying to login...")
        statement = f"SELECT studentname FROM students WHERE studentname='{self.username_guess.get()}' AND password = '{self.password_guess.get()}';"
        cur.execute(statement)
        if not cur.fetchone():
            print("Login Failed")
        else:
            print("Welcome")
            student_iden = f"SELECT studentname FROM students WHERE studentname='{self.username_guess.get()}' AND password = '{self.password_guess.get()}';"
            studentid = f"SELECT studentid FROM students WHERE studentname='{self.username_guess.get()}' AND password = '{self.password_guess.get()}';"
            cur.execute(studentid)
            session = cur.fetchone()[0]
            print(session)
            app = tkinterApp(Quiz, Student_menu)
            app.mainloop() 
            

class TeacherMainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.resizable(width=tk.TRUE, height=tk.TRUE)
        # controller.title("Login")

        label = tk.Label(
            self,
            text="Teacher Zone",
            width="35",
            height="2",
            font=("Arial", 14),
        )
        label.grid(row=0, column=0)

        # student zone for teachers
        Student_button = tk.Button(
            self,
            text="Student area",
            bg="#DCDCDC",
            height="2",
            width="30",
            font=("Arial", 13),
            command=lambda: controller.show_frame(Student_teacher),
        )
        Student_button.grid(row=1, column=0, padx=0, pady=20)

        Add_plane = tk.Button(
            self,
            text="Add plane",
            bg="#DCDCDC",
            height="2",
            width="30",
            font=("Arial", 13),
            command=lambda: controller.show_frame(Plane_menu),
        )
        Add_plane.grid(row=3, column=0, padx=0, pady=20)

        Class_menu_btn = tk.Button(
            self,
            text="Class menu",
            bg="#DCDCDC",
            height="2",
            width="30",
            font=("Arial",14),
            command=lambda: controller.show_frame(Class_menu),
        )
        Class_menu_btn.grid(row=2, column=0, padx=0, pady=20)
        
        # create a quit button
        quit_button = tk.Button(
            self,
            text="Quit",
            height="2",
            width="30",
            bg="#FF775A",
            font=("Arial", 13),
            command=controller.destroy,
        )
        quit_button.grid(row=4, column=0, padx=0, pady=20)


        
class Student_teacher(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
            self,
            text="Student area",
            height="2",
            font=("Arial", 14),
        )
        label.grid(row=0, column=0)
        # Creating the username & password entry boxes
        self.SetStudentUsername_text = tk.Label(self, text="Set Student Username:", font=("Comic Sans MS", 13))
        self.SetStudentUsername_guess = tk.Entry(self)
        self.SetStudentPassword_text = tk.Label(self, text="Set Student Password:", font=("Comic Sans MS", 13))
        self.SetStudentPassword_guess = tk.Entry(self, show="*")

        # Attempt to login button
        self.attempt_create_account = tk.Button(
            self,
            text="Create",
            width="10",
            height="1",
            font=("Arial", 13),
            command=lambda: self.try_register(controller),
        )
        
        self.view_scores = tk.Button(
            self,
            text="View Student Leaderboard",
            bg="#DCDCDC",
            height="2",
            width="30",
            font=("Arial",14),
            command=lambda: controller.show_frame(leader_board)
        )

        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 13),
            command=lambda: controller.show_frame(TeacherMainMenu),
        )

        self.SetStudentUsername_text.grid(row=1, column=0, padx=10, pady=10)
        self.SetStudentUsername_guess.grid(row=1, column=1, padx=10, pady=10)
        self.SetStudentPassword_text.grid(row=2, column=0, padx=10, pady=10)
        self.SetStudentPassword_guess.grid(row=2, column=1, padx=10, pady=10)
        self.attempt_create_account.grid(row=3, column=0, padx=10, pady=10)
        self.view_scores.grid(row=4, column=1, padx=10, pady=10)
        self.back_button.grid(row=5, column=0, sticky="w")

    def try_register(self, controller):
        print("Trying to register...")
        iden = r.randint(0,9999)
        passw = self.SetStudentPassword_guess.get()
        usern = self.SetStudentUsername_guess.get()
        status = passwordcheck(passw)
        status2 = usernamecheck(usern)
        if status == True and status2 == True:
            statement = f"INSERT INTO students VALUES('{iden}','{self.SetStudentUsername_guess.get()}','{self.SetStudentPassword_guess.get()}','0','0','0');"
            cur.execute(statement)
            print("Registered!")
            conn.commit()
        else:
            print("Re-enter username and/or password")



class leader_board(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent)
        label = tk.Label(
            self,
            text="Student Leader Board",
            height="2",
            font=("Arial",16),
        )
        label.grid(row=0, column=0)

        columns = ("studentid", "studentname", "answersattempted", "answerscorrect")
        tree = ttk.Treeview(self, columns=columns, show="headings")

        tree.heading("studentid", text="Student ID")
        tree.heading("studentname", text="Student Name")
        tree.heading("answersattempted", text="Answers Attempted")
        tree.heading("answerscorrect", text="Answers Correct")

        tree.grid(row=1, column=0, stick=tk.NSEW)
        
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.sortdata(tree)

    def sortdata(self, tree):
        students = []
        sorted_list = []
        statement = """SELECT questionscorrect FROM students"""
        cur.execute(statement)
        unsorted = cur.fetchall()
        print(unsorted)
        sorted_list = merge_sort(unsorted)
        print(sorted_list)
        for score in sorted_list:
            statement = "SELECT studentid FROM students WHERE questionscorrect = {}".format(score[0])
            cur.execute(statement)
            student = cur.fetchone()
            students.append(student)
        for student in students:
            tree.insert("", tk.END, values=student)


    

class Plane_menu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
            self,
            text="Aeroplane area",
            height="2",
            font=("Arial",16),
        )
        label.grid(row=0, column=0)
        #creating the plane info entry boxes
        self.SetPlaneName_text = tk.Label(self, text="Set Aeroplane Name:", font=("Comic Sans MS", 13))
        self.SetPlaneName_entry = tk.Entry(self)
        self.SetPlaneVelocity_text = tk.Label(self, text="Set Aeroplane Velocity:", font=("Comic Sans MS", 13))
        self.SetPlaneVelocity_entry = tk.Entry(self)
        self.SetPlaneWingSpan_text = tk.Label(self, text="Set Aeroplane Wingspan:", font=("Comic Sans MS", 13))
        self.SetPlaneWingSpan_entry = tk.Entry(self)

        self.attempt_create_plane = tk.Button(
            self,
            text="Create",
            width="10",
            height="1",
            font=("Arial", 14),
            command=lambda: self.try_add(controller),
        )

        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 14),
            command=lambda: controller.show_frame(TeacherMainMenu),
        )

        self.SetPlaneName_text.grid(row=1, column=0, padx=10, pady=10)
        self.SetPlaneName_entry.grid(row=1, column=1, padx=10, pady=10)
        self.SetPlaneVelocity_text.grid(row=2, column=0, padx=10, pady=10)
        self.SetPlaneVelocity_entry.grid(row=2, column=1, padx=10, pady=10)
        self.SetPlaneWingSpan_text.grid(row=3, column=0, padx=10, pady=10)
        self.SetPlaneWingSpan_entry.grid(row=3, column=1, padx=10, pady=10)
        self.attempt_create_plane.grid(row=4, column = 1, padx=10, pady=10)
        self.back_button.grid(row=4, column=0, sticky="w")

    def try_add(self, controller):
        print("Tring to add...")
        iden = r.randint(0,9999)
        statement = f"INSERT INTO planes VALUES('{self.SetPlaneName_entry.get()}','{self.SetPlaneVelocity_entry.get()}','{self.SetPlaneWingSpan_entry.get()}');"
        cur.execute(statement)
        print("Added!")
        conn.commit()


class Class_menu(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
            self,
            text="Classroom menu",
            height="2",
            font=("Arial",16),
        )
        label.grid(row=0, column=0)

        self.class_quiz_btn = tk.Button(
            self,
            text="Questions",
            height="2",
            font=("Arial",14),
            command=lambda: controller.show_frame(Quiz_add),

        )

        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 14),
            command=lambda: controller.show_frame(TeacherMainMenu),
        )
        self.class_quiz_btn.grid(row=3, column=1, padx=10, pady=10)
        self.back_button.grid(row=4, column=0, sticky="w")

class Quiz_add(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(
            self,
            text="Quiz question add",
            width="35",
            height="2",
            font=("Arial",16),
        )
        label.grid(row=0, column=0)

        self.SetQuestion_text = tk.Label(self, text = "Set Question Phrasing: ", font=("Arial",14))
        self.setQuestion_guess = tk.Entry(self)
        self.setAnswer_text = tk.Label(self, text = "Set Question Answer ", font =("Arial",14))
        self.setAnswer_guess = tk.Entry(self)
        self.SetFalse1_text = tk.Label(self, text = "Set False Answer: ", font=("Arial",14))
        self.setFalse1_guess = tk.Entry(self)       
        self.SetFalse2_text = tk.Label(self, text = "Set Second False Answer: ", font=("Arial",14))
        self.setFalse2_guess = tk.Entry(self)

        self.attempt_create_question = tk.Button(
            self,
            text="Create",
            width="10",
            height="1",
            font=("Arial",13),
            command=lambda: self.add_quiz(controller)
        )

        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 13),
            command=lambda: controller.show_frame(Class_menu)
        )

        self.SetQuestion_text.grid(row=1, column=0, padx=10, pady=10)
        self.setQuestion_guess.grid(row=2, column=0, padx=10, pady=10)
        self.setAnswer_text.grid(row=3, column=0, padx=10, pady=10)
        self.setAnswer_guess.grid(row=4, column=0, padx=10, pady=10)
        self.SetFalse1_text.grid(row=5, column=0, padx=10, pady=10)
        self.setFalse1_guess.grid(row=6, column=0, padx=10, pady=10)
        self.SetFalse2_text.grid(row=7, column=0, padx=10, pady=10)
        self.setFalse2_guess.grid(row=8, column=0, padx=10, pady=10)
        self.attempt_create_question.grid(row=9, column=0, sticky="e")
        self.back_button.grid(row=10, column=0, sticky="w")

    def add_quiz(self, container):
        print("Attempting to add question")
        iden = r.randint(0,9999)
        qtext = self.setQuestion_guess.get()
        qanswer = self.setAnswer_guess.get()
        qfalse1 = self.setFalse1_guess.get()
        qfalse2 = self.setFalse2_guess.get()
        statement = f"INSERT INTO quiz VALUES('{iden}','{qtext}','{qanswer}','{qfalse1}','{qfalse2}');"
        cur.execute(statement)
        print("Added!")
        conn.commit()





class Student_menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        controller.resizable(width=tk.TRUE, height=tk.TRUE)

        label = tk.Label(
            self,
            text="Student Zone",
            width="35",
            height="2",
            font=("Arial", 16),
        )
        label.grid(row=0, column=0)

        Quiz_zone = tk.Button(
            self,
            text="Quiz zone",
            bg="#DCDCDC",
            height="2",
            width="30",
            font=("Arial", 14),
            command=lambda: controller.show_frame(Quiz),
        )
        Quiz_zone.grid(row=1, column=0, padx=0, pady=20)

        lift_equation = tk.Button(
            self,
            text="Takeoff / landing guide",
            bg="#DCDCDC",
            height="2",
            width="30",
            font=("Arial", 14),
            command=lambda: controller.show_frame(Lift_equation),
        )
        lift_equation.grid(row=3, column=0, padx=0, pady=20)


        self.back_button = tk.Button(
            self,
            text="Back",
            bg="#FF775A",
            width="5",
            height="2",
            font=("Arial", 14),
            command=lambda: controller.show_frame(MainMenu),
        )

        quit_button = tk.Button(
            self,
            text="Quit",
            height="2",
            width="30",
            bg="#FF775A",
            font=("Arial", 14),
            command=controller.destroy,
        )
        quit_button.grid(row=4, column=0, padx=0, pady=20)

class Lift_equation(tk.Frame):
    def __init__ (self,parent,controller):
        tk.Frame.__init__(self,parent)
        controller.resizable(width=tk.TRUE,height=tk.TRUE)

        label = tk.Label(
            self,
            text="Lift Equation",
            width="35",
            height="2",
            font=("Arial",16)
        )
        label.grid(row=0, column=1)

        

        


class Quiz(tk.Frame):
    def __init__ (self,parent,controller):
        tk.Frame.__init__(self,parent)
        controller.resizable(width=tk.TRUE,height=tk.TRUE)
        
        def random_q():
            qnumrandom = r.randint(0,10)
            return qnumrandom
            
        label = tk.Label(
            self,
            text="Quiz",
            width="35",
            height="2",
            font=("Arial",16)
            )
        label.grid(row=0, column=1)
        
        statement= f"SELECT questionsattempted FROM students WHERE studentid = {session}"
        cur.execute(statement)
        cur.fetchone()[0]

        
        attempted = tk.Label(
            self,
            text="Questions attempted: "+statement,
            height="1",
            width="15",
            bg="#DCDCDC",
            font=("Arial",7),
        )
        attempted.grid(row=2, column=0, padx=10, pady=10)

        statement=f"SELECT questionscorrect FROM students WHERE studentid = {session}"
        cur.execute(statement)
        cur.fetchone()[0]

        correct = tk.Label(
            self,
            text="Questions correct:"+statement,
            height="2",
            width="15",
            bg="#DCDCDC",
            font=("Arial",7),
        )
        correct.grid(row=2, column=2, padx=10, pady=10)
        qnumrandom = random_q()
        statement =f"SELECT qtext FROM quiz WHERE qnum = {qnumrandom}"
        cur.execute(statement)
        statement = cur.fetchone()

        questionname = tk.Label(
            self,
            text=statement,
            height="2",
            width="30",
            bg="#DCDCDC",
            font=("Arial",14),
        )
        correct.grid(row=2, column=1, padx=10, pady=10)


        #Question already chosen by random statement above, order of buttons will be randomised
        
        statement=f"SELECT fakeanswer FROM quiz WHERE qnum = {qnumrandom}"
        cur.execute(statement)

        def answrong():
            statement=f"SELECT questionsattempted FROM students WHERE studentid = {session}"
            cur.execute(statement)
            statement=cur.fetchone()[0]
            statement+=1
            sstatement = f"UPDATE students SET questionsattempted = {statement} WHERE studentid={session}"
            cur.execute(sstatement)
            #controller.show_frame(Quiz)

        def ansright():
            statement=f"SELECT questionsattempted FROM students WHERE studentid = {session}"
            cur.execute(statement)
            statement = cur.fetchone()[0]
            statement+=1
            sstatement=f"UPDATE students set questionsattempted = {statement} WHERE studentid = {session}"
            cur.execute(sstatement)
            statement=f"SELECT questionscorrect FROM students WHERE studentid = {session}"
            cur.execute(statement)
            statement= cur.fetchone()[0]
            statement+=1
            sstatement=f"UPDATE students set questionscorrect = {statement} WHERE studentid = {session}"
            cur.execute(sstatement)
            #controller.show_frame(Quiz)


        statement=f"SELECT fakeanswer FROM quiz WHERE qnum = {qnumrandom}"
        cur.execute(statement)
        statement = cur.fetchone()[0]

        ansincorrect1 = tk.Button(
            self,
            text=statement,
            height="2",
            width="30",
            bg="#DCDCDC",
            font=("Arial",14),
            command=answrong()
            )

        statement=f"SELECT fakeranswer FROM quiz WHERE qnum = {qnumrandom}"
        cur.execute(statement)
        statement = cur.fetchone()

        ansincorrect2 = tk.Button(
            self,
            text=statement,
            height="2",
            width="30",
            bg="#DCDCDC",
            font=("Arial",14),
            command=answrong()
            )

        statement=f"SELECT answer FROM quiz WHERE qnum = {qnumrandom}"
        cur.execute(statement)
        statement = cur.fetchone()

        anscorrect = tk.Button(
            self,
            text=statement,
            height="2",
            width="30",
            font=("Arial",14),
            command=ansright()
            )

        chance = r.randint(0,5)

        if chance == 0:
            anscorrect.grid(row=2, column=1, padx=10, pady=10)
            ansincorrect1.grid(row=3, column=1, padx=10, pady=10)
            ansincorrect2.grid(row=4, column=1, padx=10, pady=10)
        elif chance == 1:
            anscorrect.grid(row=2, column=1, padx=10, pady=10)
            ansincorrect1.grid(row=4, column=1, padx=10, pady=10)
            ansincorrect2.grid(row=3, column=1, padx=10, pady=10)
        elif chance== 2:
            anscorrect.grid(row=3, column=1, padx=10, pady=10)
            ansincorrect1.grid(row=2, column=1, padx=10, pady=10)
            ansincorrect2.grid(row=4, column=1, padx=10, pady=10)
        elif chance == 3:
            anscorrect.grid(row=4, column=1, padx=10, pady=10)
            ansincorrect1.grid(row=2, column=1, padx=10, pady=10)
            ansincorrect2.grid(row=3, column=1, padx=10, pady=10)
        elif chance == 4:
            anscorrect.grid(row=2, column=1, padx=10, pady=10)
            ansincorrect1.grid(row=4, column=1, padx=10, pady=10)
            ansincorrect2.grid(row=2, column=1, padx=10, pady=10)
        elif chance == 5:
            anscorrect.grid(row=4, column=1, padx=10, pady=10)
            ansincorrect1.grid(row=3, column=1, padx=10, pady=10)
            ansincorrect2.grid(row=2, column=1, padx=10, pady=10)
        else:
            print("Broken")

                
            
                
            











        
            
            
        

        
        


if __name__ == "__main__":
    app = tkinterApp(MainMenu, TeacherLogin, TeacherRegister, StudentLogin, TeacherMainMenu, Student_teacher, leader_board, Plane_menu, Class_menu, Quiz_add, Student_menu)

    app.mainloop()
