from .modules import make_gr_data


class Chart01Function:
    def __init__(self):
        gr = make_gr_data.GrTree()
        self.tx_str, self.ty_str = gr.draw()

    def get_xstr(self):
        return self.tx_str

    def get_ystr(self):
        return self.ty_str


class Chart02Function:
    def __init__(self):
        gr = make_gr_data.GrFern()
        self.tx_str, self.ty_str = gr.draw()

    def get_xstr(self):
        return self.tx_str

    def get_ystr(self):
        return self.ty_str


class Chart03Function:
    def __init__(self):
        gr = make_gr_data.GrGasket()
        self.tx_str, self.ty_str = gr.draw()

    def get_xstr(self):
        return self.tx_str

    def get_ystr(self):
        return self.ty_str


class Chart04Function:
    def __init__(self):
        gr = make_gr_data.GrSnow()
        self.tx_str, self.ty_str = gr.draw()

    def get_xstr(self):
        return self.tx_str

    def get_ystr(self):
        return self.ty_str


class Chart05Function:
    def __init__(self):
        gr = make_gr_data.GrCcurve()
        self.tx_str, self.ty_str = gr.draw()

    def get_xstr(self):
        return self.tx_str

    def get_ystr(self):
        return self.ty_str
