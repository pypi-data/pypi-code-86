import wx

from .icons import icons8_usb_connector_50
from .mwindow import MWindow

_ = wx.GetTranslation


class UsbConnect(MWindow):
    def __init__(self, *args, **kwds):
        super().__init__(915, 424, *args, **kwds)

        self.text_main = wx.TextCtrl(
            self, wx.ID_ANY, "", style=wx.TE_BESTWRAP | wx.TE_MULTILINE | wx.TE_READONLY
        )
        self.text_entry = wx.TextCtrl(
            self, wx.ID_ANY, "", style=wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB
        )

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT_ENTER, self.on_entry, self.text_entry)
        # end wxGlade
        self.pipe = None

    def window_open(self):
        self.context.channel("pipe/usb", buffer_size=500).watch(self.update_text)

    def window_close(self):
        self.context.channel("pipe/usb").unwatch(self.update_text)

    def update_text(self, text):
        if not wx.IsMainThread():
            wx.CallAfter(self.update_text_gui, text + "\n")
        else:
            self.update_text_gui(text + "\n")

    def update_text_gui(self, text):
        try:
            self.text_main.AppendText(text)
        except RuntimeError:
            pass

    def __set_properties(self):
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(icons8_usb_connector_50.GetBitmap())
        self.SetIcon(_icon)
        # begin wxGlade: Terminal.__set_properties
        self.SetTitle(_("UsbConnect"))
        self.text_entry.SetFocus()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Terminal.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.text_main, 20, wx.EXPAND, 0)
        sizer_2.Add(self.text_entry, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def on_entry(self, event):
        if self.pipe is not None:
            self.pipe.write(self.text_entry.GetValue() + "\n")
            self.text_entry.SetValue("")
        event.Skip()
