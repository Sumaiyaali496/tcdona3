import serial


class Dicon:
    def __init__(self, port, baudrate=115200, timeout=1):
        """
        Initialize the connection to the DiCon Matrix Switch.

        :param port: The COM port the switch is connected to (e.g., 'COM3' or '/dev/ttyUSB0').
        :param baudrate: Communication speed, default is 115200.
        :param timeout: Timeout for reading from the switch.
        """
        self.ser = serial.Serial(port, baudrate, timeout=timeout)

    def send_command(self, command):
        """
        Send a command to the switch and return the response.

        :param command: The command string to send (e.g., 'X1 CH 1 1').
        :return: Response from the switch.
        """
        if not command.endswith("\n"):
            command += "\n"
        self.ser.write(command.encode())
        response = self.ser.readline().decode().strip()
        return response

    def connect_ports(self, input_port, output_port):
        """
        Connect an input port to an output port.

        :param input_port: The input port number.
        :param output_port: The output port number.
        :return: The response from the switch after connecting the ports.
        """
        command = f"X1 CH {input_port} {output_port}"
        return self.send_command(command)

    def clear_all_connections(self):
        """
        Clear all connections by resetting the switch to default parking state.

        :return: The response from the switch.
        """
        command = "X1 CH * 0"  # Connect all inputs to park (output channel 0)
        return self.send_command(command)

    def get_connection_status(self, input_port):
        """
        Get the current connection status of a specific input port.

        :param input_port: The input port number.
        :return: The output port the input port is currently connected to.
        """
        command = f"X1 CH? {input_port}"
        return self.send_command(command)

    def reboot_device(self):
        """
        Reboot the switch device.

        :return: The response from the switch.
        """
        command = "REBOOT"
        return self.send_command(command)

    def close(self):
        """
        Close the serial connection.
        """
        self.ser.close()
