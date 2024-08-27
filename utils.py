import mysql.connector
import os
import math

FIRST_CENTRAL_FREQ = 191350.0
CHANNEL_SPACING = 50.0
CHANNEL_WIDTH = 50.0
wdm_channel_list = list(range(1,96))

def check_patch_owners(patch_list):

    """Check if the ports in the patch list are available and are allocated to the running user.
    
    :param patch_list: A list of patches, where each patch is a list of ports.
    :type patch_list: list

    :return: True if all ports are available and allocated to the running user, False otherwise.
    :rtype: bool
    """


    # Get the Unix user behind sudo
    unix_user = os.getenv("SUDO_USER")
    if not unix_user:
        unix_user = os.getenv("USER")

    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="127.0.0.1", user="testbed", password="mypassword", database="provdb"
    )
    cursor = conn.cursor()

    nonexistent_ports = []
    other_owners = []

    for patch in patch_list:
        for port in patch:
            # Skip NULL connections
            if port == "NULL":
                continue

            # Check if the port exists and fetch the owner
            cursor.execute("SELECT Owner FROM ports_new WHERE Name = %s", (port,))
            result = cursor.fetchone()
            if not result:
                nonexistent_ports.append(port)
            else:
                #if len(owner) == 0:
                #    nonexistent_ports.append(port)
                owner=result[0]
                if len(owner)!=0 and unix_user not in owner.split(','):
                    other_owners.append(result)
    if (len(nonexistent_ports) > 0) or (len(other_owners) > 0):
        # Close the cursor and connection
        cursor.close()
        conn.close()

        if nonexistent_ports:
            print("Nonexistent ports:", nonexistent_ports)
        if other_owners:
            print("Ports with other owners:", other_owners)
        return False

    else:
        # # If all checks pass, update the owner of the ports to the Unix user
        # for connection in patch_list:
        #     for name in connection:
        #         if name == "NULL":
        #             continue
        #         cursor.execute(
        #             "UPDATE ports SET owner = %s WHERE Name = %s", (unix_user, name)
        #         )

        # # Commit the changes
        # conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()
        return True
    


def db_to_abs(db_value):
    """ Function to convert dB to absolute value

    :param db_value
    :type db_value: list or float

    :return: Absolute value in Watts
    """
    absolute_value = 10 ** (db_value / float(10))
    return absolute_value


def abs_to_db(absolute_value):

    """ Function to convert absolute value to dB 

    :param absolute_value
    :type absolute_value: list or float

    :return: dB value
    """
    db_value = 10 * math.log10(absolute_value)
    return db_value


def abs_to_dbm(absolute_value):
    """Function to convert absolute value to dBm

    :param absolute_value
    :type absolute_value: list or float

    :return: dBm value
    """
    dbm_value = 10 * math.log10(absolute_value / 1e-3)
    return dbm_value

def get_freq_range(channel_num):
    """Function to get the frequency range of a channel number according to the 95 x 50 GHz grid defined by ITU-T G.694.1

    :param channel_num: Channel number in the range [1,95]
    :type channel_num: int

    :return: Start frequency, central frequency, and end frequency of the channel in THz
    :rtype: tuple
    """

    central_freq = FIRST_CENTRAL_FREQ + (channel_num-1)*CHANNEL_SPACING
    start_freq = central_freq - CHANNEL_WIDTH/2.0
    end_freq = central_freq + CHANNEL_WIDTH/2.0

    return int(start_freq), int(central_freq), int(end_freq)

