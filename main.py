from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title ("KCDC Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="dark blue")

        cmbNameTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssuedDate=StringVar()
        DailyDose=StringVar()
        PossibleSideEffects=StringVar()
        FurtherInformation=StringVar()
        StorageAdvice=StringVar()
        DrivingUsingMachines=StringVar()
        HowtoUseMedication=StringVar()
        PatientID=StringVar()
        PatientNHSNo=StringVar()
        DateofBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label (TitleFrame, font=('arial', 40, 'bold'), text="KCDC Management System", padx=2)
        self.lblTitle.grid()

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = Frame(DataFrame, bd=10, width=800, height=400, padx=20, relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = Frame(DataFrame, bd=10, width=450, height=400, padx=20, relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)
        #============================DataFrameLeft======================================
        self.lblNameTablet = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Name of Tablets:", padx=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(DataFrameLEFT, textvariable=cmbNameTablets, state='readonly', font=('arial', 12, 'bold'), width=20)

        self.cboNameTablet['value']=('','Ibuprofen', 'Codine', 'Naltrexone', 'Acamprosate', 'Disulfiram', 'Bupropion', 'Gabapentin', 'Varenicline')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.lblFurtherInfo = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information: ", padx=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= FurtherInformation)
        self.txtFurtherInfo.grid(row=0, column=3)

        self.lblRef = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Reference No", padx=2)
        self.lblRef.grid(row=1, column=0, sticky=W)
        self.txtRef=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= Ref)
        self.txtRef.grid(row=1, column=1)

        self.lblStorage = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage Advice: ", padx=2)
        self.lblStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= StorageAdvice)
        self.txtStorage.grid(row=1, column=3)

        self.lblDose = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Dosage: ", padx=2)
        self.lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= Dose)
        self.txtDose.grid(row=2, column=1)

        self.lblDUseMachine = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Driving Machines ", padx=2)
        self.lblDUseMachine.grid(row=2, column=2, sticky=W)
        self.txtDUseMachine=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= DrivingUsingMachines)
        self.txtDUseMachine.grid(row=2, column=3)

        self.lblNoOfTablets = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="No. of Tablets", padx=2)
        self.lblNoOfTablets.grid(row=3, column=0, sticky=W)
        self.txtNoOfTablets=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= NumberTablets)
        self.txtNoOfTablets.grid(row=3, column=1)

        self.lblUseMedication = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Driving Machines", padx=2)
        self.lblUseMedication.grid(row=3, column=2, sticky=W)
        self.txtUseMedication=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= HowtoUseMedication)
        self.txtUseMedication.grid(row=3, column=3)

        self.lblLot = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot: ", padx=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= Lot)
        self.txtLot.grid(row=4, column=1)

        self.lblPatientID = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot: ", padx=2)
        self.lblPatientID.grid(row=4, column=0, sticky=W)
        self.txtPatientID=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= Lot)
        self.txtPatientID.grid(row=4, column=1)

        self.lblIssuedDate = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Issued Date: ", padx=2)
        self.lblIssuedDate.grid(row=4, column=2, sticky=W)
        self.txtIssuedDate=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= IssuedDate)
        self.txtIssuedDate.grid(row=4, column=3)












if __name__=='__main__':
    root = Tk()
    application = Hospital (root)
    root.mainloop()
