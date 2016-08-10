from tkinter import *
from tkinter import ttk


def Labels(local,text_lbl,nwidth=10):
    label = ttk.Label(local, text=text_lbl, width=nwidth, anchor="center")
    return label

def Buttons(local,text_lbl,comms,nwidth=10):
    button = ttk.Button(local, text=text_lbl, width=nwidth,command=comms)
    return button

def Entrys(local,txtvar,nwidth=10):
    entry = ttk.Entry(local,width=nwidth, textvariable=txtvar)
    return entry

def RadioButtons(local,text_lbl,var,val):
    radio = ttk.Radiobutton(local, text=text_lbl, variable=var, value=val)
    return radio

def Comboboxs(local,val,nwidth=10):
    combobox = ttk.Combobox(local, values=val, width=nwidth)
    return combobox

def CheckButtons(local,text_lbl,var,onval,offval):
    checkbuttons = ttk.Checkbutton(local, text=text_lbl, variable=var, onvalue=onval, offvalue=offval)
    return checkbuttons

def updatevalue(evt):
    widget = evt.widget
    txt = widget.get()
    vals = widget.cget('values')

    if not vals:
        widget.configure(values = (txt, ))
    elif txt not in vals:
        widget.configure(values =vals + (txt, ))
    
    return 'break'

