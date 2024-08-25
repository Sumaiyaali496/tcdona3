import mysql.connector
import os

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