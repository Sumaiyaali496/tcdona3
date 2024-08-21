Polatis
===========================

The `Polatis` class is designed to interact with the Polatis optical switch, providing methods to apply patch lists, print patch tables, and save patch table information in a CSV format.

Class Overview
--------------

.. code-block:: python

   class Polatis:
       """
       A class to interface with a Polatis optical switch.
       
       Methods:
           login(): 
               Logs into the Polatis switch.
               
           apply_patch_list(patch_list): 
               Applies a list of patches to the switch.
               
           print_patch_table(patch_list, csv=False): 
               Prints or returns the patch table based on the patch list.
               
           get_patch_table_csv(patch_list, filename): 
               Saves the patch table as a CSV file.
       """

Method: `login`
---------------

.. code-block:: python

   def login(self):
       """
       Logs into the Polatis optical switch.

       This method handles the authentication process to access the Polatis switch.
       It should be called before any other operations are performed.

       Returns:
           None
       """

**Usage Example:**

.. code-block:: python

   pol = Polatis()
   pol.login()

Method: `apply_patch_list`
--------------------------

.. code-block:: python

   def apply_patch_list(self, patch_list):
       """
       Applies a list of patches to the Polatis switch.

       Args:
           patch_list (list): A list of tuples representing the patches to be applied. 
                              Each tuple should contain two strings, where the first 
                              string represents the input component and the second 
                              string represents the output component.

       Raises:
           Exception: If one or more components are in use by another user.
           Exception: If some (or all) ports are not available in the patch_list.

       Returns:
           None
       """

**Usage Example:**

.. code-block:: python

   patch_list = [('comp1', 'comp2'), ('comp2', 'comp3')]
   pol.apply_patch_list(patch_list)

In case the ports are being shown to be used by another user and you require it, please contact the admin.

Method: `print_patch_table`
---------------------------

.. code-block:: python

   def print_patch_table(self, patch_list, csv=False):
       """
       Prints a patch table based on the given patch list.

       Args:
           patch_list (list): A list of tuples representing the patches.
               Each tuple should contain two elements: the input patch and the output patch.
           csv (bool, optional): If True, returns the patch table as a CSV string.
               Defaults to False.

       Returns:
           None or str: If csv is True, returns the patch table as a CSV string.
               Otherwise, prints the patch table and returns None.

       Raises:
           Exception: If patch_list is not a list or if it is empty.
       """

**Usage Example:**

.. code-block:: python

   pol.print_patch_table(patch_list)

To print the patch table as a CSV string:

.. code-block:: python

   csv_string = pol.print_patch_table(patch_list, csv=True)

Method: `get_patch_table_csv`
-----------------------------

.. code-block:: python

   def get_patch_table_csv(self, patch_list, filename):
       """
       Generates a CSV file containing the patch table based on the given patch list.

       Args:
           patch_list (list): A list of patches.
           filename (str): The name of the CSV file to be generated.

       Returns:
           None
       """

**Usage Example:**

.. code-block:: python

   filename = 'patch_table.csv'
   pol.get_patch_table_csv(patch_list, filename)

Usage Example
-------------

.. code-block:: python

   from tcdona2.polatis import Polatis

   # Initialize and login
   pol = Polatis()
   pol.login()

   # Define a list of patches
   patch_list = [('comp1', 'comp2'), ('comp2', 'comp3')]

   # Apply the patch list to the switch
   pol.apply_patch_list(patch_list)

   # Print the patch table
   pol.print_patch_table(patch_list)

   # Save the patch table to a CSV file
   pol.get_patch_table_csv(patch_list, 'patch_table.csv')
