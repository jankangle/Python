# Title: GUI for deMon2k Input Generation (Python 2.7.6) 
# Date Created: Aug 8th,2016
# Date Last Modified: Aug 11th, 2016
# Version: 1.0
#
# Author: Jonathan Kung
# D.R. Salahub, M.C. Silva
# University of Calgary
# Purpose: Create a simple GUI to allow users to easily make a demon2k input
# without worrying about formatting or forgetting settings

### Import Libraries ###
from Tkinter import *
import ttk

### Tk Widget as functions ###
# local = Which window the widget is on
# text_lbl = The text displayed on the widget
# nwidth = the width of the widget
# comms = the command associated with the widget when activated
# txtvar = The variable associated with the input of text
# var = variable associated with the on/off state of the widget
# val = the list of values used in the combobox
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

def CheckButtons(local,text_lbl,var):
    checkbuttons = ttk.Checkbutton(local, text=text_lbl, variable=var)
    return checkbuttons

### Combobox command ###
# This will allow the custom entries into comboboxes
def updatevalue(evt):
    widget = evt.widget
    txt = widget.get()
    vals = widget.cget('values')

    if not vals:
        widget.configure(values = (txt, ))
    elif txt not in vals:
        widget.configure(values =vals + (txt, ))
    
    return 'break'

