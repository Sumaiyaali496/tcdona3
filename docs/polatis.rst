Polatis Optical Switch
============================

Capabilities
*****************************

Polatis is a high-capacity, reliable all-optical matrix switch designed for fast switching of optical signals, supporting up to 320x320 ports. It is used in the lab to route optical signals between different components. Optical fibers are connected to the input and output ports, with the switch internally managing the optical paths based on external commands. Because most optical components are connected to the Polatis, there is no need to manually connect and disconnect components.

A connection between two devices in the Polatis is referred to as a patch. Each patch has an optical loss of approximately 1.5 dB, with a polarization-dependent loss of less than 0.1 dB. The maximum input power threshold is 20 dBm. 

The `Polatis` class is designed to interact with the Polatis optical switch using NETCONF, providing methods to apply patch lists, print patch tables, and save patch table information in a CSV format. The aggregate power of the power levels of the devices in the patch list are measured through the built-in Optical Power Monitors in the Polatis, with a resolution of +/-1.0 dBm. The power levels are measured in dBm.

Below is the data sheet for the Polatis switch:

.. list-table:: Polatis Datasheet
   :widths: 75 50
   :header-rows: 1

   * - **Performance Parameters**
     - **Specifications**
   * - Typical Insertion Loss
     - 1.5 dB
   * - Maximum Insertion Loss
     - 2.7 dB
   * - Loss Repeatibility
     - +/-0.1 dB
   * - Connection Stability
     - +/-0.1 dB
   * - Switching Time
     - 50 ms for a single connection
   * - Dark Fiber Switching
     - Yes
   * - Polarization Dependent Loss
     - <0.3dB (C+L Band)
   * - Crosstalk
     - >50 dB
   * - Operating Wavelength Range
     - 1260-1675 nm
   * - Data Latency through a Patch
     - <25 ns
   * - Optical Input Power Range
     - Dark to +20 dBm
   * - Optical Power Monitoring Resolution
     - +/- 1.0 dBm 

The patch list can be found `here <https://docs.google.com/spreadsheets/d/11gGlnunXhfdTFGhSzP-2jx-jE0ROisqUnhYTsxsmiMc/edit?usp=sharing>`_. 

.. Note::
   #. Before starting any experiment and patching devices, you must request for the equipments to be allocated to you for the time-frame of the experiment. This is necessary to avoid any conflicts with other users. Please go to :ref:`getting-started` for more information on how to request for equipment allocation.

   #. You would not be able to patch any components in the Polatis, or initialize any equipment unless they have been allocated to you, or not allocated to any other user. 

   #. The Polatis switch is a sensitive optical device. Please be cautious when using the methods in this module. The failsafe mechanism will not patch any components if the input power is greater than 20 dBm. 

``Polatis`` API
*****************************
.. autoclass:: polatis.Polatis
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: get_NE_type, get_all_atten, get_all_labels, get_all_patch, get_all_pmon, get_all_power, get_all_shutter, getall, logger, logout, report_all, test_all_power

Usage
*****************************
.. Polatis Class Documentation
.. ===========================

**Usage Example:**

.. code-block:: python

    from tcdona3.polatis import Polatis

    # Initialize and login
    pol = Polatis()
    pol.login()

    # Define a list of patches
    patch_list = [('device_1', 'device_2'), ('device_2', 'device_3')]

    # Apply the patch list to the switch
    pol.apply_patch_list(patch_list)

    # Print the power levels of the devices in the patch list
    pol.print_patch_table(patch_list)
    # Output: 
    # Device 1: Out: -10.0 dBm --> Device 2: In: -12.0 dBm
    # Device 2: Out: -12.0 dBm --> Device 3: In: -14.0 dBm

    # Save the power levels of the devices in the patch list to a CSV file
    pol.get_patch_table_csv(patch_list, 'patch_table.csv')

    # Disconnect the connection between two devices
    pol.disconnect_devices(device_1, device_2)

    # Disconnect all the connections in a patch list
    pol.disconnect_patch_list(patch_list)
