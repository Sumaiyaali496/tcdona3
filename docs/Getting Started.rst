.. _getting-started:

Getting Started
#####################
This is a placeholder for the Getting Started guide.

From first contact to your first experiment on the Open Ireland Testbed, this guide will walk you through a 4-step process to help you get started.

#. **Generate SSH Keys**: Generate SSH keys to access the Open Ireland Testbed.
#. **Get Access to the Testbed**: Get access to the testbed from the Admin. 
#. **Equipment Allocation**: Understand how to reserve equipment for your experiments.
#. **Lab Rules and Safety**: Review the rules and safety guidelines for using the Open Ireland Testbed.
#. **Troubleshooting**: Find solutions to common issues you may encounter while using the Open Ireland Testbed.
#. **First Experiment**: Run your first experiment on the Open Ireland Testbed.

.. note::
    You will need a computer running Linux or MAC to access the Open Ireland Testbed. Although Windows is supported, it is recommended to use Linux or MAC, since there will not be much available support for Windows. The guide below assumes you are using Linux or MAC.

.. _ssh-key:

1. Generate SSH Keys
************************************************

Access to Open Ireland Testbed is granted through SSH Connection. SSH keys come in pairs: a **public key** that you can share with others and a **private key** that remains on your local machine. This guide will show you how to generate and retrieve your SSH key in Linux.

Generating SSH Keys
==========================================
If you haven't already generated an SSH key, you can easily create one using the following steps:

1. Open your terminal.
2. Run the following command to generate a new SSH key pair:

   .. code-block:: bash

       ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

   Here's what each part of the command means:
   - `-t rsa`: This specifies the type of key to generate. RSA is the most common algorithm used.
   - `-b 4096`: This defines the bit size for the key. A 4096-bit key is recommended for security.
   - `-C "your_email@example.com"`: This is an optional comment field, typically used to specify the email address for easier identification.

3. After running the command, you'll be prompted to choose a file location to save the key:

   .. code-block:: text

       Enter file in which to save the key (/home/your_username/.ssh/id_rsa):

   Press **Enter** to accept the default location (`/home/your_username/.ssh/id_rsa`), or specify a custom path if you prefer.

4. Next, you'll be asked to provide a passphrase. This is optional but highly recommended to add an extra layer of security. If you don’t want to use a passphrase, press **Enter** to leave it empty.

   .. code-block:: text

       Enter passphrase (empty for no passphrase):
       Enter same passphrase again:

After successfully completing these steps, your SSH key pair will be generated and saved on your local machine.

Retrieving Your SSH Key
=========================
Once you have generated the key pair, you'll want to retrieve your **public key** to share with a server or service. Here's how to find it:

1. Open your terminal.
2. Use the following command to display the contents of your public key:

   .. code-block:: bash

       cat ~/.ssh/id_rsa.pub

3. The command will print out your public key, which will look something like this:

   .. code-block:: text

       ssh-rsa AAAAB3Nza...rest_of_the_key... your_email@example.com

4. Copy the entire output from the terminal. This is the public key you'll need to provide when setting up SSH access with other services.

Note that your private key is located in the same directory as your public key (`~/.ssh/id_rsa` by default). This key should **never** be shared with anyone or uploaded to any service.

.. Caution::
    Do not share your private key with anyone. Keep it secure on your local machine to prevent unauthorized access to Open Ireland servers.

.. _get-access-testbed:

2. Get Access to the Testbed
**************************************************************

Once you have generated your SSH keys (see :ref:`ssh-key`), the next step is to request access to the Open Ireland Testbed. Access is typically granted by the administrator of the testbed. You need to send the following information to the administrator:

#. Your full name
#. The purpose of your access (e.g., research, experimentation, etc.)
#. Your public SSH key (see :ref:`ssh-key`)

.. _ssh-config-inclusion:

Using the SSH Configuration to Access the Testbed
=================================================

After you have been granted access to the Open Ireland Testbed, the administrator will send you the necessary SSH configuration details via email. These details are meant to simplify the process of connecting to the testbed by configuring your SSH settings. In this section, you'll learn how to manually add the provided SSH configuration to your Linux system and access the testbed.

Step-by-Step Guide to Adding SSH Config
-----------------------------------------

1. **Check the SSH Configuration Details in Your Email:**

   The administrator will send you an email containing the SSH configuration. It should look something like this:

   .. code-block:: text

       Host openireland-testbed
           HostName testbed.openireland.example.com
           User your_username
           IdentityFile ~/.ssh/id_rsa
           ProxyCommand ssh -W %h:%p jumpserver.example.com
           Port 22

   Explanation of each field:
   - **Host**: This defines an alias for the connection. In this case, `openireland-testbed` is used as a shortcut for connecting to the testbed.
   - **HostName**: The domain or IP address of the testbed server.
   - **User**: Your username on the testbed.
   - **IdentityFile**: The path to your private SSH key. Make sure this matches where your SSH key is located on your machine (usually `~/.ssh/id_rsa`).
   - **Port**: The SSH port number, typically `22` unless specified otherwise by the administrator.
    - **ProxyCommand**: If you need to connect through a jump server, this command specifies the proxy settings.

