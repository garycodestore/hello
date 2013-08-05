#!/usr/bin/python
import wx

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(None)
		self.frame.Show()
		return True


class MyFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition, 
						style=wx.DefaultPosition, size=wx.DEFAULT_FRAME_STYLE, name="MyFrame"):
		super(MyFrame, self).__init__(parent, id, title, pos, size, style, name)

		self.panel = wx.Panel(self)
		self.button1 = wx.Button(self.panel, label="Crawl", pos=(100, 325))
		self.button2 = wx.Button(self.panel, label="Save", pos=(200, 325))
		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.button1, 0, wx.ALL, 10)
		sizer.Add(self.button2, 0, wx.ALL, 10)
		self.panel.SetSizer(sizer)

		self.Bind(wx.EVT_BUTTON, self.OnButton, self.button1)


		self.logger = wx.TextCtrl(self, pos=(30, 20), size=(280, 300), style=wx.TE_MULTILINE|wx.TE_READONLY)
		self.Show()

	def OnButton(self, event):
		event_id = event.GetId()
		event_obj = event.GetEventObject()
		print ""


if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()
