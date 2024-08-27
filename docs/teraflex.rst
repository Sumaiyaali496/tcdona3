Teraflex
===============

The ``TFlex`` Class

Class to interact with the Teraflex device using NETCONF protocol

You would not be able to initialize this class unless you have been allocated as the patch owners for the Teraflex device, or the device is not being used. 

Usually, you should only use the following methods:

- :meth:`teraflex.TFlex.change_configuration`

- :meth:`teraflex.TFlex.read_pm_data`

- :meth:`teraflex.TFlex.set_power_and_frequency`

You can also use all the read-only methods such as :meth:`teraflex.TFlex.get_interface`, :meth:`teraflex.TFlex.get_symbolrate`, :meth:`teraflex.TFlex.get_filterrolloff`, :meth:`teraflex.TFlex.get_fec_algorithm`, :meth:`teraflex.TFlex.get_power_and_frequency`, :meth:`teraflex.TFlex.get_interface_modulation`. 

For the other methods, currently we have 4 line ports available: [1/1/n1, 1/1/n2, 1/2/n1, 1/2/n2]. This denotes shelf/rack/port. 

.. Caution::
Other specific configuration changing methods should be dealt with caution. Unless you have highly specific configuration requirements, refrain from using other options. Use the :meth:`teraflex.TFlex.change_configuration` method instead.

*****************************

.. automodule:: teraflex
   :members:
   :undoc-members:
   :show-inheritance:
