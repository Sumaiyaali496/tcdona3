Teraflex Transceiver
====================

Capabilities
**************************

The ADVA Teraflex transceiver is a 1RU terminal that enables optical transmissions upto 600 Gbps, with modulation formats ranging from DP-QPSK to DP-64QAM. 

#. Tuning Range 191.15 THz to 196.1 THz on 25GHz grid
#. Modulation Formats: DP-QPSK, DP-16QAM, DP-32QAM, DP-64QAM
#. Transmit Power: -10 dBm to +3 dBm in 0.1dB steps
#. Receiver power: single carrier input range -22 dBm to +3 dBm

.. Caution::

   Other specific configuration changing methods should be dealt with caution. Unless you have highly specific configuration requirements, refrain from using other options. Use the :meth:`teraflex.TFlex.change_configuration` method instead.

``TFlex`` API
**************************

Class to interact with the Teraflex device using NETCONF protocol

You would not be able to initialize this class unless you have been allocated as the patch owners for the Teraflex device, or the device is not being used. 

Usually, you should only use the following methods:

- :meth:`teraflex.TFlex.change_configuration`

- :meth:`teraflex.TFlex.read_pm_data`

- :meth:`teraflex.TFlex.set_power_and_frequency`

You can also use all the read-only methods such as :meth:`teraflex.TFlex.get_interface`, :meth:`teraflex.TFlex.get_symbolrate`, :meth:`teraflex.TFlex.get_filterrolloff`, :meth:`teraflex.TFlex.get_fec_algorithm`, :meth:`teraflex.TFlex.get_power_and_frequency`, :meth:`teraflex.TFlex.get_interface_modulation`. 

For the other methods, currently we have 4 line ports available: [1/1/n1, 1/1/n2, 1/2/n1, 1/2/n2]. This denotes shelf/rack/port. 

.. automodule:: tcdona3.teraflex
   :members:
   :undoc-members:
   :show-inheritance:


Usage
**************************

.. Note::
   This section is still under development.