### Defining the main window ###
def main_window(frame):

    ### Get all the variables from all the widgets ###
    def getvars(*args):

        _finp = Entry1.get()
        _title = Entry2.get()
        _vxctyp = vxctyp_var.get()
        _xcfunc = Combobox1.get()
        _basis = Combobox2.get()
        _auxis = Combobox3.get()
        _ecp = Combobox4.get()
        _shelltyp = Combobox5.get()
        _scfmxiter = Entry3.get()
        _tol = Entry4.get()
        _guess = Combobox6.get()
        _calctyp = calc_var.get()
        _freq = freq_var.get()
        _geom = Entry5.get()
        _thermo = thermo_var.get()
        _mult = Entry6.get()
        _charge = Entry7.get()
        #_tight = tight_var.get()
        _shift = Entry8.get()
        _grid = Combobox7.get()
        _diis = diis_var.get()
        _optgeom = Combobox8.get()
        _geomdis = geomdis_var.get()
        _geomtyp = geomtyp_var.get()

        ### Take the variables and print the deMon2k input into output file ###
        def makeinp(*args):
            output = open(_finp, 'w')
            output.write("TITLE"+" "+_title+"\n")
            output.write("VXCTYP"+" "+_vxctyp+" "+_xcfunc+"\n")
            output.write("BASIS ("+_basis+")"+"\n")
            if _ecp != "NONE":
                output.write("ECPS ("+_ecp+")"+"\n")
            output.write("AUXIS ("+_auxis+")"+"\n")
            _tight = tight_var.get()
            if _tight == 1:
                output.write("SCFTYP"+" "+_shelltyp+" "+"MAX="+_scfmxiter+" "+_tol+"\n")
            elif _tight == 0:
                _tight = "NOTIGHTEN"
                output.write("SCFTYP"+" "+_tight+" "+_shelltyp+" "+"MAX="+_scfmxiter+" "+_tol+"\n")
            else:
                print("Invalid Tight setting")
            if _shift != "0":
                output.write("SHIFT"+" "+_shift+"\n")
            if (_grid == "medium" or _grid == "coarse" or _grid == "fine"):
                output.write("GRID FIXED"+" "+_grid+"\n")
            output.write("GUESS"+" "+_guess+"\n")
            if _diis == 0:
                output.write("DIIS OFF")
            output.write("MULTIPLICITY"+" "+_mult+"\n")
            output.write("CHARGE"+" "+_charge+"\n")
            if _calctyp == "OPT":
                output.write("OPTIMIZATION"+" "+_optgeom+"\n")
            if _freq == 1:
                output.write("FREQUENCY"+"\n")
                if _thermo == 1:
                    output.write("THERMO"+"\n")
            output.write("GEOMETRY"+" "+_geomtyp+" "+_geomdis+"\n")
            ### Open Geometry file ###
            geomfile= open(_geom,'r')
            ### Read and copy file up to 101 lines ###
            for x in range(0,100):
                try:
                   _xyz=geomfile.readline()
                   output.write(_xyz)
                except EOFError:
                    pass
            geomfile.close()
            output.close()
        ### end of getvars

        makeinp()

    #### Each individual widget on the main screen ####

    ### FILE NAME ###
    Label1 = Labels(frame,"File name:")
    Label1.grid(column=1,row=1)
    file_name_var = StringVar()
    Entry1 = Entrys(frame,file_name_var,30)
    Entry1.grid(column=2,row=1,columnspan=2)
    
    ### TITLE ###
    Label2 = Labels(frame, "Title:")
    Label2.grid(column=4,row=1)
    title_var = StringVar()
    Entry2 = Entrys(frame,title_var,30)
    Entry2.grid(column=5,row=1,columnspan=2)
    
    ### VXCTYP ###
    Label3 = Labels(frame,"VXCTYP")
    Label3.grid(column=1,row=2)
    vxctyp_var = StringVar()
    Radio1 = RadioButtons(frame,"Auxis",vxctyp_var,"AUXIS")
    Radio2 = RadioButtons(frame,"Basis",vxctyp_var,"BASIS")
    Radio1.grid(column=3,row=2)
    Radio2.grid(column=2,row=2)
    
    ### XC Functional ###
    Label4 = Labels(frame,"XC Functional:",12)
    Label4.grid(column=5,row=2)
    functional_list =('B3LYP', 'BLYP', 'PBE', 'PBE0', 'PW91')
    Combobox1 = Comboboxs(frame,functional_list)
    Combobox1.bind('<Return>', updatevalue)
    Combobox1.grid(column=6,row=2)
    
    ### BASIS SET ###
    Label5 = Labels(frame, "Basis set:")
    Label5.grid(column=1,row=5)
    basis_set_list=('DZVP','DZVP-GGA','TZVP','TZVP-GGA')
    Combobox2 = Comboboxs(frame,basis_set_list)
    Combobox2.bind('<Return>', updatevalue)
    Combobox2.grid(column=2,row=5)
    
    ### AUXIS SET ###
    Label6 = Labels(frame, "Auxis set:")
    Label6.grid(column=3,row=5)
    auxis_set_list=('gen-a1','gen-a2','gen-a2**','gen-a3**')
    Combobox3 = Comboboxs(frame,auxis_set_list)
    Combobox3.bind('<Return>', updatevalue)
    Combobox3.grid(column=4,row=5)
    
    ### ECP ###
    Label7 = Labels(frame, "ECP:")
    Label7.grid(column=5,row=5)
    ecp_list=('NONE','ECP|SD','RECP|SD','QECP|SD')
    Combobox4 = Comboboxs(frame,ecp_list)
    Combobox4.bind('<Return>', updatevalue)
    Combobox4.grid(column=6,row=5)
    
    ### KS Shell Type ###
    Label8 = Labels(frame, "KS type:")
    Label8.grid(column=1,row=6)
    shelltyp_list=('RKS','ROKS','UKS')
    Combobox5 = Comboboxs(frame,shelltyp_list)
    Combobox5.bind('<Return>', updatevalue)
    Combobox5.grid(column=2,row=6)
    
    ### SCF MAX ITER ###
    Label9 = Labels(frame, "Max Iter for SCF:",12)
    Label9.grid(column=3,row=6)
    scfmaxiter_var = StringVar()
    Entry3 = Entrys(frame,scfmaxiter_var)
    Entry3.grid(column=4,row=6)
    
    ### TOL ###
    Label10 = Labels(frame, "Tolerance:")
    Label10.grid(column=1,row=7)
    tol_var = StringVar()
    Entry4 = Entrys(frame,tol_var)
    Entry4.grid(column=2,row=7)
    
    ### GUESS ###
    Label11 = Labels(frame, "Guess:")
    Label11.grid(column=5,row=6)
    guess_list=('TB','CORE','Fermi')
    Combobox6 = Comboboxs(frame,guess_list)
    Combobox6.bind('<Return>', updatevalue)
    Combobox6.grid(column=6,row=6)
    
    ### CALCTYP ###
    Label12 = Labels(frame, "Calculation:")
    Label12.grid(column=1,row=10)
    calc_var = StringVar()
    Radio3 = RadioButtons(frame,"Single Point Energy",calc_var, "SPE")
    Radio4 = RadioButtons(frame,"Optimization",calc_var, "OPT")
    Radio3.grid(column=2,row=10)
    Radio4.grid(column=3,row=10)
    
    ### FREQUENCY ###
    freq_var = IntVar()
    check1 = CheckButtons(frame, "Frequency Analysis", freq_var)
    check1.grid(column=4,row=10)
    
    ### GEOMETRY ###
    Label13 = Labels(frame, "Input Geometry file name:",30)
    Label13.grid(column=1,row=12,columnspan=2)
    geometry_var = StringVar()
    Entry5 = Entrys(frame, geometry_var,20)
    Entry5.grid(column=3,row=12,columnspan=2)
    
    ### THERMO ###
    thermo_var = StringVar()
    check2 = CheckButtons(frame, "Thermo Calc.",  thermo_var)
    check2.grid(column=5,row=10)
    
    ### MULTIPLICITY ###
    Label14 = Labels(frame, "Multiplicity:")
    Label14.grid(column=3,row=7)
    multiplicity_var = StringVar()
    Entry6 = Entrys(frame, multiplicity_var)
    Entry6.grid(column=4,row=7)
    
    ### CHARGE ###
    Label15 = Labels(frame, "Charge:")
    Label15.grid(column=5,row=7)
    charge_var = StringVar()
    Entry7 = Entrys(frame, charge_var)
    Entry7.grid(column=6,row=7)
    
    ### TIGHT ###
    tight_var = IntVar()
    check3 = CheckButtons(frame, "Tighten",  tight_var)
    check3.grid(column=5,row=8)
    
    ### SHIFT ###
    Label16 = Labels(frame, "Shift:")
    Label16.grid(column=1,row=8)
    shift_var = StringVar()
    Entry8 = Entrys(frame, shift_var)
    Entry8.grid(column=2,row=8)
    
    ### GRID ###
    Label17 = Labels(frame, "Grid:")
    Label17.grid(column=3,row=8)
    grid_list =('do not fix','MEDIUM','COARSE','FINE')
    Combobox7 = Comboboxs(frame,grid_list)
    Combobox7.bind('<Return>', updatevalue)
    Combobox7.grid(column=4,row=8)

    ### DIIS ###
    diis_var = StringVar()
    check4 = CheckButtons(frame, "DIIS", diis_var)
    check4.grid(column=6,row=8)
    
    ### OPTGEOM ###
    Label18 = Labels(frame, "Geometry for OPT:",14)
    Label18.grid(column=5,row=12)
    optgeom_list=('REDUNDANT','CARTESIAN','INTERNAL')
    Combobox8 = Comboboxs(frame, optgeom_list,15)
    Combobox8.bind('<Return>', updatevalue)
    Combobox8.grid(column=6,row=12)
    
    ### GEOMDIS ###
    Label19 = Labels(frame, "Geometry Coordinates:",18)
    Label19.grid(column=1,row=13)
    geomdis_var = StringVar()
    Radio5 = RadioButtons(frame, "Angstrom", geomdis_var, "ANGSTROM")
    Radio6 = RadioButtons(frame, "Bohr", geomdis_var, "BOHR")
    Radio5.grid(column=3,row=13)
    Radio6.grid(column=2,row=13)
    
    ### GEOMTYP ###
    Label20 = Labels(frame, "Geometry Type:",12)
    Label20.grid(column=4,row=13)
    geomtyp_var = StringVar()
    Radio7 = RadioButtons(frame,"Cartesian",geomtyp_var,"CARTESIAN")
    Radio8 = RadioButtons(frame,"Z-Matrix",geomtyp_var,"ZMATRIX")
    Radio7.grid(column=5,row=13)
    Radio8.grid(column=6,row=13)
    
    
    ### CREATE/Exit ###
    Button1 = Buttons(frame,"Create Input",getvars)
    Button1.grid(column=3,row=20)
    Button2 = Buttons(frame,"Exit",frame.destroy)
    Button2.grid(column=4,row=20)
 
    ### Separators ###
    s1 = ttk.Separator(frame, orient=HORIZONTAL)
    s1.grid(row=14,columnspan=7, stick="ew",pady=2)
    s2 = ttk.Separator(frame, orient=HORIZONTAL)
    s2.grid(row=11,columnspan=7, stick="ew",pady=2)
    s3 = ttk.Separator(frame, orient=HORIZONTAL)
    s3.grid(row=9,columnspan=7, stick="ew",pady=2)
### Initialize window ###
def main(): 
    root = Tk()
    frame = ttk.Frame(root)
    app1 = main_window(root)
    root.mainloop()

### Start program ###
if __name__ == '__main__':
    main()
