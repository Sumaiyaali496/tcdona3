Quadflex Transceiver
=====================

Capabilities
**************************

Our FSP 3000 QuadFlex™ is a q00Gbit/s module capable of multiplexing up to two 100GbE/OTU-4 client signals into two ITU-T compliant coherent wavelengths. 

#. Single slot trans/muxponder with 2 integrated, flexible and tunable coherent interfaces
#. QPSK, 8QAM and 16QAM coherent transmission at 100G/150G/200G
#. High performance SD-FEC (15/25%)
#. Modulation is represented with Network Port provisioning:
   #. ot200: represent 200G/16QAM modulation
   #. ot300 (150Gb/s per network): represent 150G/8QAM modulation
   #. ot100: represents 100G/DP-QPSK modulation

.. Caution::
   #. Other specific configuration changing methods should be dealt with caution. Unless you have highly specific configuration requirements, refrain from using other options. Use the :meth:`tcdona3.quadflex.QFlex.change_configuration` method instead.
   #. Being an older model, Quadflex offers a more limited functionality and performance as compared to the Teraflex. 

``Quadflex`` API
**************************

.. automodule:: quadflex
   :members:
   :undoc-members:
   :show-inheritance:

Usage
**************************

.. Note::
   This section is still under development.