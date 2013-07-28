#!/usr/bin/python
import wx

class ExampleFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent)
		
		panel = wx.Panel(self)
		self.quote = wx.StaticText(panel, label="your quote: ", pos=(20, 30))
		self.logger = wx.TextCtrl(self, pos=(300, 20), size=(200, 300), style=wx.TE_MULTILINE|wx.TE_READONLY)
		
		self.button = wx.Button(self, label="Save", pos=(200, 325))
		#self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

		self.Show()

app = wx.App(False)
ExampleFrame(None)
app.MainLoop()