2. **Create or Edit Your SSH Config File:**

   If you don’t already have an SSH config file, you’ll need to create one. If the file already exists, you’ll append the new configuration to it. Here’s how to proceed:

   a. Open a terminal.
   
   b. Use a text editor (such as `nano` or `vim`) to create or edit the SSH config file:

   .. code-block:: bash

       nano ~/.ssh/config

   If the file doesn’t exist, this command will create it. Otherwise, it will open the existing file.

3. **Add the SSH Configuration Details:**

   Copy the configuration details from the email and paste them into the file. The final config file should look something like this:

   .. code-block:: text

       Host openireland-testbed
           HostName testbed.openireland.example.com
           User your_username
           IdentityFile ~/.ssh/id_rsa
           ProxyCommand ssh -W %h:%p jumpserver.example.com
           Port 22

   Ensure that the **IdentityFile** points to the correct path of your private key. If you saved your private key in a different location (not `~/.ssh/id_rsa`), update the path accordingly.

4. **Save and Close the File:**

   If you’re using `nano`, you can save the file by pressing `CTRL + O`, then `Enter`, and then exit by pressing `CTRL + X`. In `vim`, you can save and exit by typing `:wq` and pressing `Enter`.

5. **Set Correct Permissions:**

   SSH requires certain file permissions for security reasons. Make sure that your `.ssh` directory and the `config` file have the correct permissions:

   .. code-block:: bash

       chmod 700 ~/.ssh
       chmod 600 ~/.ssh/config

   This ensures that only your user account can read and modify these files.

Accessing the Testbed with SSH
--------------------------------

Once the configuration is in place, connecting to the Open Ireland Testbed is straightforward. You can use the following command to connect:

.. code-block:: bash

    ssh openireland-testbed

This command uses the alias (`openireland-testbed`) you configured in the SSH config file, and SSH will automatically:
- Use the appropriate domain or IP address (`HostName`).
- Authenticate you with the provided username (`User`) and SSH key (`IdentityFile`).

This eliminates the need to type out the full connection details every time you want to connect.

Testing Your Connection
--------------------------

After setting up your SSH config, you should test the connection to ensure everything is working:

1. Open a terminal.
2. Run the SSH command to connect to the testbed:

   .. code-block:: bash

       ssh openireland-testbed

3. If the connection is successful, you will see a login prompt or be directly logged into the testbed's shell environment.

4. If there are issues (e.g., "connection refused" or "permission denied"), check the following:
   - Ensure that your SSH key is correctly configured and added to the SSH agent (use `ssh-add ~/.ssh/id_rsa` to add your key).
   - Verify that the SSH config file is correctly placed in the `~/.ssh/` directory and that there are no typos in the details.
   - Make sure the file permissions are set correctly as shown above.

   If issues persist, double-check the information in the email sent by the administrator and contact them if necessary.

Best Practices for SSH Configuration
--------------------------------------

- **Backup Your Configurations**: Keep a backup of your SSH keys and the config file, especially if you are working from multiple machines.
- **Use Aliases for Other Servers**: If you frequently access multiple servers, adding aliases in your SSH config (like `openireland-testbed`) can save time and effort.
- **Update as Needed**: If the administrator provides updated connection details (e.g., a new server address), make sure to update your SSH config accordingly.

.. _equipment-allocation:

3. Equipment Allocation
*****************************


In order to perform experiments on the Open Ireland Testbed, users must first reserve the necessary equipment. This ensures that multiple experiments do not interfere with each other and allows for the smooth operation of the testbed. Users are required to request specific equipment and time slots in advance. This section explains how to reserve equipment, what information to provide, how to plan experiments in advance (especially around important deadlines), and how access is granted by the admin.

Why Equipment Allocation is Important
---------------------------------------

The equipment on the Open Ireland Testbed is shared among multiple users and institutions. To avoid conflicts and ensure efficient usage, the testbed employs an allocation system. **Users cannot access any equipment unless it has been specifically allocated to them.** This prevents multiple experiments from using the same instruments at the same time, which could lead to unreliable results or damage to the equipment.

Careful planning and proper equipment allocation are essential for smooth operation, and particularly important during high-demand periods such as leading up to conference submission deadlines or major research project milestones.

Planning Experiments Ahead of Time
------------------------------------

When planning experiments, it is important to think ahead, especially if your research results need to meet a specific deadline, such as:
- **Conference Submission Deadlines**
- **Project Milestones**
- **Funding Application Deadlines**

Experiments often take longer than expected due to equipment availability, troubleshooting, or unforeseen issues. Planning ahead allows you to account for these potential delays and ensures you have enough time to gather and analyze your results before submission deadlines.

### Key Considerations for Planning:

1. **Check Availability Early:**

   Testbed equipment can be in high demand, especially during busy periods like conference deadlines. To avoid scheduling conflicts, start planning your experiment well in advance. Check the availability of the equipment as soon as possible by contacting the admin or checking the testbed's equipment calendar (if available).

   For conference deadlines, it's best to begin planning at least **3-4 weeks** in advance. This buffer time will allow for:
   - **Equipment Reservation**: Ensuring you can secure the equipment for your specific time frame.
   - **Setup and Calibration**: Some equipment may require additional setup or calibration before it can be used in experiments.
   - **Troubleshooting**: If issues arise, you will have time to resolve them without impacting your deadline.

2. **Submit Equipment Requests Early:**

   During high-demand periods, equipment is often booked weeks in advance. Therefore, you should submit your equipment request as early as possible. Providing a flexible time frame for your experiments increases your chances of getting the equipment when you need it. When submitting your request, clearly indicate that your experiment is time-sensitive due to an upcoming deadline. 

3. **Avoid Over-Allocating Equipment:**

   When planning an experiment, it's important to accurately estimate the time you need to avoid over-allocating equipment. This helps other users and ensures efficient testbed operation. If you know the exact equipment setup time and duration of your experiment, include that information in your request. For example:
   - **Setup Time**: If your equipment requires a few hours for setup or calibration, include this in your reservation request.
   - **Experiment Duration**: Ensure that the equipment is only booked for the time it is actively in use.

   If your experiment involves several stages over an extended period, consider booking only the necessary time slots, freeing up the equipment between stages if it is not being used.

Requesting Equipment Allocation
---------------------------------

To request equipment for your experiments, follow these steps:

1. **Prepare Your Equipment Request:**

   Once you have determined what equipment you need, you must prepare a request to the testbed administrator. Your request should include the following information:

   - **List of Equipment**: Specify each piece of equipment you require for your experiment.
   - **Time Frame**: Clearly define the start and end date/time of your experiment. Make sure the time frame includes any setup or calibration you may need to perform.
   - **Purpose of the Experiment**: Provide a brief description of your experiment to help the admin understand the scope and needs of your reservation.
   - **Deadline Sensitivity**: If the experiment is time-sensitive (e.g., related to a conference or project deadline), make this clear in the request.

3. **Submit the Request to the Admin:**

   Send your request to the Admin, and ensure you submit your request **well in advance** of your desired start time, as the admin needs time to review and process the allocation.

4. **Wait for Confirmation:**

   The admin will review your request, check the availability of the equipment, and either approve or reject your reservation. You will receive a confirmation email if the equipment is available. The confirmation will include:
   - The equipment that has been allocated to you.
   - The duration for which the equipment is reserved.
   - Any specific instructions for accessing or using the equipment.

   If the equipment is not available, the admin may suggest alternative time slots or inform you about when the equipment will be available.

5. **Access to Equipment:**

   Once your reservation is confirmed, you will be granted access to the equipment during the allocated time. The equipment will be automatically locked for your use, ensuring that no other user can interfere with your experiment. Access to the equipment is controlled via your SSH connection to the testbed.

   You will not be able to use any equipment that has not been specifically allocated to you, or if it is currently allocated to another user. This prevents conflicts and ensures that experiments do not overlap or interfere with each other.

Best Practices for Equipment Allocation
-----------------------------------------

To ensure the smooth operation of the testbed and maximize your chances of getting the equipment you need, follow these best practices:

- **Plan Ahead**: Submit your equipment requests as early as possible, particularly during high-demand periods like conference deadlines.
- **Be Specific**: Clearly specify the equipment and time frame needed for your experiment. Vague or incomplete requests may delay the approval process.
- **Be Considerate of Other Users**: Only request equipment for the time you actually need it. Blocking equipment for extended periods when you don’t need it prevents others from using the testbed.
- **Communicate Deadline Sensitivity**: If you have a time-sensitive experiment due to conference submissions or project deadlines, make sure to communicate this in your equipment request.
- **Cancel Unused Reservations**: If your experiment is delayed or canceled, inform the admin as soon as possible so they can free up the equipment for other users.

Troubleshooting and Common Issues
-----------------------------------

Sometimes, issues may arise during the equipment reservation process. Here are a few common problems and how to resolve them:

- **Equipment Not Available**: If the equipment you need is already reserved, the admin will notify you. In this case, consider modifying your experiment schedule or asking if there is alternative equipment that could be used.
- **Overlapping Time Frames**: If another user’s reservation overlaps with yours, the admin may adjust your reservation or ask you to select a different time slot.
- **Technical Issues with Equipment**: If you encounter problems with the equipment after it has been allocated to you (e.g., calibration errors, connectivity issues), contact the testbed support team immediately for assistance.

Equipment Sharing and Off-hours Access
========================================

4. Lab Rules and Safety
*****************************



6. Troubleshooting
*****************************

7. First Experiment
*****************************