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
        ExpDate = StringVar()
        #====================================FUCTION DECLRATIOON==================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("KCDC Management System","Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return

        def iPrescription():
            return
        
        def iReceipt():

            return

        def iDelete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            ExpDate.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            return

        def iReset():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            ExpDate.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            return


        #=================================================FRAME==================================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=20, width=2500, padx=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label (TitleFrame, font=('arial', 40, 'bold'), text="KCDC Management System", padx=2)
        self.lblTitle.grid()

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=2500, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=2500, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, font=('arial', 12, 'bold'), text ="Patient Informatioon")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE, font=('arial', 12, 'bold'), text="Prescription")
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
        self.txtPatientID=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= PatientID)
        self.txtPatientID.grid(row=4, column=1)

        self.lblIssuedDate = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Issued Date: ", padx=2)
        self.lblIssuedDate.grid(row=4, column=2, sticky=W)
        self.txtIssuedDate=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= IssuedDate)
        self.txtIssuedDate.grid(row=4, column=3)
        
        self.lblDaileyDose = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Daily Dose: ", padx=2)
        self.lblDaileyDose.grid(row=5, column=0, sticky=W)
        self.lblDaileyDose=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= DailyDose)
        self.lblDaileyDose.grid(row=5, column=1)

        self.lblPossibleSideEffects = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Possible Side Effects: ", padx=2)
        self.lblPossibleSideEffects.grid(row=5, column=2, sticky=W)
        self.lblPossibleSideEffects=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= PossibleSideEffects)
        self.lblPossibleSideEffects.grid(row=5, column=3)

        self.lblPatientNHSNo = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient NHS No.", padx=2)
        self.lblPatientNHSNo.grid(row=6, column=0, sticky=W)
        self.lblPatientNHSNo=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= PatientNHSNo)
        self.lblPatientNHSNo.grid(row=6, column=1)

        self.lblDateOfBirth = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Date of Birth", padx=2)
        self.lblDateOfBirth.grid(row=6, column=2, sticky=W)
        self.lblDateOfBirth=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= DateofBirth)
        self.lblDateOfBirth.grid(row=6, column=3)

        self.lblPatientAddress = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Address: ", padx=2)
        self.lblPatientAddress.grid(row=7, column=0, sticky=W)
        self.lblPatientAddress=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= PatientAddress)
        self.lblPatientAddress.grid(row=7, column=1)

        self.lblExpDate = Label (DataFrameLEFT, font=('arial', 12, 'bold'), text="Expire Date", padx=2)
        self.lblExpDate.grid(row=7, column=2, sticky=W)
        self.lblExpDate=Entry(DataFrameLEFT, font=('arial', 12, 'bold'),  textvariable= ExpDate)
        self.lblExpDate.grid(row=7, column=3)

        #====================Right Side=====================================================
        self.txtPrescription =Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=43, height=14, padx=2)
        self.txtPrescription.grid(row=0, column=0)

        #====================ButtonFrame=====================================================
        self.btnPrescription=Button(ButtonFrame, text='Prescription', font=('arial', 12, 'bold'), width=15, bd=4, command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        self.btnReceipt=Button(ButtonFrame, text='Receipt', font=('arial', 12, 'bold'), width=15, bd=4, command=iReceipt)
        self.btnReceipt.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame, text='Delete', font=('arial', 12, 'bold'), width=15, bd=4, command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        self.btnReset=Button(ButtonFrame, text='Reset', font=('arial', 12, 'bold'), width=15, bd=4, command=iReset)
        self.btnReset.grid(row=0,column=3)
        self.btnExit=Button(ButtonFrame, text='Exit', font=('arial', 12, 'bold'), width=15, bd=4, command=iExit)
        self.btnExit.grid(row=0,column=4)

        #====================Frame Detail=====================================================
        self.lblLabel = Label(FrameDetail, font=('arial', 10, 'bold'), pady=8,text="Tablet Name\tReference No.\t Dosage\t No. of Tablets\t Lot\t Issued Date\t Exp. Date",)
        self.lblLabel.grid(row=0, column=0)

        self.FrameDetail =Text(FrameDetail, font=('arial', 12, 'bold'), width=141, height=8, padx=2)
        self.FrameDetail.grid(row=1, column=0)




if __name__=='__main__':
    root = Tk()
    application = Hospital (root)
    root.mainloop()
