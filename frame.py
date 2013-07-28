#!/usr/bin/python
import wx

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None)
		self.frame.Show()
		return True


class MyFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent)
		self.logger = wx.TextCtrl(self, pos=(30, 20), size=(280, 300), style=wx.TE_MULTILINE|wx.TE_READONLY)
		self.button1 = wx.Button(self, label="Crawl", pos=(100, 325))
		self.button2 = wx.Button(self, label="Save", pos=(200, 325))
		self.panel = wx.Panel(self)
		self.Show()
if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()
