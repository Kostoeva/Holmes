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

import wx
import wikipedia
import pyttsx
import pyaudio

#Define engine for speech
engine = pyttsx.init()
engine.setProperty('rate', 120)

#voices = engine.getProperty('voices')
#for voice in voices:
    #print "Using voice: ", voice.id
engine.setProperty('voice', "en-scottish")
engine.say("Sherlock Holmes was a detective created by Newt Scamander")



engine.say("I'm a little teapot; the big brown fox jumped over the lazy dog")
#engine.runAndWait()


class MyFrame(wx.Frame):
    def __init__(self):
        #GUI
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition,
            size = wx.Size(450, 100),
            style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
            | wx.CLIP_CHILDREN,
            title = "J.A.R.V.I.S.")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label = "Hello. How may I assist you today?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()

        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        engine.say("Hello.")#" How may I assist you today?")
        engine.runAndWait()


    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()

        for char in input:
            #need space between each char for it to work: 2 + 2 not 2+2
            if char == 'more':


                engine.say(wikipedia.summary(input))
                engine.runAndWait()

            else:


                engine.say(wikipedia.summary(input, sentences = 3))
                engine.runAndWait()






if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
