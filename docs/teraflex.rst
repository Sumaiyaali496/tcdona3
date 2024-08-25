Teraflex
===============

The ``TFlex`` Class

Class to interact with the Teraflex device using NETCONF protocol

You would not be able to initialize this class unless you have been allocated as the patch owners for the Teraflex device., or the device is not being used. 

Usually, you should only use the following methods:
- read_pm_data
- change_configuration
- return_current_config

You can also use all the read-only methods such as get_operational_state, get_interface, get_params, get_symbolrate, get_filterrolloff, get_fec_algorithm, get_power_and_frequency, get_interface_modulation, get_port_admin_state.

For the other methods, currently we have 4 line ports available: [1/1/n1, 1/1/n2, 1/2/n1, 1/2/n2]. This denotes shelf/rack/port. 

CAUTION: Other specific configuration changing methods should be dealt with caution. Unless you have highly specific configuration requirements, refrain from using other options. Use the change_configuration method instead.

*****************************

.. automodule:: teraflex
   :members:
   :undoc-members:
   :show-inheritance:
