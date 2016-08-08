from tkinter import *
from tkinter import ttk

root = Tk()

# create a toplevel menu
menubar = Menu(root)

def donothing():
    print ("a")
def updatevalue(evt):
    widget = evt.widget
    txt = widget.get()
    vals = widget.cget('values')

    if not vals:
        widget.configure(values = (txt, ))
    elif txt not in vals:
        widget.configure(values =vals + (txt, ))
    
    return 'break'
def newinp():
    TOP = Toplevel()
    TOP.title('New deMon2k Input')
    TOP.focus_set()
    TOP.config(height=300, width=300)
    frame = ttk.Frame(TOP, borderwidth=5, relief="sunken", width=200, height=200, padding="3 3 12 12")
    finp = ttk.Label(TOP, text="File name:")
    finp.grid(column=1, row=1)

    file_name_var = StringVar()
    file_name = ttk.Entry(TOP, width=20, textvariable=file_name_var)
    file_name.grid(column=2, row=1, stick=(W, E))

    ti = ttk.Label(TOP, text="Title:")
    ti.grid(column=1, row=2)

    title_var = StringVar()
    title = ttk.Entry(TOP, width=20, textvariable=title_var)
    title.grid(column=2, row=2, stick=(W, E))

    vxctyp_var = StringVar()
    auxis = ttk.Radiobutton(TOP, text="Auxis", variable=vxctyp_var, value="AUXIS")
    basis = ttk.Radiobutton(TOP, text="Basis", variable=vxctyp_var, value="BASIS")
    auxis.grid(column=3, row=3)
    basis.grid(column=2, row=3)
    
    vxctyp_ti = ttk.Label(TOP, text="VXCTYP")
    vxctyp_ti.grid(column=1, row=3)

    functionalX_ti = ttk.Label(TOP, text="Exchange Functional")
    functionalX_ti.grid(column=1,row=4)
    
    functionalX_list=('PW86','B88','PW91','PBE96','TPSS')
    functionalX = ttk.Combobox(TOP, values=functionalX_list)
    functionalX.bind('<Return>', updatevalue)
    functionalX.grid(column=2,row=4)

    functionalC_ti = ttk.Label(TOP, text="Correlation Functional")
    functionalC_ti.grid(column=3,row=4)

    functionalC_list=('VWN',"PW92","LYP","PW91","PBE","TPSS")
    functionalC = ttk.Combobox(TOP, values=functionalC_list)
    functionalC.bind('<Return>', updatevalue)
    functionalC.grid(column=4,row=4)

    basis_set_ti = ttk.Label(TOP, text="Basis Set")
    basis_set_ti.grid(column=1,row=5)

    basis_set_list=('DZVP','DZVP-GGA','TZVP','TZVP-GGA')
    basis_set = ttk.Combobox(TOP, values=basis_set_list)
    basis_set.bind('<Return>', updatevalue)
    basis_set.grid(column=2,row=5)

    auxis_set_ti = ttk.Label(TOP, text="Auxis set")
    auxis_set_ti.grid(column=3,row=5)
    
    auxis_set_list=('gen-a1','gen-a2','gen-a2**','gen-a3**')
    auxis_set = ttk.Combobox(TOP, values=auxis_set_list)
    auxis_set.bind('<Return>', updatevalue)
    auxis_set.grid(column=4,row=5)

    shelltyp_ti = ttk.Label(TOP, text="Shell type:")
    shelltyp_ti.grid(column=1,row=6)

    shelltyp_list=('RKS','ROKS','UKS')
    shelltyp = ttk.Combobox(TOP,values=shelltyp_list, state='readonly')
    shelltyp.grid(column=2,row=6)

    scfmaxiter_ti = ttk.Label(TOP, text="Max Iterations for SCF:")
    scfmaxiter_ti.grid(column=3,row=6)

    scfmaxiter_var = StringVar()
    scfmaxiter = ttk.Entry(TOP, width=5, textvariable=scfmaxiter_var)
    scfmaxiter.grid(column=4,row=6)


    tol_ti = ttk.Label(TOP, text="Tolerance")
    tol_ti.grid(column=1, row=7)
    
    tol_var = StringVar()
    tol = ttk.Entry(TOP, width=10, textvariable=tol_var)
    tol.grid(column=2,row=7)
    
    guess_ti = ttk.Label(TOP, text="Guess")
    guess_ti.grid(column=3,row=7)

    guess_list=('TB','CORE','Fermi')
    guess = ttk.Combobox(TOP, values=guess_list)
    guess.grid(column=4,row=7)

    calctyp_ti = ttk.Label(TOP, text="Calculation type:")
    calctyp_ti.grid(column=1,row=8)

    calc_var = StringVar()
    singpnterg = ttk.Radiobutton(TOP, text="Single Point Energy", variable=calc_var, value="SPE")
    optimize = ttk.Radiobutton(TOP, text="OPTIMIZATION", variable=calc_var, value="OPT")
    singpnterg.grid(column=2, row=8)
    optimize.grid(column=3, row=8)

    freq_var = StringVar()
    freq = ttk.Checkbutton(TOP, text="Frequency Analysis", variable=freq_var, onvalue='on', offvalue='off')
    freq.grid(column=4,row=8)
    
    geometry_ti = ttk.Label(TOP, text="Input Geometry file name:")
    geometry_ti.grid(column=1,row=9)

    geometry_var = StringVar()
    geometry = ttk.Entry(TOP, textvariable=geometry_var)
    geometry.grid(column=2,row=9)

    thermo_var = StringVar()
    thermo = ttk.Checkbutton(TOP, text="Thermo calculation",variable=thermo_var, onvalue='on', offvalue='off')
    thermo.grid(column=4,row=9)

    multiplicity_ti = ttk.Label(TOP, text="Multiplicity")
    multiplicity_ti.grid(column=1,row=10)

    multiplicity_var = StringVar()
    multiplicity = ttk.Entry(TOP, width=5,textvariable=multiplicity_var)
    multiplicity.grid(column=2,row=10)

    charge_ti = ttk.Label(TOP, text="Charge")
    charge_ti.grid(column=3,row=10)
    
    charge_var = StringVar()
    charge = ttk.Entry(TOP, width=5,textvariable=charge_var)
    charge.grid(column=4,row=10)


    create = ttk.Button(TOP, text="Create Input", command=donothing)
    create.grid(column=4, row=20)
    cancel = ttk.Button(TOP, text="Cancel", command=TOP.destroy)
    cancel.grid(column=5, row=20)


def file_save():
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".inp")
    if f is None:
        return
    text2save = str(text.get(1.0, END))
    f.write(text2save)
    f.close()
def callback():
    name=askopenfilename()
    print (name)



# display the menu
root.config(menu=menubar)

#create a pulldown menu, and add it to the menu bar

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newinp)
filemenu.add_command(label="Open", command=callback)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)


root.mainloop()
