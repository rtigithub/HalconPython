import sys
from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcom to Halcon")
window.geometry('325x250')
window.configure(background = "gray")
ttk.Button(window, text="Hello").grid()
window.mainloop()

# clr from package pythonnet
import clr
clr.AddReference("System")
from System import Environment

# Begin setting up access to Halcon
# Add path to halcondotnet.dll
HALCONROOT = Environment.GetEnvironmentVariable("HALCONROOT")
sys.path.append(HALCONROOT+"/bin/dotnet35")

# Add halcondotnet reference
clr.AddReference("halcondotnet")
clr.AddReference("hdevenginedotnet")

# import HALCON from namespace
from HalconDotNet import *
# End setting up access to Halcon

ho_Image = HImage()
ho_ImageInvert = HImage()
hv_WindowHandle = HWindow()

HSystem.SetWindowAttr("background_color","black")

# Unless using HTuple variable, explicit cast to HTuple required
hv_WindowHandle.OpenWindow(0,0,256,256,HTuple(0),"visible","")

# Read image and display for 5 seconds
ho_Image.ReadImage("mreut")
hv_WindowHandle.DispImage(ho_Image)
HSystem.WaitSeconds(5)

# Invert image and display for 5 seconds
ho_ImageInvert = ho_Image.InvertImage( )
hv_WindowHandle.DispImage(ho_ImageInvert)
HSystem.WaitSeconds(5)

# Clean up
hv_WindowHandle.CloseWindow()
ho_Image.Dispose()
ho_ImageInvert.Dispose()
hv_WindowHandle.Dispose()