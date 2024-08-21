Optical Spectrum Analyzer (OSA)
=================================

Capablities
*****************************

The Anritsu OSA (Optical Spectrum Analyzer) has excellent wavelength and level specifications that meet the DWDM requirements. It can measure and analyze wavelength, level, and SNR for up to 300 WDM-signal channels simultaneously. Accurate SNR measurements can be made with errors less than 0.2 dB.

.. list-table:: Anritsu Optical Spectrum Analyzer Datasheet
   :header-rows: 0
   :widths: 25 75

   * - **Parameter**
     - **Specification**

   * - λ accuracy
     - 20pm (1530～1570nm), 50pm (1520～1600nm)
   * - MAX. RBW
     - 50 pm
   * - RBW accuracy (0.2 nm) 
     - <3% (1530～1570nm)
   * - Level flatness
     - +/-0.1dB (1530～1570nm), +/-0.3dB (1520～1620nm)
   * - PDL
     - +/- 0.05dB (C +L band)
   * - Level linearity
     - +/- 0.05dB (C +L band)



.. Caution::

   #. The OSA is a highly sensitive optical device. Please be cautious when using the methods in this module.

   #. Pay attention to the input power level when using the OSA. It is advisable to use a splitter, or an attenuator to reduce the input power level to the OSA. The OSA optical attenuator should be set to “ON” when the input power is more than 7 dBm.

Anritsu ``OSA`` API
*****************************

.. automodule:: osa
   :members:
   :undoc-members:
   :show-inheritance:

Usage
*****************************

.. Note::

  This section is still under construction. 
