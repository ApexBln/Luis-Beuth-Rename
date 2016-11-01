# -*- coding: utf-8 -*-
from tkinter import Tk,Button,Frame,Label,filedialog, ttk, Menu, Toplevel, Entry
import os as os
import tkinter as tkinter
import csv as csv
#To Do
"""
-Studium Generale rein (Liste + CSV), zweites Dropdown
-If-BA/MA Abfragen zu Studiengängen
-Main Menü (Datei,Optionen,Info/About) erstellen
-Öffnen der Ursprungsdatei (Vorschau)
"""
class Application(Frame):
    #Design des Fensters und deren Darstellung

    def __init__(self, master=None):
        Frame.__init__(self, master)        
       
        self.lst_abschluss=[]        
        #print("Leer: ",self.lst_abschluss)        
        self.lst_studiengang=[]
        self.lst_modul=[]
        self.lst_semester=[]
        self.lst_dozent=[]
        self.lst_przr=[]
        self.lst_version=[]
        self.lst_note=[]
        self.total_content=[]
        with open('LOUIS-Beuth-Renamer.csv','r',newline='')as csvfile:
            for row in csv.reader(csvfile):
                    self.total_content.append(row)
        self.lst_abschluss=self.total_content[0]
        self.lst_abschluss_mod=self.total_content[0]        
        self.lst_studiengang_BA=self.total_content[1]
        self.lst_studiengang_MA=self.total_content[2]
        
        #Modulnamen weiter anpassen
        self.lst_module_BA_BauIng=self.total_content[3]
        self.lst_module_BA_UmweltIng=self.total_content[4]
        self.lst_module_BA_WiIng=self.total_content[5]
        self.lst_module_BA_GeoInfo=self.total_content[6]
        self.lst_module_MA_WiIng=self.total_content[7]
        self.lst_module_MA_BauIng=self.total_content[8]
        self.lst.module_MA_GeoInfo=self.total_content[9]
        self.lst_module_MA_UmweltIng=self.total_content[10]
        self.lst_semester=self.total_content[11]
        self.lst_dozent=self.total_content[12]
        self.lst_przr=self.total_content[13]
        self.lst_version=self.total_content[14]
        self.lst_note=self.total_content[15]
        #print(self.lst_abschluss)
        #print(self.lst_studiengang)
                             

        self.var_abschluss = tkinter.StringVar()
        self.var_abschluss.set("unbekannt")    

        self.var_studiengang = tkinter.StringVar()
        self.var_studiengang.set("unbekannt")        
        
        self.var_modul = tkinter.StringVar()
        self.var_modul.set("unbekannt")        

        self.var_semester = tkinter.StringVar()
        self.var_semester.set("unbekannt")        

        self.var_dozent = tkinter.StringVar()
        self.var_dozent.set("unbekannt")        

        self.var_przr = tkinter.StringVar()
        self.var_przr.set("unbekannt")        

        self.var_version = tkinter.StringVar()
        self.var_version.set("unbekannt")        

        self.var_note = tkinter.StringVar()
        self.var_note.set("unbekannt")        
        self.create_widgets()
        self.drop_refresh()
        self.mainmenu()
    
    #Create
    def create_widgets(self):
        self.abschluss_l = Label(root,text="Abschluss:  ")
        self.abschluss_l.grid(row=0,column=0,sticky='w')
        self.studiengang_l = Label(root,text="Studiengang:  ")
        self.studiengang_l.grid(row=1,column=0,sticky='w')
        self.modul_l = Label(root,text="Modulname:  ")
        self.modul_l.grid(row=2,column=0,sticky='w')
        self.semester_l = Label(root,text="Semester:  ")
        self.semester_l.grid(row=4,column=0,sticky='w')
        self.dozent_l = Label(root,text="Dozent:  ")
        self.dozent_l.grid(row=3,column=0,sticky='w')        
        self.przr_l = Label(root,text="Prüfungszeitraum:  ")
        self.przr_l.grid(row=5,column=0,sticky='w')        
        self.version_l = Label(root,text="Version:  ")
        self.version_l.grid(row=6,column=0,sticky='w')        
        self.note_l = Label(root,text="Note:  ")
        self.note_l.grid(row=7,column=0,sticky='w')

        self.select_button = Button(root,text="Datei",command=self.datei_waehlen)
        self.select_button.grid(row=8,column=0,sticky='w')  
        self.save_button = Button(root,text="Save",command=self.save_file)
        self.save_button.grid(row=8,column=0,sticky='e')

        self.vorschau_label = Label(root,text='')
        self.vorschau_label.grid(row=11,columnspan=1000)
        self.datei_label = Label(root,text='Datei:  ')
        self.datei_label.grid(row=9,column=0,sticky='w')
        self.datei_gewaehlt = Label(root,text='')
        self.datei_gewaehlt.grid(row=9,column=1)
        
        self.vorschau_button = Button(root,text="Dateiname Vorschau",command=self.dateiname_vorschau)
        self.vorschau_button.grid(row=10,column=0)
        
    def drop_refresh(self):                             
        self.drop_abschluss = ttk.Combobox(root,textvariable=self.var_abschluss,values=self.lst_abschluss)
        self.drop_abschluss.grid(row=0,column=1)
        
        self.drop_studiengang = ttk.Combobox(root,textvariable=self.var_studiengang,values=self.lst_studiengang)
        self.drop_studiengang.grid(row=1,column=1)
        self.drop_modul = ttk.Combobox(root,textvariable=self.var_modul,values=self.lst_modul)
        self.drop_modul.grid(row=2,column=1)
        self.drop_semester = ttk.Combobox(root,textvariable=self.var_semester,values=self.lst_semester)
        self.drop_semester.grid(row=3,column=1)
        self.drop_dozent = ttk.Combobox(root,textvariable=self.var_dozent,values=self.lst_dozent)
        self.drop_dozent.grid(row=4,column=1)
        self.drop_przr = ttk.Combobox(root,textvariable=self.var_przr,values=self.lst_przr)
        self.drop_przr.grid(row=5,column=1)
        self.drop_version = ttk.Combobox(root,textvariable=self.var_version,values=self.lst_version)
        self.drop_version.grid(row=6,column=1)
        self.drop_note = ttk.Combobox(root,textvariable=self.var_note,values=self.lst_note)
        self.drop_note.grid(row=7,column=1)
        
            
        
    def mainmenu(self):
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)      
        filemenu.add_separator()      
        filemenu.add_command(label="Exit", command=self.donothing)    
        menubar.add_cascade(label="Datei", menu=filemenu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Dozent hinzufügen", command=self.add_dozent)
        editmenu.add_command(label="Modul hinzufügen", command=self.add_modul)
        editmenu.add_separator() 
        editmenu.add_command(label="Dozent entfernen", command=self.del_dozent)
        editmenu.add_command(label="Modul entfernen", command=self.del_modul)             
        menubar.add_cascade(label="Bearbeiten", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.about)
        menubar.add_cascade(label="About", menu=helpmenu)

    def donothing(self):
        button = Button(root, text="Do nothing button")
        button.pack()
    
    def datei_waehlen(self):
        self.filepath=filedialog.askopenfilename()
        self.filename=os.path.basename(self.filepath)
        if self.filename != '':
            self.datei_gewaehlt['text']=self.filename
        
    def dateiname_vorschau(self):
        self.newName = self.var_abschluss.get()+"_"+self.var_studiengang.get()+"_"+self.var_modul.get()+"_"+self.var_semester.get()+"_"+self.var_dozent.get()+"_"+self.var_przr.get()+"_"+self.var_version.get()+"_"+self.var_note.get()+".pdf"
        self.vorschau_label['text']=self.newName
        
    def target_directory(self):
        self.EndPath = self.var_abschluss.get()+"/"+self.var_studiengang.get()+"/"+self.var_modul.get()+"/"+self.var_semester.get()+"/"+self.var_dozent.get()      
        
    def new_name(self):
        self.newName = self.var_abschluss.get()+"_"+self.var_studiengang.get()+"_"+self.var_modul.get()+"_"+self.var_semester.get()+"_"+self.var_dozent.get()+"_"+self.var_przr.get()+"_"+self.var_version.get()+"_"+self.var_note.get()+".pdf"
        
        
    def make_dir(self):
        if not os.path.exists(self.EndPath):
            os.makedirs(self.EndPath)
           
    def save_file(self):
        self.drop_refresh()
        self.target_directory()
        self.new_name()
        self.make_dir()
        os.rename(self.filepath,self.EndPath+"/"+self.newName)
        print(self.EndPath+"/"+self.newName)

    def about(self):
        t = Toplevel(root)
        t.wm_attributes('-topmost',-1)
        t.wm_title("Impressum, About" )
        t.wm_geometry('500x600+10+10')
        l = Label(t, text="Impressum, etc" )
        l.pack(side="top", fill="both", expand=True)

    def add_dozent(self):
        self.drop_refresh()
        popup_add_dozent = Toplevel(root)
        popup_add_dozent.wm_attributes('-topmost',-1)
        popup_add_dozent.wm_title("Dozent hinzufügen" )
        popup_add_dozent.wm_geometry('250x100+10+350')
        #popup_add_dozent = Label(self.popup_add_dozent, text="Hier könnte ein Fließtext stehen" )
        
        Label(popup_add_dozent, text="Dozentenname").grid(row=0)
        
        Dozentenname = Entry(popup_add_dozent)
        Dozentenname.grid(row=0, column=1)
        
        # Hier muss noch die übergabe an die CSV gemacht werden.     
        # GGF ein weiters Popup mit der frage ob es übernommen werden soll
        Eingabeende = Button(popup_add_dozent,text="übernehmen", command=self.donothing)
        Eingabeende.grid(row=4, column=1)

    def add_modul(self):
        self.drop_refresh()        
        popup_add_modul = Toplevel(root)
        popup_add_modul.wm_attributes('-topmost',-1)
        popup_add_modul.wm_title("Modul hinzufügen" )
        popup_add_modul.wm_geometry('300x100+10+500')
        #popup_add_dozent = Label(self.popup_add_dozent, text="Hier könnte ein Fließtext stehen" )
        
        Label(popup_add_modul, text="Abschluss  ").grid(row=0,column=0,sticky='w')
        Label(popup_add_modul, text="Studiengang  ").grid(row=1,column=0,sticky='w')
        Label(popup_add_modul, text="Modulname  ").grid(row=2,column=0,sticky='w')
        
        drop_abschluss = ttk.Combobox(popup_add_modul,textvariable=self.var_abschluss,values=self.lst_abschluss)
        drop_abschluss.grid(row=0,column=1)
        if drop_abschluss.get() == "Bachelor":
            drop_studiengang = ttk.Combobox(popup_add_modul,textvariable=self.var_studiengang_BA,values=self.lst_studiengang)
            drop_studiengang.grid(row=1,column=1) 
        elif drop_abschluss.get() == "Master":
            drop_studiengang = ttk.Combobox(popup_add_modul,textvariable=self.var_studiengang_MA,values=self.lst_studiengang)
            drop_studiengang.grid(row=1,column=1)        
        else: 
            print ('Bitte Abschluss angeben')  
        
        modulname = Entry(popup_add_modul)
        modulname.grid(row=2, column=1)
        
        # Hier muss noch die übergabe an die CSV gemacht werden.
        # GGF ein weiters Popup mit der frage ob es übernommen werden soll
        Eingabeende = Button(popup_add_modul,text="übernehmen", command=self.donothing)
        Eingabeende.grid(row=4, column=1)

    def del_dozent(self):
        popup_del_dozent = Toplevel(root)
        popup_del_dozent.wm_attributes('-topmost',-1)
        popup_del_dozent.wm_title("Dozent entfernen" )
        popup_del_dozent.wm_geometry('250x100+260+350')
        #popup_del_dozent = Label(self.popup_add_dozent, text="Hier könnte ein Fließtext stehen" )
        
        Label(popup_del_dozent, text="Dozentenname").grid(row=0)
        
        Dozentenname = Entry(popup_del_dozent)
        Dozentenname.grid(row=0, column=1)
        
        # Hier muss noch die übergabe an die CSV gemacht werden.     
        # GGF ein weiters Popup mit der frage ob es übernommen werden soll
        Eingabeende = Button(popup_del_dozent,text="übernehmen", command=self.donothing)
        Eingabeende.grid(row=4, column=1)

    def del_modul(self):
        self.popup_del_modul = Toplevel(root)
        self.popup_del_modul.wm_attributes('-topmost',-1)
        self.popup_del_modul.wm_title("Modul entfernen" )
        self.popup_del_modul.wm_geometry('250x100+260+500')
        #popup_del_dozent = Label(self.popup_add_dozent, text="Hier könnte ein Fließtext stehen" )
        
       
        # Hier muss noch die übergabe an die CSV gemacht werden.
        # GGF ein weiters Popup mit der frage ob es übernommen werden soll
        Eingabeende = Button(self.popup_del_modul,text="übernehmen", command=self.donothing)
        Eingabeende.grid(row=4, column=1)

    


root = Tk()
root.title("LUIS Beuth Renamer") 
menubar=Menu(root)
root.config(menu=menubar)
root.wm_attributes('-topmost',-1)
root.wm_geometry('500x280+10+10') 
app = Application(master=root)
app.mainloop()