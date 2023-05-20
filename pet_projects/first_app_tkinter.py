from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pickle
import pymysql


root = Tk()

def newwindow():
        def add_digit(digit):
                value = calc.get()
                if value[0] == '0' and len(value)==1:
                        value = value[1:]
                calc['state'] = NORMAL
                calc.delete(0, 'end')
                calc.insert(0, value+str(digit))
                calc['state'] = DISABLED
        
        def add_operation(operation):
                value = calc.get()
                if value[-1] in '-+/*':
                        value = value[:-1]
                if '+' in value or '-' in value or '/' in value or '*' in value:
                        calculate()
                        value = calc.get()
                calc['state'] = NORMAL
                calc.delete(0, 'end')
                calc.insert(0, value+operation)
                calc['state'] = DISABLED

        def calculate():
                value = calc.get()
                if value[-1] in '+-/*':
                        value = value + value[:-1]
                calc['state'] = NORMAL
                calc.delete(0, 'end')
                try:
                        calc.insert(0, eval(value))
                        calc['state'] = DISABLED
                except (NameError, SyntaxError):
                        messagebox.showinfo('ERROR', 'ENTER ONLY NUMBERS')
                        calc.insert(0, 0)
                except ZeroDivisionError:
                        messagebox.showinfo('ERROR', 'You are serious? It is zero, maaaan')
                        calc.insert(0, 0)


        def clear():
                calc['state'] = NORMAL
                calc.delete(0, 'end')
                calc.insert(0,0)
                calc['state'] = DISABLED


        def make_digit_button(digit):
                return Button(win1, text=digit, bg='black', fg='#fdfdfd', bd=5, font=('Arial', 13, 'bold'), command= lambda : add_digit(digit))
        
        def make_operation_button(operation):
                return Button(win1, text=operation, bg='black', bd=5, fg='red', font=('Arial', 13, 'bold'), command= lambda : add_operation(operation))

        def make_calc_button(operation):
                return Button(win1, text=operation, bg='black', bd=5, fg='#fdfdfd', font=('Arial', 13, 'bold'), command = lambda : calculate())

        def make_clear_button(operation):
                return Button(win1, text=operation, bg='black', bd=5, fg='red', font=('Arial', 13, 'bold'), command = lambda : clear())

        def press_key(event):
                #print(repr(event.char))
                if event.char.isdigit():
                        add_digit(event.char)
                elif event.char in '+*-/':
                        add_operation(event.char)
                elif event.char == '\r':
                        calculate()
                elif event.char == '\x1b':
                        clear()



        win1 = Tk()
        win1['bg'] = '#121212'
        #logo1 = PhotoImage(file='cal1.png')
        win1.title('Calculator')
        #win1.iconphoto(False, logo1)
        win1.geometry(f'240x290+100+200')
        win1.resizable(False, False)

        calc = Entry(win1, font= ('Arial', 15, 'bold'), width=18, relief=RAISED, bd=7, justify=RIGHT)
        calc.insert(0, '0')
        #calc['bg'] = 'black'
        calc['state'] = DISABLED
        calc.grid(row=0, column=0, columnspan=4, stick = 'we', padx=5, pady=5)



        win1.bind('<Key>', press_key)      
        
        make_digit_button(1).grid(row=1, column=0, stick='wens', padx=5, pady=5)
        make_digit_button(2).grid(row=1, column=1, stick='wens', padx=5, pady=5)
        make_digit_button(3).grid(row=1, column=2, stick='wens', padx=5, pady=5)
        make_digit_button(4).grid(row=2, column=0, stick='wens', padx=5, pady=5)
        make_digit_button(5).grid(row=2, column=1, stick='wens', padx=5, pady=5)
        make_digit_button(6).grid(row=2, column=2, stick='wens', padx=5, pady=5)
        make_digit_button(7).grid(row=3, column=0, stick='wens', padx=5, pady=5)
        make_digit_button(8).grid(row=3, column=1, stick='wens', padx=5, pady=5)
        make_digit_button(9).grid(row=3, column=2, stick='wens', padx=5, pady=5)
        make_digit_button(0).grid(row=4, column=0, stick='wens', padx=5, pady=5)


        make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
        make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
        make_operation_button('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
        make_operation_button('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

        make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
        make_clear_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

        win1.grid_columnconfigure(0,minsize=60)
        win1.grid_columnconfigure(1,minsize=60)
        win1.grid_columnconfigure(2,minsize=60)
        win1.grid_columnconfigure(3,minsize=60)
        win1.grid_rowconfigure(1,minsize=60)
        win1.grid_rowconfigure(2,minsize=60)
        win1.grid_rowconfigure(3,minsize=60)
        win1.grid_rowconfigure(4,minsize=60)

        win1.mainloop()

def todolist():
        list = Tk()
        list.title('To-do List')
        list['bg'] = '#121212'
        list.resizable(False, False)


        def press_key(event):
                print(repr(event.char))
                if event.char == '\r':
                        add_task()
                elif event.char == '\x1b':
                        save_task()
                elif event.char == '\t':
                        load_task()
                elif event.char == 'UP':
                        delete_task()


        def add_task():
                task = entry_task.get()
                print(task)
                if task != '':
                        listbox_task.insert(END, task)
                        entry_task.delete(0, END)
                else:
                        messagebox.showwarning(title='Warning!', message='You are can not enter void task.')

        def delete_task():
                try:
                        task_index = listbox_task.curselection()[0]
                        listbox_task.delete(task_index)
                except:
                        messagebox.showwarning(title='Warning!', message='You are can not delete void task.')


        def correct_task():
                try:
                        task_index = listbox_task.curselection()[0]
                        task_text = listbox_task.get(task_index)
                        print(task_text)
                        entry_task.insert(0, task_text)
                        listbox_task.delete(task_index)
                        #entry_task.insert(0, task_index+1)

                        #listbox_task.delete(task_index)
                except:
                        messagebox.showwarning(title='Warning!', message='You are can not correct void task.')


        def load_task():
                try:
                        tasks = pickle.load(open('tasks.bat', 'rb'))
                        listbox_task.delete(0, END)
                        for task in tasks:
                                listbox_task.insert(END, task)
                except:
                        messagebox.showwarning(title='Warning!', message='No data file present.')

        def save_task():
                tasks = listbox_task.get(0, listbox_task.size())
                pickle.dump(tasks, open('tasks.bat', 'wb'))


        frame_task = Frame(list)
        frame_task.pack()

        listbox_task = Listbox(frame_task, height=10, width=60, bg='#121212', fg='white', relief=RAISED, bd=7)
        listbox_task.pack(side=LEFT)

        scrolbar_task = Scrollbar(frame_task, relief=RAISED, bd=7)
        scrolbar_task.pack(side=RIGHT, fill=Y)
        ttk.Style().configure(scrolbar_task, background="#121212", bordercolor="red", arrowcolor="black")

        list.bind('<Key>', press_key)  

        listbox_task.config(yscrollcommand=scrolbar_task.set)
        scrolbar_task.config(command=listbox_task.yview)

        entry_task = Entry(list, width=60, bg='black', fg='white', relief=RAISED, bd=7)
        entry_task.pack()

        button_add_task = Button(list, text='Add Task (Enter)', width=58, command=add_task, bg='#121212', fg='white', relief=RAISED, bd=7)
        button_add_task.pack()

        button_delete_task = Button(list, text='Delete Task', width=58, command=delete_task, bg='#121212', fg='white', relief=RAISED, bd=7)
        button_delete_task.pack()

        button_correct_task = Button(list, text='Correct Task', width=58, command=correct_task, bg='#121212', fg='white', relief=RAISED, bd=7)
        button_correct_task.pack()

        button_load_task = Button(list, text='Load Task (Tab)', width=58, command=load_task, bg='#121212', fg='white', relief=RAISED, bd=7)
        button_load_task.pack()

        button_save_task = Button(list, text='Save Task (Escape)', width=58, command=save_task, bg='#121212', fg='red', relief=RAISED, bd=7)
        button_save_task.pack()

        list.mainloop()


def get_entry():
        value = name.get()
        if value:
                print(value)
        else:
                print('Empty entry')

def delete_entry():
        name.delete(0, 'end')

def add_clients():
        con = pymysql.connect(host = 'localhost', user = 'root', password = '8886547.artsiomsk23!', database = 'sms')
        cursor = con.cursor()
        print('connect')
        


def managment():
        win2 = Tk()
        win2['bg'] = '#121212'
        win2.geometry('1370x700+0+0')
        win2.resizable(False, False)
        title = Label(win2, text="MANAGMENT SYSTEM", bd = 9, relief=GROOVE, font=("Arial", 50, 'bold'), bg = 'yellow', fg= 'red')
        title.pack(side = TOP, fill= X)
        
        

        win2.roll_no_var = StringVar()        
        win2.name_var = StringVar()        
        win2.email_var = StringVar()        
        win2.gender_var = StringVar()        
        win2.contact_var = StringVar()        
        win2.date_var = StringVar()        
        win2.search_by = StringVar()        
        win2.search_txt = StringVar()        



        
        
        
        
        
        
        #MANAGE FRAME#
        Manage_Frame = Frame(win2, bd = 4, relief=RIDGE, bg='blue')
        Manage_Frame.place(x = 20, y = 100, width=450, height=585)
        
        m_title = Label(Manage_Frame, text='Manage clients', bg='yellow', fg='black', font=("Arial", 40, 'bold'))
        m_title.grid(row=0, columnspan=2, pady=20)
        
        lbl_roll = Label(Manage_Frame, text='Roll No', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')
        txt_roll = Entry(Manage_Frame, textvariable=win2.roll_no_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')
        
        lbl_name = Label(Manage_Frame, text='Name:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        txt_name = Entry(Manage_Frame, textvariable=win2.name_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')
        
        lbl_email = Label(Manage_Frame, text='Email:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        txt_email = Entry(Manage_Frame, textvariable=win2.email_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')
        
        lbl_gender = Label(Manage_Frame, text='Gender:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')
        
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=win2.gender_var, font=("Arial", 13, 'bold'), state='readonly')
        combo_gender['values'] = ('male', 'female', 'other')
        combo_gender.grid(row=4, column=1, pady=10, padx=20)
        
        lbl_contact = Label(Manage_Frame, text='Contact:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        txt_contact = Entry(Manage_Frame, textvariable=win2.contact_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')
        
        lbl_date = Label(Manage_Frame, text='Date:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_date.grid(row=6, column=0, pady=10, padx=20, sticky='w')
        txt_date = Entry(Manage_Frame, textvariable=win2.date_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
        txt_date.grid(row=6, column=1, pady=10, padx=20, sticky='w')
        
        lbl_adress = Label(Manage_Frame, text='Adress:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_adress.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        win2.txt_Adress = Text(Manage_Frame, width=30, height=3, font=("Arial", 10, 'bold'))
        win2.txt_Adress.grid(row=7, column=1, pady=10, padx=20, sticky='we')
        
        #bnt frame#
        
        btn_frame = Frame(Manage_Frame, bd = 3, relief=RIDGE, bg='black')
        btn_frame.place(x = 15, y = 525, width=420)
        
        add_btn = Button(btn_frame, text = 'Add', width=10, command=add_clients).grid(row = 0, column=0, padx=10, pady= 10)
        update_btn = Button(btn_frame, text = 'Update', width=10).grid(row = 0, column=1, padx=10, pady= 10)
        delete_btn = Button(btn_frame, text = 'Delete', width=10).grid(row = 0, column=2, padx=10, pady= 10)
        clear_btn = Button(btn_frame, text = 'Clear', width=10).grid(row = 0, column=3, padx=10, pady= 10)
        
        
        #DETAILS FRAME#
        Details_Frame = Frame(win2, bd = 4, relief=RIDGE, bg='blue')
        Details_Frame.place(x = 500, y = 100, width=880, height=585)
        
        lbl_search = Label(Details_Frame, text='Search By', bg='blue', fg='white', font=("Arial", 20, 'bold'))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')
        
        combo_search = ttk.Combobox(Details_Frame, textvariable=win2.search_by, font=("Arial", 13, 'bold'), width = 10, state='readonly')
        combo_search['values'] = ('Roll no', 'Name', 'Contact')
        combo_search.grid(row=0, column=1, pady=10, padx=20)
        txt_search = Entry(Details_Frame, textvariable=win2.search_txt, font=("Arial", 15, 'bold'),width=20, bd = 5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')
        
        search_btn = Button(Details_Frame, text = 'Search', width=10, pady=5).grid(row = 0, column=3, padx=10, pady= 10)
        showall_btn = Button(Details_Frame, text = 'Show All', width=10, pady=5).grid(row = 0, column=4, padx=10, pady= 10)
        
        
        #Table FRAME#
        Table_Frame = Frame(Details_Frame, bd = 4, relief=RIDGE, bg='crimson')
        Table_Frame.place(x = 10, y = 70, width=760, height=500)
        
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        
        win2.Client_table = ttk.Treeview(Table_Frame, column=("Roll", "Name", "Email", "Gender","Contact", "Date", "Address"), xscrollcommand=scroll_y, yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config()
        scroll_y.config()

        win2.Client_table.heading("Roll", text='Roll No.')
        win2.Client_table.heading("Name", text='Name')
        win2.Client_table.heading("Email", text='Email')
        win2.Client_table.heading("Gender", text='Gender')
        win2.Client_table.heading("Contact", text='Contact')
        win2.Client_table.heading("Date", text='Date')
        win2.Client_table.heading("Address", text='Adress')
        
        win2.Client_table['show'] = 'headings'
        win2.Client_table.column("Roll", width=100)
        win2.Client_table.column("Name", width=100)
        win2.Client_table.column("Email", width=100)
        win2.Client_table.column("Gender", width=100)
        win2.Client_table.column("Contact", width=100)
        win2.Client_table.column("Date", width=100)
        win2.Client_table.column("Address", width=150)
        
        win2.Client_table.pack(fill=BOTH, expand=1)
        
        
        
        win2.mainloop()

root['bg'] = '#121212'
#logo = PhotoImage(file='logo.png')
#root.iconphoto(False, logo)
root.title('FirstSpace')
root.wm_attributes('-alpha', 0.7)
root.geometry('600x600')
root.minsize(400,400)
root.maxsize(900,900)
root.resizable(False, False)

label_1 = Label(root, text= 'Welcome', 
                bg='black',     #background
                fg='gold',     #textcolor
                font= ('Arial', 18, 'bold'), #text
                #padx= 10,
                #pady= 20,    #inlabel
                width=10,
                #height=4,
                anchor='n',
                relief=RAISED,   #granici knopky
                bd=7
                #justify=LEFT    #prizhat k granici kogda nieskolko strok
)

btn1 = Button(root, text='Calculator',

        command=newwindow,   #vyzov funkcii
        bg='#121212',
        fg='#fdfdfd',
        font=('Arial', 12, 'bold'),
        #height = 5,
        #pady=10,
        relief = RAISED,
        bd = 5,
        )

btn1.grid(row=4, column=1, stick='we')

btn2 = Button(root, text='todolist',

        command=todolist,   #vyzov funkcii
        bg='#121212',
        fg='#fdfdfd',
        font=('Arial', 12, 'bold'),
        #height = 5,
        #pady=10,
        relief = RAISED,
        bd = 5
        )
btn2.grid(row=4, column=2, stick= 'we')

btn3 = Button(root, text="Get", command=get_entry, bg='black', fg='#fdfdfd',font= ('Arial', 12, 'bold'), width=10, anchor='n', relief=RAISED, bd=7).grid(row=3, column=1)
btn4 = Button(root, text="delete", command=delete_entry, bg='black', fg='#fdfdfd',font= ('Arial', 12, 'bold'), width=10, anchor='n', relief=RAISED, bd=7).grid(row=3, column=2)

btn5 = Button(root, text='Managment',

        command=managment,   #vyzov funkcii
        bg='#121212',
        fg='#fdfdfd',
        font=('Arial', 12, 'bold'),
        #height = 5,
        #pady=10,
        relief = RAISED,
        bd = 5,
        )
btn5.grid(row=5, column=1, stick='we')

name = Entry(root, bg='black', fg='#fdfdfd',font= ('Arial', 10, 'bold'), width=10, relief=RAISED, bd=7)

apples = Checkbutton(root, text="Do you like apples?", bg = '#121212', fg = '#fdfdfd', selectcolor = "black", font= ('Arial', 10, 'bold'))

label_1.grid(row=1, column=1, columnspan=2, stick='we')
name.grid(row=2, column=1, columnspan=2, stick='we')
apples.grid(row=6, column=1, columnspan=2,stick= 'we')


root.grid_columnconfigure(0, minsize=200)
root.grid_rowconfigure(0,minsize=150)



#root.grid_location(10, 10)

root.mainloop()