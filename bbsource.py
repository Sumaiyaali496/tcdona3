import pyvisa
from time import sleep


class BBS:
    """Class for controlling the Apex Broadband Source"""

    def __init__(self):
        rm = pyvisa.ResourceManager()
        self.base = rm.open_resource("GPIB0::3::INSTR")
        # self.base.timeout = None
        # self.base.read_termination = None
        # self.base.write_termination = None

    def identify(self):
        """Identify the instrument"""
        return self.base.query("*IDN?")

    def get_sw_version(self):
        return self.base.query("SOFT?")

    def set_poweron(self):
        """Turn on the instrument"""
        return self.base.write("ASEON")

    def set_poweroff(self):
        """Turn off the instrument"""
        return self.base.write("ASEOFF")

    def check_poweron(self):
        """Check if the instrument is on"""
        return self.base.query("ASEON?")

    def check_poweroff(self):
        """Check if the instrument is off"""
        return self.base.query("ASEOFF?")

    def check_unitdbm(self):
        """Check the power output (dBm)"""
        return self.base.query("ASEdBm?")

    def check_unitmw(self):
        """Check the power output (mW)"""
        return self.base.query("ASEmW?")