#def makeinp(self):
#    print("Not implemented yet!")
def makeinp(self):
    blah = self.Entry1.get()
    print('hi')
    print(blah)


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)

        ### FILE NAME ###
        self.Label1 = Labels(self.master,"File name:")
        self.Label1.grid(column=1,row=1)
        file_name_var = StringVar()
        self.Entry1 = Entrys(self.master,file_name_var,30)
        self.Entry1.grid(column=2,row=1,columnspan=2)

        ### TITLE ###
        self.Label2 = Labels(self.master, "Title:")
        self.Label2.grid(column=4,row=1)
        title_var = StringVar()
        self.Entry2 = Entrys(self.master,title_var,30)
        self.Entry2.grid(column=5,row=1,columnspan=2)

        ### VXCTYP ###
        self.Label3 = Labels(self.master,"VXCTYP")
        self.Label3.grid(column=1,row=2)
        vxctyp_var = StringVar()
        self.Radio1 = RadioButtons(self.master,"Auxis",vxctyp_var,"AUXIS")
        self.Radio2 = RadioButtons(self.master,"Basis",vxctyp_var,"BASIS")
        self.Radio1.grid(column=3,row=2)
        self.Radio2.grid(column=2,row=2)

        ### XC Functional ###
        self.Label4 = Labels(self.master,"XC Functional:",12)
        self.Label4.grid(column=5,row=2)
        functional_list =('B3LYP', 'BLYP', 'PBE', 'PBE0', 'PW91')
        self.Combobox1 = Comboboxs(self.master,functional_list)
        self.Combobox1.grid(column=6,row=2)

        ### BASIS SET ###
        self.Label5 = Labels(self.master, "Basis set:")
        self.Label5.grid(column=1,row=5)
        basis_set_list=('DZVP','DZVP-GGA','TZVP','TZVP-GGA')
        self.Combobox2 = Comboboxs(self.master,basis_set_list)
        self.Combobox2.bind('<Return>', updatevalue)
        self.Combobox2.grid(column=2,row=5)

        ### AUXIS SET ###
        self.Label6 = Labels(self.master, "Auxis set:")
        self.Label6.grid(column=3,row=5)
        auxis_set_list=('gen-a1','gen-a2','gen-a2**','gen-a3**')
        self.Combobox3 = Comboboxs(self.master,auxis_set_list)
        self.Combobox3.bind('<Return>', updatevalue)
        self.Combobox3.grid(column=4,row=5)

        ### ECP ###
        self.Label7 = Labels(self.master, "ECP:")
        self.Label7.grid(column=5,row=5)
        ecp_list=('NONE','ECP|SD','RECP|SD','QECP|SD')
        self.Combobox4 = Comboboxs(self.master,ecp_list)
        self.Combobox4.bind('<Return>', updatevalue)
        self.Combobox4.grid(column=6,row=5)

        ### Shell Type ###
        self.Label8 = Labels(self.master, "Shell type:")
        self.Label8.grid(column=1,row=6)
        shelltyp_list=('RKS','ROKS','UKS')
        self.Combobox5 = Comboboxs(self.master,shelltyp_list)
        self.Combobox5.bind('<Return>', updatevalue)
        self.Combobox5.grid(column=2,row=6)

        ### SCF MAX ITER ###
        self.Label9 = Labels(self.master, "Max Iter for SCF:",12)
        self.Label9.grid(column=3,row=6)
        scfmaxiter_var = StringVar()
        self.Entry3 = Entrys(self.master,scfmaxiter_var)
        self.Entry3.grid(column=4,row=6)
        
        ### TOL ###
        self.Label10 = Labels(self.master, "Tolerance:")
        self.Label10.grid(column=1,row=7)
        tol_var = StringVar()
        self.Entry4 = Entrys(self.master,tol_var)
        self.Entry4.grid(column=2,row=7)

        ### GUESS ###
        self.Label11 = Labels(self.master, "Guess:")
        self.Label11.grid(column=5,row=6)
        guess_list=('TB','CORE','Fermi')
        self.Combobox6 = Comboboxs(self.master,guess_list)
        self.Combobox6.bind('<Return>', updatevalue)
        self.Combobox6.grid(column=6,row=6)

        ### CALCTYP ###
        self.Label12 = Labels(self.master, "Calculation:")
        self.Label12.grid(column=1,row=9)
        calc_var = StringVar()
        self.Radio3 = RadioButtons(self.master,"Single Point Energy",calc_var, "SPE")
        self.Radio4 = RadioButtons(self.master,"Optimization",calc_var, "OPT")
        self.Radio3.grid(column=2,row=9)
        self.Radio4.grid(column=3,row=9)
        
        ### FREQUENCY ###
        freq_var = StringVar()
        self.check1 = CheckButtons(self.master, "Frequency Analysis", freq_var,'on','off')
        self.check1.grid(column=4,row=9)
        
        ### GEOMETRY ###
        self.Label13 = Labels(self.master, "Input Geometry file name:",30)
        self.Label13.grid(column=1,row=10,columnspan=2)
        geometry_var = StringVar()
        self.Entry5 = Entrys(self.master, geometry_var,20)
        self.Entry5.grid(column=3,row=10,columnspan=2)

        ### THERMO ###
        thermo_var = StringVar()
        self.check2 = CheckButtons(self.master, "Thermo Calc.",  thermo_var, 'on','off')
        self.check2.grid(column=5,row=9)
    
        ### MULTIPLICITY ###
        self.Label14 = Labels(self.master, "Multiplicity:")
        self.Label14.grid(column=3,row=7)
        multiplicity_var = StringVar()
        self.Entry6 = Entrys(self.master, multiplicity_var)
        self.Entry6.grid(column=4,row=7)
        
        ### CHARGE ###
        self.Label15 = Labels(self.master, "Charge:")
        self.Label15.grid(column=5,row=7)
        charge_var = StringVar()
        self.Entry7 = Entrys(self.master, charge_var)
        self.Entry7.grid(column=6,row=7)
        
        ### TIGHT ###
        tight_var = StringVar()
        self.check3 = CheckButtons(self.master, "Tighten",  tight_var, 'on','off')
        self.check3.grid(column=5,row=8)
        
        ### SHIFT ###
        self.Label16 = Labels(self.master, "Shift:")
        self.Label16.grid(column=1,row=8)
        shift_var = StringVar()
        self.Entry8 = Entrys(self.master, shift_var)
        self.Entry8.grid(column=2,row=8)

        ### GRID ###
        self.Label17 = Labels(self.master, "Grid:")
        self.Label17.grid(column=3,row=8)
        grid_list =('medium','coarse','fine')
        self.Combobox7 = Comboboxs(self.master,grid_list)
        self.Combobox7.bind('<Return>', updatevalue)
        self.Combobox7.grid(column=4,row=8)

        ### DIIS ###
        diis_var = StringVar()
        self.check4 = CheckButtons(self.master, "DIIS", diis_var, 'on','off')
        self.check4.grid(column=6,row=8)
        
        ### OPTGEOM ###
        self.Label18 = Labels(self.master, "Geometry for OPT:",14)
        self.Label18.grid(column=5,row=10)
        optgeom_list=('Redundant','Cartesian','Z-matrix')
        self.Combobox8 = Comboboxs(self.master, optgeom_list)
        self.Combobox8.bind('<Return>', updatevalue)
        self.Combobox8.grid(column=6,row=10)
        
        ### GEOMDIS ###
        self.Label19 = Labels(self.master, "Geometry Coords.",15)
        self.Label19.grid(column=1,row=11)
        geomdis_var = StringVar()
        self.Radio5 = RadioButtons(self.master, "Angstrom", geomdis_var, "Angstrom")
        self.Radio6 = RadioButtons(self.master, "Bohr", geomdis_var, "Bohr")
        self.Radio5.grid(column=3,row=11)
        self.Radio6.grid(column=2,row=11)
        
        ### GEOMTYP ###
        self.Label20 = Labels(self.master, "Geometry Type:",12)
        self.Label20.grid(column=4,row=11)
        geomtyp_var = StringVar()
        self.Radio7 = RadioButtons(self.master,"Cartesian",geomtyp_var,"Cartesian")
        self.Radio8 = RadioButtons(self.master,"Z-Matrix",geomtyp_var,"Z-Matrix")
        self.Radio7.grid(column=5,row=11)
        self.Radio8.grid(column=6,row=11)


        ### CREATE ###
        self.Button1 = Buttons(self.master,"Create Input",makeinp(self))
        self.Button1.grid(column=3,row=20)
        self.Button2 = Buttons(self.master,"Exit",self.master.destroy)
        self.Button2.grid(column=4,row=20)

    def new_window(self):
        self.newWindow = ttk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.quitButton = ttk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()
    

def main(): 
    root = Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
