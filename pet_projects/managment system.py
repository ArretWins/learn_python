from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Client():
        def add_clients(self):
                if self.roll_no_var.get() == "" or self.name_var.get() == "":
                        messagebox.showerror("all fields are required to fill")
                else:
                        con = pymysql.connect(host = 'localhost', port = 3307, user = 'root', password='8886547.artsiomsk23!', database='sms')
                        cur = con.cursor()
                        cur.execute("insert into clients values (%s, %s, %s, %s, %s, %s, %s)", (self.roll_no_var.get(),
                                                                                                self.name_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.gender_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.date_var.get(),
                                                                                                self.txt_Adress.get('1.0', END)
                                                                                                ))
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        con.close()
                        messagebox.showinfo("success", "Recored has been inserted")

        def fetch_data(self):
                con = pymysql.connect(host = 'localhost', port = 3307, user = 'root', password='8886547.artsiomsk23!', database='sms')
                cur = con.cursor()
                cur.execute("SELECT * FROM CLIENTS")
                rows = cur.fetchall()
                if len(rows) != 0:
                        self.Client_table.delete(*self.Client_table.get_children())
                        for row in rows:
                                self.Client_table.insert('', END, values=row)
                        con.commit()
                con.close()
                        
        def clear(self):
                self.roll_no_var.set("")
                self.name_var.set("")
                self.email_var.set("")
                self.gender_var.set("")
                self.contact_var.set("")
                self.txt_Adress.delete("1.0", END)
        


        def __init__(self, root):
                self.root = root
                self.root['bg'] = '#121212'
                self.root.geometry('1370x700+0+0')
                #self.root.resizable(False, False)
                title = Label(self.root, text="MANAGMENT SYSTEM", bd = 9, relief=GROOVE, font=("Arial", 50, 'bold'), bg = 'yellow', fg= 'red')
                title.pack(side = TOP, fill= X)
                
                
                self.roll_no_var = StringVar()        
                self.name_var = StringVar()        
                self.email_var = StringVar()        
                self.gender_var = StringVar()        
                self.contact_var = StringVar()        
                self.date_var = StringVar()        
                self.search_by = StringVar()        
                self.search_txt = StringVar()        

                
                #MANAGE FRAME#
                Manage_Frame = Frame(self.root, bd = 4, relief=RIDGE, bg='blue')
                Manage_Frame.place(x = 20, y = 100, width=450, height=585)
                
                m_title = Label(Manage_Frame, text='Manage clients', bg='yellow', fg='black', font=("Arial", 40, 'bold'))
                m_title.grid(row=0, columnspan=2, pady=20)
                
                lbl_roll = Label(Manage_Frame, text='Roll No', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky='w')
                txt_roll = Entry(Manage_Frame, textvariable=self.roll_no_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                #txt_roll = Entry(Manage_Frame, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky='w')
                
                lbl_name = Label(Manage_Frame, text='Name:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
                txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                #txt_name = Entry(Manage_Frame, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')
                
                lbl_email = Label(Manage_Frame, text='Email:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky='w')
                txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                #txt_email = Entry(Manage_Frame, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                txt_email.grid(row=3, column=1, pady=10, padx=20, sticky='w')
                
                lbl_gender = Label(Manage_Frame, text='Gender:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')
                
                combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("Arial", 13, 'bold'), state='readonly')
                #combo_gender = ttk.Combobox(Manage_Frame, font=("Arial", 13, 'bold'), state='readonly')
                combo_gender['values'] = ('male', 'female', 'other')
                combo_gender.grid(row=4, column=1, pady=10, padx=20)
                
                lbl_contact = Label(Manage_Frame, text='Contact:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky='w')
                #txt_contact = Entry(Manage_Frame, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky='w')
                
                lbl_date = Label(Manage_Frame, text='Date:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_date.grid(row=6, column=0, pady=10, padx=20, sticky='w')
                txt_date = Entry(Manage_Frame, textvariable=self.date_var, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                #txt_date = Entry(Manage_Frame, font=("Arial", 15, 'bold'),bd = 5, relief=GROOVE)
                txt_date.grid(row=6, column=1, pady=10, padx=20, sticky='w')
                
                lbl_adress = Label(Manage_Frame, text='Adress:', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_adress.grid(row=7, column=0, pady=10, padx=20, sticky='w')
                self.txt_Adress = Text(Manage_Frame, width=30, height=3, font=("Arial", 10, 'bold'))
                self.txt_Adress.grid(row=7, column=1, pady=10, padx=20, sticky='we')
                
                #bnt frame#
                
                btn_frame = Frame(Manage_Frame, bd = 3, relief=RIDGE, bg='black')
                btn_frame.place(x = 15, y = 525, width=420)
                
                add_btn = Button(btn_frame, text = 'Add', width=10, command= self.add_clients).grid(row = 0, column=0, padx=10, pady= 10)
                update_btn = Button(btn_frame, text = 'Update', width=10).grid(row = 0, column=1, padx=10, pady= 10)
                delete_btn = Button(btn_frame, text = 'Delete', width=10).grid(row = 0, column=2, padx=10, pady= 10)
                clear_btn = Button(btn_frame, text = 'Clear', width=10, command= self.clear).grid(row = 0, column=3, padx=10, pady= 10)
                
                
                #DETAILS FRAME#
                Details_Frame = Frame(self.root, bd = 4, relief=RIDGE, bg='blue')
                Details_Frame.place(x = 500, y = 100, width=880, height=585)
                
                lbl_search = Label(Details_Frame, text='Search By', bg='blue', fg='white', font=("Arial", 20, 'bold'))
                lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')
                
                combo_search = ttk.Combobox(Details_Frame, textvariable=self.search_by, font=("Arial", 13, 'bold'), width = 10, state='readonly')
                #combo_search = ttk.Combobox(Details_Frame, font=("Arial", 13, 'bold'), width = 10, state='readonly')
                combo_search['values'] = ('Roll no', 'Name', 'Contact')
                combo_search.grid(row=0, column=1, pady=10, padx=20)
                txt_search = Entry(Details_Frame, textvariable=self.search_txt, font=("Arial", 15, 'bold'),width=20, bd = 5, relief=GROOVE)
                #txt_search = Entry(Details_Frame, font=("Arial", 15, 'bold'),width=20, bd = 5, relief=GROOVE)
                txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')
                
                search_btn = Button(Details_Frame, text = 'Search', width=10, pady=5).grid(row = 0, column=3, padx=10, pady= 10)
                showall_btn = Button(Details_Frame, text = 'Show All', width=10, pady=5).grid(row = 0, column=4, padx=10, pady= 10)
                
                
                #Table FRAME#
                Table_Frame = Frame(Details_Frame, bd = 4, relief=RIDGE, bg='crimson')
                Table_Frame.place(x = 10, y = 70, width=760, height=500)
                
                scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
                scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
                
                self.Client_table = ttk.Treeview(Table_Frame, column=("Roll", "Name", "Email", "Gender","Contact", "Date", "Address"), xscrollcommand=scroll_y, yscrollcommand=scroll_x)
                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                
                scroll_x.config()
                scroll_y.config()

                self.Client_table.heading("Roll", text='Roll No.')
                self.Client_table.heading("Name", text='Name')
                self.Client_table.heading("Email", text='Email')
                self.Client_table.heading("Gender", text='Gender')
                self.Client_table.heading("Contact", text='Contact')
                self.Client_table.heading("Date", text='Date')
                self.Client_table.heading("Address", text='Adress')
                
                self.Client_table['show'] = 'headings'
                self.Client_table.column("Roll", width=100)
                self.Client_table.column("Name", width=100)
                self.Client_table.column("Email", width=100)
                self.Client_table.column("Gender", width=100)
                self.Client_table.column("Contact", width=100)
                self.Client_table.column("Date", width=100)
                self.Client_table.column("Address", width=150)
                
                self.Client_table.pack(fill=BOTH, expand=1)


                
class Client():
        pass
        root = Tk()
        obj = Client(root)
        root.mainloop()
