

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: object
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置\1

        """
        self.ui = ui
        # TODO 组件初始化 赋值操作
    def Options(self):
        print("点击了菜单")
    def mode1(self,evt):
        print("<<ComboboxSelected>>事件未处理:",evt)
    def mode4(self,evt):
        print("<<ComboboxSelected>>事件未处理:",evt)
    def mode5(self,evt):
        print("<<ComboboxSelected>>事件未处理:",evt)
    def mode6(self,evt):
        print("<<ComboboxSelected>>事件未处理:",evt)
    def connect(self,evt):
        print("<Button-1>事件未处理:",evt)
    def disconnect(self,evt):
        print("<Button-1>事件未处理:",evt)
    def get_Waveform(self,evt):
        print("<Button-1>事件未处理:",evt)
