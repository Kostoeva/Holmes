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
import feedparser
import random

#Define engine for speech, set properties (rate, accent)
engine = pyttsx.init()
engine.setProperty('rate', 115)
engine.setProperty('voice', "en-scottish")

#List of RSS feeds for news sources
newsurls = {
    'googlenews': 'http://news.google.com/?output=rss',
    'cnn': 'http://rss.cnn.com/rss/cnn_topstories.rss',
    'wired': 'https://www.wired.com/feed/',
    'scientific american': 'http://rss.sciam.com/sciam/biology'
}

#Fetch rss feed and return parsed RSS
def parseRSS(rss_url):
    return feedparser.parse(rss_url)

    #Fetch RSS feed headlines (titles), return them as String
def getHeadlines(rss_url):
    headlines = []

    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines

#Create frame (GUI)
class MyFrame(wx.Frame):
    def __init__(self):
        #GUI Constructor
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
        engine.say("Hello. How may my superior mind assist you today?")
        engine.runAndWait()

        #Define boolean variable
        self.beginning = True

        #List to hold all headlines
        self.allHeadlines = []

#Define function to invoke when the engine event fires
    def fire(word):
	print(word)

#Define OnEnter click event
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()

        self.txt.Clear()

    	engine = pyttsx.init()
    	engine.setProperty('rate', 120)
    	engine.setProperty('voice', "en-scottish")

        if self.beginning == True:
            engine.runAndWait()
            self.beginning = False

    	#Define engine for speech, set properties (rate, accent)
        if input == '':
            phrases = ["You look marvelous today", "Ahh, to be friends with a mind as superior as my own",
            "That was a curios incident", "They were the footprints of a gigantic hound!",
            "I make a point of never having any prejudices, and of following docilely where fact may lead me",
            "It is a capital mistake to theorize in advance of the facts. Insensibly one begins to twist facts to suit theories instead of theories to suit facts",
            "It is my business to know what other people do not know",
            "Scotland Yard feels lonely without me, and it causes an unhealthy excitement among the criminal classes",
            "No man lives or has ever lived who has brought the same amount of study and of natural talent to the detection of crime which I have done",
            "Never trust to general impressions, my boy, but concentrate yourself upon details",
            "The chief proof of man's real greatness lies in his perception of his own smallness",
            "There is nothing more stimulating than a case where everything  goes against you",
            ]
            engine.say(random.choice(phrases))
            return
        if "i am bored" in input or "suprise me" in input:
            phrases = ["When you have eliminated the impossible, whatever remains, however improbably, must be the truth",
            "There is no one who knows the higher criminal world of London so well as I do",
            "Boredom is only a state of mind and it is not permanent",
            "The world is full of obvious things which nobody by any chance ever observes",
            "I trust that age doth not wither nor custom stale my infinite variety",
            "The work is its own reward",
            "Mediocrity knows nothing higher than itself; but talent instantly recognizes genius",
            "Where there is no imagination there is no horror",
            "The game is afoot",
            "You say that we go round the sun. If we went round the moon it would not make a pennyworth of difference to me or to my work",
            ]
            engine.say(random.choice(phrases))
            return
        if "hi" in input or "hello" in input:
            engine.say("Hello, dear")
            return
        elif "news" in input or "headlines" in input or "headline" in input:
            for key, url in newsurls.items():
                self.allHeadlines.extend(getHeadlines(url))
            for headline in self.allHeadlines:
                engine.say(headline)
        elif ("print" in input) and ("more" in input):
    	    input =input.replace("print", "")
    	    input =input.replace("more", "")
    	    print wikipedia.summary(input)
        elif "print" in input:
    	    input = input.replace('print', '')
    	    print wikipedia.summary(input, sentences = 2)
        elif "more" in input:
            input = input.replace("more", "")
            engine.say(wikipedia.summary(input))
        elif ("who" in input or "what" in input) and ("more" in input) and ("print" in input):
            input = input.replace("print", "")
            input = input.replace("more", "")
            print wikipedia.summary(input)
        elif ("who" in input or "what" in input) and ("more" in input):
            input = input = input.split(' ')
            input = input = " ".join(input[2:])
            engine.say(wikipedia.summary(input))
        elif ("who" in input or "what" in input) and ("print" in input):
            input = input.replace("print", "")
            print wikipedia.summary(input, sentences = 2)
        elif "who" in input or "what" in input:
            input = input.split(' ')
            input = " ".join(input[2:])
            engine.say(wikipedia.summary(input, sentences = 2))
        else:
            engine.say(wikipedia.summary(input, sentences = 2))

#Main
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
