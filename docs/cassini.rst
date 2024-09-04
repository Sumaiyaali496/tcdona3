Cassini Transciever
=======================

Capabilities
*****************************

Cassini is a 1.5-RU open packet optical transponder, available as a commercial open network product from Edgecore. It offers a flexible mix of 100 Gigabit Ethernet (GbE) packet switching ports and 100/200 Gbps coherent optical interfaces. Cassini integrates 100GbE L2/L3 switching with L1 optical transport functions as line-card modules. 

Open Ireland Testbed currently has 4 Digital Coherent Optics Transcievers (DCOs) installed in the Cassini. The DCOs are capable of 100Gbps and 200Gbps transmission, at *dp-qpsk* and *dp-16qam* modulation formats. The Cassini can be configured and monitored through the Transponder Abstraction Interface (TAI). TAI, defines the API to provide a form-factor/vendor independent way of controlling transponders and transceivers from various vendors and implementations in a uniform manner. The Cassini TAI interfaces are hosted on Kubernetes pods for open, dissagregated access and control. More details on TAI can be found `here <https://github.com/Telecominfraproject/oopt-tai>`_.

The below library provides a high level Python API to interact with the Cassini transciever. The API is built on top of the TAI API, and provides a simplified interface to interact with the Cassini.

.. list-table:: Cassini Specifications
   :widths: 50 50
   :header-rows: 1

   * - **Feature**
     - **Description**
   * - Modulation Formats
     - dp-qpsk (100 Gbps), dp-16qam (200 Gbps)
   * - Line Rates
     - 100 Gbps, 200 Gbps
   * - Output Power
     - -1 dBm to 1 dBm


.. Caution::

   #. The Cassini is a high-power optical device. The Cassini is only meant to be used in a fiber-optical network between long optical fibers. It has the cpaacity to damage optical components, and the Polatis if connected directy. Do not connect any other component (other than fibers) directly to the Cassini without supervision. 
 
   #. Please be cautious when using the methods in this module. Turn off the Cassini when not in use, and when patching dynamically with other components in the Polatis. 


``Cassini`` API
*****************************

Library to configure and monitor the Cassini Transceiver. The Cassini is accessed by the Transponder Abstraction Interface (TAI), which is hosted on a Kubernetes pod. The library uses the paramiko library to connect to the Kubernetes pod and execute the commands. The library can be used to get the performance monitoring attributes of the Cassini Transceiver, set the modulation format, set the output power, get the operational status, get the DSP operational status, get the current post-FEC BER, get the current pre-FEC BER, get the current SD FEC BER, get the current HD FEC BER, get the current input power, get the current output power, get the transmitter laser frequency, and set the transmitter laser frequency.

.. automodule:: tcdona3.cassini
   :members:
   :undoc-members:
   :show-inheritance:

Usage
*****************************

.. Note::

  This section is still under construction. 