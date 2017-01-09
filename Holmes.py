#brew install wxpython
#sudo apt install linuxbrew-wrapper
#sudo apt install python-pip
#pip install SpeechRecognition
#sudo apt-get install python-pyaudio python3-pyaudio
#pip install --allow-unverified=pyaudio pyaudio
#sudo apt-get install python-wxtools
#sudo pip install pyttsx
#sudo pip install wikipedia

#IF MEMORYERROR = run as sudo pip --no-cache-dir install SpeechRecognition
'''
Holmes: The Know-It-All Encyclopedia who will assist you
        in your search for knowledge.

Copyright (c) 2017 Revekka Kostoeva

'''
#Imports
import wx
import wikipedia
import pyttsx
import pyaudio

#Define engine for speech, set properties (rate, accent)
engine = pyttsx.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', "en-scottish")

#Define boolean variable
work = True

#Create frame (GUI)
class MyFrame(wx.Frame):
    def __init__(self):
        #GUI
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition,
            size = wx.Size(450, 100),
            style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
            | wx.CLIP_CHILDREN,
            title = "Holmes")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label = "Hello. How may my superior mind assist you today?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()

        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        engine.say("Hello. How may my superior mind assist you today?")#" How may I assist you today?")
        engine.runAndWait()

#Define OnEnter click event
    def OnEnter(self, event):
        while work:
            input = self.txt.GetValue()
            input = input.lower()
            for char in input:
                if char == 'more':
                    engine.say(wikipedia.summary(input, sentences = 1))
                    #engine.runAndWait()
                if char == 'hi' or 'hello':
                    engine.say("Hello)
                    engine.say("dear!")
                    #engine.runAndWait()
                else:
                    engine.say(wikipedia.summary(input, sentences = 2))
            engine.runAndWait()

#Main
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
