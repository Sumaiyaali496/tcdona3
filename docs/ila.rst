Juniper In-Line Amplifier (ILA)
=================================

Capabilities
*****************************

The Juniper TCX-1000 In-line Amplifier is a standalone Erbium-Doped Fiber Amplifier (EDFA) that supports dual optical in-line amplification — two functionally separate amplifiers. The TCX1000-ILA provides periodic optical amplification of a Dense Wavelength-Division Multiplexing (DWDM) signal to enable long-distance transmission as it propagates along the fiber-optic cable. 

The ILA dual EDFA amplification solution that provides optical gain for the optical signal traversing the amplifier in the A-B direction, and the signal traversing the amplifier in the opposite B-A direction. Thus, it can be viewed as two amplifiers in one box. The two amplifiers are totally separate (with the exception of the Optical Service Channel (OSC) and are referred to as amplifier AB and amplifier BA. Line A is serviced by the input to amplifier AB and the output of amplifier BA. Line B is serviced by the input to amplifier BA and the output of amplifier AB.

Since the TCX-1000 ILA is a commercial equipment and meant to be operated in a production environment, the API provides a limited set of functionalities to interact with the device. Additionally, the device has fail-safe mechanisms to keep a commercial nework running:

#. **Line Ports vs Direction**: The ILA operates in line-mode, and hence, it has two line ports, Line A and Line B. The Line A port is serviced by the input to amplifier AB and the output of amplifier BA. The Line B port is serviced by the input to amplifier BA and the output of amplifier AB. The direction of the signal is determined by the input and output ports. 

  .. list-table:: TCX1000-ILA Line Ports vs Direction
    :widths: 50 50 50
    :header-rows: 1

    * - **Amplifier**
      - **Physical Ports**
      - **Direction Served**
    * - AB
      - Line A In
      - A to B input
    * - AB
      - Line B Out
      - A to B output
    * - BA
      - Line B IN
      - B to A input
    * - BA
      - Line A Out
      - B to A output

  While patching in the Polatis, Let us consider a situation when you want to connect *fiber_1* to *ila_1*, and further the output of *ila_1* to *fiber_2*. In this case, *fiber_1* is connected to the Line A port of the ILA, and *fiber_2* is connected to the Line B port of the ILA.
  Counter intuitively, the polatis patch list would look like this:


  .. code-block:: python

    patch_list = [('fiber_1', 'ila_1_fwd'), ('ila_1_bck', 'fiber_2')]

  This is because the ILA operates in line-mode (directionally), instead of the traditional port-mode like ROADMs and other components. 


#. **Automatic Laser Shutdown (ALS)**: Automatic line shutoff is implemented on the Line Out ports of the TCX-1000 ILA, and identifies fiber breaks or
disconnects between two interconnected TCX1000 device Line Out ports. The ALS feature is enabled by default and is not configurable. In short, if there is no light detected on backward direction, the ILA will shut down the laser in both directions. The same goes for the forward direction.


#. **Automatic Power Reduction (APR)**: The TCX1000-ILA APR mechanism monitors the back-reflection ratio (OBR) of each line output port and uses it as a gauge. If the back-reflection ratio goes above -17 dB (indicative of a fiber cut) on either output port, and the total output power is higher than
19 dBm, the amplifier enters the APR mode. I this mode, the Line-out power output will be attenuated by 2 dB to bring the output to a safe level. The amplifier stays in APR state until the back-reflection ratio goes below -19 dB, at which point the target output signal power is restored and the APR alarm is cleared. APR engagement occurs in less than 40 ms after disconnection of either line port fiber. 


.. Caution::

   #. The ILA is a high-power optical device. The ILA is only meant to be used in a fiber-optical network between long optical fibers. It has the cpaacity to damage optical components, and the Polatis if connected directy. Do not connect ano other component (other than fibers) directly to the ILA.
   
   #. The TCX Series system functions in the 850 nm to 1620 nm wavelength window that is considered invisible radiation. Laser light being emitted by a fiber, a pigtail, or a bulkhead connector cannot be seen by the naked eye. Use appropriate eye protection.

   #. Please be cautious when using the methods in this module. The best parctice is to start with a small target gain setting and small input power, and then gradually ramping up the setting until you reach the desired power. 
   
``ILA`` API
*****************************

.. automodule:: tcdona3.ila
   :members:
   :undoc-members:
   :show-inheritance:

Usage
*****************************

This usage example demonstrates how to use the ILA API to interact with the ILA device. We create a simple topology, connecting an ILA between two fibers.

**Usage Example**

.. code-block:: python

   from tcdona3.ila import ILA
   from tcdona3.polatis import Polatis

   # Create an instance of the Polatis switch
   pol = Polatis()
   pol.login()

   # Create an instance of the ILA
   ila = ILA('ila_1')

   # Define a patch list
   patch_list = [
       ('fiber_1', 'ila_1_fwd'),
       ('ila_1_bck', 'fiber_2')
   ]

   # Apply the patch list to the Polatis
   pol.apply_patch_list(patch_list)

   # Configure the target gain of the ILA
   ila.set_target_gain(10)

   # Get the current gain of the ILA
   ila.get_current_gain()

   # Set the Amplifier state to to in-service
   ila.set_amp_state('ab', 'true')

   # Dump the PM data to a XML file
   with open('ila_pm.xml', 'w') as f:
       f.write(ila.get_pm_xml())