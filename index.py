from tkinter import *

WHITE = "#FFFFFF"
LIGHT_GRAY = "#F0F0F0"
BLUE = "#3282F6"
LARGE_TEXT = ("Arial",26,"bold")
NORMAL_TEXT = ("Arial",15,"bold")

class Calculator:
    
    digit_flag = 1
    operator_flag = 1
    
    def __init__(self):
        self.total_expression = ""
        self.current_expression = "0"

        self.root = Tk()
        self.root.title("My first Calculator")

        self.display_frame = Frame(self.root,bg=LIGHT_GRAY)
        self.display_frame.pack(expand=True,fill="both")

        self.button_frame = Frame(self.root,bg=LIGHT_GRAY)
        self.button_frame.pack(expand=True,fill="both")

        for x in range(1,5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)

        self.total_label = Label(self.display_frame,anchor=E,text=self.total_expression,font=NORMAL_TEXT,fg=BLUE)
        self.total_label.pack(expand=True,fill="both")

        self.current_label = Label(self.display_frame,anchor=E,text=self.current_expression,font=LARGE_TEXT)
        self.current_label.pack(expand=True,fill="both")
        
        self.create_digits_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_clear_entry_button()
        self.create_equal_button()


    def create_digits_buttons(self):
        digits = {7:(1,1),8:(1,2),9:(1,3),
                  4: (2,1),5:(2,2),6:(2,3),
                  1:(3,1),2:(3,2),3:(3,3),
                  0:(4,1),'.':(4,2)}

        for digit,pos in digits.items():
            button = Button(self.button_frame,
                            text=digit,
                            font=LARGE_TEXT,
                            fg=BLUE,
                            bg=WHITE,
                            borderwidth=0,
                            command=lambda x = str(digit):self.add_digits(x))
            button.grid(row=pos[0],column=pos[1],sticky=NSEW)
            
    def create_operator_buttons(self):
        operators = {"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        i = 0
        for operator,symbol in operators.items():
            
            button = Button(self.button_frame,
                            text=symbol,
                            font=LARGE_TEXT,
                            bg=WHITE,
                            fg=BLUE,
                            borderwidth=0,
                            command=lambda x=operator:self.add_operators(x))
            button.grid(row=i,column=4,sticky=NSEW)
            i += 1

    def create_equal_button(self):
        button = Button(self.button_frame,
                            text="=",
                            font=LARGE_TEXT,
                            bg=BLUE,
                            fg=WHITE,
                            borderwidth=0,
                            command=lambda:self.equal_button())
        button.grid(row=4,column=3,columnspan=2,sticky=NSEW)
    
    def create_clear_button(self):
        button = Button(self.button_frame,
                            text="C",
                            font=NORMAL_TEXT,
                            borderwidth=0,
                            command=lambda:self.clear_button()
                            )
        button.grid(row=0,column=1,columnspan=2,sticky=NSEW)
    
    def create_clear_entry_button(self):
        button = Button(self.button_frame,
                            text="CE",
                            font=NORMAL_TEXT,
                            borderwidth=0,
                            command=lambda:self.clear_entry_button()
                            )
        button.grid(row=0,column=3,sticky=NSEW)
      
    def update_current_label(self):
        self.current_label.config(text=self.current_expression)
        
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)
        
    def add_digits(self,digit):
        if self.current_expression == "0":
            self.current_expression = ""
            
        if self.digit_flag == 1:
            self.current_expression += digit
        else:
            self.current_expression = digit
            self.digit_flag = 1
        self.total_expression += digit
        
        self.update_current_label()
        self.update_total_label()
        
        
    def add_operators(self,operator):
        
        if self.operator_flag == 1:
            self.total_expression += operator
            self.operator_flag = 0
        elif self.digit_flag == 1:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = self.current_expression + operator
        else:
            self.total_expression = self.total_expression[:-1]
            self.total_expression += operator
        self.update_total_label()
        self.update_current_label()
        self.digit_flag = 0
        
    def equal_button(self):
        if self.digit_flag == 1 and self.operator_flag == 0 :
            self.current_expression = str(eval(self.total_expression))
            self.update_current_label()
    
    def clear_button(self):
        self.current_expression = "0"
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()
        self.digit_flag = 1
        self.operator_flag = 1
    
    def clear_entry_button(self):
        if self.digit_flag == 0 and self.operator_flag == 0:
            self.total_expression = self.total_expression[:-1]
            self.current_expression = self.total_expression
            self.digit_flag = 1
            self.operator_flag = 1
         
        elif self.digit_flag == 1 and self.operator_flag == 0:
            length = len(self.current_expression)
            self.total_expression = self.total_expression[:-length]
            self.current_expression = ""
            self.digit_flag = 0
        self.update_current_label()
        self.update_total_label()  
         
    def run(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    calc = Calculator()
    calc.run()

