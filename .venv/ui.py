#界面
import random
from tkinter import *
from tkinter.ttk import *
from ttkbootstrap import *
from pytkUI.widgets import *
class WinGUI(Window):
    def __init__(self):
        super().__init__(themename="cosmo", hdpi=False)
        self.__win()
        self.tk_label_resource_name = self.__tk_label_resource_name(self)
        self.tk_input_source_name = self.__tk_input_source_name(self)
        self.tk_label_channel = self.__tk_label_channel(self)
        self.tk_select_box_Channel_s = self.__tk_select_box_Channel_s(self)
        self.tk_label_times = self.__tk_label_times(self)
        self.tk_input_Timebase = self.__tk_input_Timebase(self)
        self.tk_label_voltage = self.__tk_label_voltage(self)
        self.tk_input_voltage_scale = self.__tk_input_voltage_scale(self)
        self.tk_label_trigger = self.__tk_label_trigger(self)
        self.tk_select_box_trigger_mode = self.__tk_select_box_trigger_mode(self)
        self.tk_label_Tsource = self.__tk_label_Tsource(self)
        self.tk_select_box_Tsource_s = self.__tk_select_box_Tsource_s(self)
        self.tk_label_trigger_slope = self.__tk_label_trigger_slope(self)
        self.tk_select_box_trigger_slope_mode = self.__tk_select_box_trigger_slope_mode(self)
        self.tk_label_trigger_le = self.__tk_label_trigger_le(self)
        self.tk_input_trigger_level = self.__tk_input_trigger_level(self)
        self.tk_button_connect1 = self.__tk_button_connect1(self)
        self.tk_button_disconnect1 = self.__tk_button_disconnect1(self)
        self.tk_button_getWaveform1 = self.__tk_button_getWaveform1(self)
        self.tk_label_frame_wave1 = self.__tk_label_frame_wave1(self)
    def __win(self):
        self.title("Scope")
        # 设置窗口大小、居中
        width = 950
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def new_style(self,widget):
        ctl = widget.cget('style')
        ctl = "".join(random.sample('0123456789',5)) + "." + ctl
        widget.configure(style=ctl)
        return ctl
    def __tk_label_resource_name(self,parent):
        label = Label(parent,text="resource_name",anchor="center", bootstyle="default")
        label.place(x=0, y=0, width=100, height=20)
        return label
    def __tk_input_source_name(self,parent):
        ipt = Entry(parent, bootstyle="dark")
        ipt.place(x=0, y=20, width=400, height=20)
        return ipt
    def __tk_label_channel(self,parent):
        label = Label(parent,text="Channel",anchor="center", bootstyle="default")
        label.place(x=0, y=50, width=100, height=20)
        return label
    def __tk_select_box_Channel_s(self,parent):
        cb = Combobox(parent, state="readonly", bootstyle="dark")
        cb['values'] = ("CH1","CH2","CH3","CH4")
        cb.place(x=0, y=70, width=150, height=20)
        return cb
    def __tk_label_times(self,parent):
        label = Label(parent,text="Timebase(s/div)",anchor="center", bootstyle="default")
        label.place(x=0, y=100, width=100, height=20)
        return label
    def __tk_input_Timebase(self,parent):
        ipt = Entry(parent, bootstyle="dark")
        ipt.place(x=0, y=120, width=150, height=20)
        return ipt
    def __tk_label_voltage(self,parent):
        label = Label(parent,text="Voltage scale(V/div)",anchor="center", bootstyle="default")
        label.place(x=0, y=150, width=120, height=20)
        return label
    def __tk_input_voltage_scale(self,parent):
        ipt = Entry(parent, bootstyle="dark")
        ipt.place(x=0, y=170, width=150, height=20)
        return ipt
    def __tk_label_trigger(self,parent):
        label = Label(parent,text="Trigger mode",anchor="center", bootstyle="default")
        label.place(x=0, y=200, width=100, height=20)
        return label
    def __tk_select_box_trigger_mode(self,parent):
        cb = Combobox(parent, state="readonly", bootstyle="dark")
        cb['values'] = ("EDGE","AUTO")
        cb.place(x=0, y=220, width=150, height=20)
        return cb
    def __tk_label_Tsource(self,parent):
        label = Label(parent,text="Trigger_source",anchor="center", bootstyle="default")
        label.place(x=0, y=250, width=100, height=20)
        return label
    def __tk_select_box_Tsource_s(self,parent):
        cb = Combobox(parent, state="readonly", bootstyle="dark")
        cb['values'] = ("CH1","CH2","CH3","CH4")
        cb.place(x=0, y=270, width=150, height=20)
        return cb
    def __tk_label_trigger_slope(self,parent):
        label = Label(parent,text="Trigger slope",anchor="center", bootstyle="default")
        label.place(x=0, y=300, width=100, height=20)
        return label
    def __tk_select_box_trigger_slope_mode(self,parent):
        cb = Combobox(parent, state="readonly", bootstyle="dark")
        cb['values'] = ("NA","NA2","NA3")
        cb.place(x=0, y=320, width=150, height=20)
        return cb
    def __tk_label_trigger_le(self,parent):
        label = Label(parent,text="Trigger level",anchor="center", bootstyle="default")
        label.place(x=0, y=340, width=100, height=20)
        return label
    def __tk_input_trigger_level(self,parent):
        ipt = Entry(parent, bootstyle="dark")
        ipt.place(x=0, y=360, width=150, height=20)
        return ipt
    def __tk_button_connect1(self,parent):
        btn = Button(parent, text="connect", takefocus=False,bootstyle="dark")
        btn.place(x=20, y=550, width=100, height=30)
        return btn
    def __tk_button_disconnect1(self,parent):
        btn = Button(parent, text="disconnect", takefocus=False,bootstyle="dark")
        btn.place(x=200, y=550, width=100, height=30)
        return btn
    def __tk_button_getWaveform1(self,parent):
        btn = Button(parent, text="getWaveform", takefocus=False,bootstyle="dark")
        btn.place(x=360, y=550, width=100, height=30)
        return btn
    def __tk_label_frame_wave1(self,parent):
        frame = LabelFrame(parent,text="wave",bootstyle="default")
        frame.place(x=238, y=50, width=640, height=480)
        return frame
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.config(menu=self.create_menu())
        self.ctl.init(self)
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_command(label="选项",command=self.ctl.Options)
        return menu
    def __event_bind(self):
        self.tk_select_box_Channel_s.bind('<<ComboboxSelected>>',self.ctl.mode1)
        self.tk_select_box_trigger_mode.bind('<<ComboboxSelected>>',self.ctl.mode4)
        self.tk_select_box_Tsource_s.bind('<<ComboboxSelected>>',self.ctl.mode5)
        self.tk_select_box_trigger_slope_mode.bind('<<ComboboxSelected>>',self.ctl.mode6)
        self.tk_button_connect1.bind('<Button-1>',self.ctl.connect)
        self.tk_button_disconnect1.bind('<Button-1>',self.ctl.disconnect)
        self.tk_button_getWaveform1.bind('<Button-1>',self.ctl.get_Waveform)
        pass
    def __style_config(self):
        sty = Style()
        sty.configure(self.new_style(self.tk_label_resource_name),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_channel),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_times),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_voltage),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_trigger),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_Tsource),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_trigger_slope),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_label_trigger_le),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_connect1),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_disconnect1),font=("微软雅黑",-12))
        sty.configure(self.new_style(self.tk_button_getWaveform1),font=("微软雅黑",-12))
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()