Apex Broadband Source 
==========================

Capabilities
*****************************

The Apex Broadband Source is a high performance Broadband Amplified Spontaneous Emission (ASE) source. The source is capable of providing a high power output over upto +21 dBm with a broad spectrum. The broadband source can be combined with a WSS to make a comb source, or for introducing ASE noise in optical systems. The device is connected via GPIB interface for control and monitoring.

.. list-table:: Apex Broadband Source Specifications
   :widths: 50 50
   :header-rows: 1

   * - **Feature**
     - **Description**
   * - Output Power
     - +21 dBm
   * - Wavelength Range
     - 1529 nm to 1570 nm (C-Band)
   * - Output Power Stability
     - 0.02 dB
   * - Spectrum Flatness
     - +/-2 dB

.. Caution::
   The Apex Broadband Source is an extremely high power optical device. The device is only meant to be used in combination with a VOA, or a splitter. As a caution, a 10 dB attenuator is already added to the output port of the device. Do NOT connect any other component (other than fibers) directly to the Apex Broadband Source.

``BBS`` API
*****************************

.. automodule:: tcdona3.bbsource
   :members:
   :undoc-members:
   :show-inheritance:
