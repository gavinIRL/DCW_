import tkinter as tk
import tkinter.font as tkFont
from g_utils import G_Utils
from analysis_window import AnalysisWindow
from wallet_window import WalletWindow


class MainWindow():

    def __init__(self, root):
        self.root = root
        # set variables
        self.newWindowAnalysis = None
        self.newWindowWallet = None
        # set fonts
        ftButton = tkFont.Font(family='Times', size=16)
        ft = tkFont.Font(family='Times', size=13)
        ftStatus = tkFont.Font(family='Times', size=16, weight="bold")
        # setting title
        self.root.title("Helper")
        # setting window size
        width = 300
        height = 321
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.btnAnalysis = tk.Button(self.root)
        self.btnAnalysis["font"] = ftButton
        self.btnAnalysis["justify"] = "center"
        self.btnAnalysis["text"] = "Open Analysis Window"
        self.btnAnalysis.place(x=0, y=230, width=width, height=30)
        self.btnAnalysis["command"] = self.btnAnalysis_command

        btnLog = tk.Button(self.root)
        btnLog["font"] = ftButton
        btnLog["justify"] = "center"
        btnLog["text"] = "Open X"
        btnLog.place(x=0, y=160, width=width, height=30)
        btnLog["command"] = self.btnLog_command

        lblBitcoinPrice = tk.Label(self.root)
        lblBitcoinPrice["font"] = ft
        lblBitcoinPrice["justify"] = "center"
        lblBitcoinPrice["text"] = "Bitcoin price at login: $" + str(
            G_Utils.days_until_christmas())
        lblBitcoinPrice.place(x=0, y=125, width=width, height=30)

        lblStart = tk.Label(self.root)
        lblStart["font"] = ft
        lblStart["justify"] = "center"
        lblStart["text"] = "Status 1"
        lblStart.place(x=0, y=95, width=width, height=30)

        self.btnWallet = tk.Button(self.root)
        self.btnWallet["font"] = ftButton
        self.btnWallet["justify"] = "center"
        self.btnWallet["text"] = "Open Wallet"
        self.btnWallet.place(x=0, y=195, width=width, height=30)
        self.btnWallet["command"] = self.btnWallet_command

        btnClose = tk.Button(self.root)
        btnClose["font"] = ftButton
        btnClose["justify"] = "center"
        btnClose["text"] = "Close"
        btnClose.place(x=0, y=290, width=width, height=30)
        btnClose["command"] = self.btnClose_command

        self.lblVPNStatus = tk.Label(self.root)
        self.lblVPNStatus["font"] = ftStatus
        self.lblVPNStatus["justify"] = "center"
        self.lblVPNStatus["text"] = "User Status: " + \
            str(G_Utils.checkSettingsFileExists())
        self.lblVPNStatus.place(x=0, y=5, width=width, height=30)

        self.lblBlockStatus = tk.Label(self.root)
        self.lblBlockStatus["font"] = ftStatus
        self.lblBlockStatus["justify"] = "center"
        self.lblBlockStatus["text"] = "User Net Worth: " + \
            str(G_Utils.getNetWorth())
        self.lblBlockStatus.place(x=0, y=35, width=width, height=30)

        lblBirthday = tk.Label(self.root)
        lblBirthday["font"] = ft
        lblBirthday["justify"] = "center"
        lblBirthday["text"] = "Status 2"
        lblBirthday.place(x=0, y=65, width=width, height=30)

    def destroyAnalysis(self):
        self.newWindowAnalysis.destroy()
        self.btnAnalysis["state"] = "normal"

    def destroyWallet(self):
        self.newWindowWallet.destroy()
        self.btnWallet["state"] = "normal"

    def new_window(self, _class):
        if _class is WalletWindow:
            self.btnWallet["state"] = "disabled"
            self.newWindowWallet = tk.Toplevel(self.root)
            self.newWindowWallet.protocol(
                "WM_DELETE_WINDOW", self.destroyWallet)
            _class(self, self.newWindowWallet)
        else:
            self.btnAnalysis["state"] = "disabled"
            self.newWindowAnalysis = tk.Toplevel(self.root)
            self.newWindowAnalysis.protocol(
                "WM_DELETE_WINDOW", self.destroyAnalysis)
            _class(self, self.newWindowAnalysis)

    def btnLog_command(self):
        pass

    def btnClose_command(self):
        # then close
        self.root.destroy()

    def btnAnalysis_command(self):
        self.new_window(AnalysisWindow)

    def btnWallet_command(self):
        self.new_window(WalletWindow)


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-toolwindow', True)
    MainWindow = MainWindow(root)

    def checkPrices():
        # Perform an update of the information
        pass
        root.after(30000, checkPrices)
    root.after(30, checkPrices)
    root.wm_attributes('-topmost', True)
    root.mainloop()
