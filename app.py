from network_monitoring_examples import *
import datetime


def check_server_status():
    """
    Allows user to set the frequency or interval of checks for each service.
    Configure a list of servers (IP addresses or domain names) and services 
    they want to monitor (HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP).
    """

    servers = configure_servers()

    try:
        frequency = int(input("Enter the Frequency of status updates. Default set to 30: \n"))
        print(f"Frequency set to {frequency} seconds \n")
    except ValueError:
        frequency = 30
        print("Frequency set to 30 seconds")
    
    input(f"CTRL + C to stop the program. Press Enter to start")
    
    try:
        while True:
            for server in servers:
                if server == "":
                    return
                print(f"Showing status updates for {server}: ")
                for service in servers[server]:
                    if service[0] == "http":
                        print(f"    HTTP Status:")
                        print(f'    {check_server_http(f"{service[0]}://{server}")}')

                    elif service[0] == "https":
                        print(f"    HTTPS Status:")
                        print(f'    {check_server_https(f"{service[0]}://{server}", service[1])}')

                    elif service[0] == "icmp":
                        print(f"    ICMP Status:")
                        print(f'    {ping(service[1][0], service[1][1], service[1][2], service[1][3])}') 
                        
                    elif service[0] == "dns":
                        print(f"    DNS Status:")
                        print(f'    {check_dns_server_status(server, service[1][0], service[1][1])}')
                                
                    elif service[0] == "ntp":
                        print(f"    NTP Status:")
                        print(f'    {check_ntp_server(server)}')
                        
                    elif service[0] == "tcp":
                        print(f"    TCP Status:")
                        print(f'    {check_tcp_port(server, service[1])}')

                    elif service[0] == "udp":
                        print(f"    UDP Status:")
                        print(f'    {check_udp_port(server, service[1][0], service[1][1])}')
                print("")
            time.sleep(frequency)
    except:
        KeyboardInterrupt

def configure_servers():
    """
    Configure a list of servers (IP addresses or domain names) and services 
    they want to monitor (HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP)
    """

    servers = {}
    
    server="sd"
    while server != "":
        service_configs = [] # List of params for services for specified server. Default params left blank ("").
        if len(servers) == 0:
            server = input(f"Enter the Server Domain Name or IP Address: \n    ")
        if len(servers) != 0:
            server = input(f"Optional: Enter another Server Domain Name or IP Address. Or press Enter to continue: \n    ")
        if server == "":
            break
        
        service="sd"
        while service != "":
            if len(service_configs) == 0:
                service = input(f"    Enter the service-type to monitor status (e.g. HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP): \n    ")
            if len(service_configs) != 0:
                service = input(f"    Optional: Enter another service-type to monitor status (e.g. HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP). Or press Enter to continue: \n    ")

            if service == "http":
                """
                :param url: URL of the server (including http://)
                :return (tuple):(True/False, status code)
                True if server is up (status code < 400), False otherwise
                """
                service_configs.append((service,(None)))

            if service == "https":
                """
                :param url (str): URL of the server (including https://)
                :param timeout (str): Timeout for the request in seconds. Default is 5 seconds.
                :return (tuple):(True/False for server status, status code, description)                 
                """
                try:
                    timeout = int(input("    Enter the Timeout for the request in seconds. Press Enter to leave default (5 seconds).\n    "))
                except ValueError:
                    timeout = 5
                service_configs.append((service, (timeout)))

            if service == "icmp":
                """
                :param host (str): The IP address or hostname of the target host.
                :param ttl (int): Time-To-Live for the ICMP packet. Determines how many hops (routers) the packet can pass through.
                :param timeout (int): The time in seconds that the function will wait for a reply before giving up.
                :param sequence_number (int): The sequence number for the ICMP packet. Useful for matching requests with replies.
                :return (tuple): A tuple containing the address of the replier and the total ping time in milliseconds.
                    If the request times out, the function returns None for the ping time. The address part of the tuple is also None if no reply is received.
                """
                host = input("    Enter the IP Address or Hostname of the target host.\n    ")
                try:
                    ttl = int(input("    Time-To-Live for the ICMP packet. Enter how many hops (routers) the packet can pass through (Default 64).\n    "))
                except ValueError:
                    ttl = 64
                try:
                    timeout = int(input("    Enter the time in seconds that the function will wait for a reply before giving up (Default 1).\n    "))
                except:
                    timeout = 1
                try:
                    sequence_number = int(input("    Enter the sequence number for the ICMP packet. Useful for matching requests with replies (Default 1).\n    "))
                except:
                    sequence_number = 1
                service_configs.append((service, (host, ttl, timeout, sequence_number)))

            if service == "ntp":
                service_configs.append((service, (None)))

            if service == "dns":
                """
                :param server: DNS server name or IP address
                :param query: Domain name to query
                :param record_type: Type of DNS record (e.g., 'A', 'AAAA', 'MX', 'CNAME')
                :return: Tuple (status, query_results)
                """
                domain = input("    Enter the Domain name to query.\n    ")
                record_type = input("    Enter the Type of DNS record (e.g., 'A', 'AAAA', 'MX', 'CNAME').\n    ")         
                service_configs.append((service, (domain, record_type)))      

            if service == "tcp":
                """
                :param ip_address (str): The IP address of the target server.
                :param port (int): The TCP port number to check.
                :return (tuple): A tuple containing a boolean and a string.
                    The boolean is True if the port is open, False otherwise.
                    The string provides a description of the port status.
                """
                port = int(input("    Enter the The TCP port number to check.\n    "))
                service_configs.append((service, (port)))
            
            if service == "udp":
                """ 
                :param ip_address (str): The IP address of the target server.
                :param port (int): The UDP port number to check.
                :param timeout (int): The timeout duration in seconds for the socket operation. Default is 3 seconds.
                :return (tuple): A tuple containing a boolean and a string.
                    The boolean is True if the port is open (or if the status is uncertain), False if the port is definitely closed.
                    The string provides a description of the port status.
                """
                port = int(input("    Enter the The UDP port number to check.\n    "))
                try:
                    timeout = int(input("    Enter the timeout duration in seconds for the socket operation. (Default 3).\n    "))
                except ValueError:
                    timeout = 3
                service_configs.append((service, (port, timeout)))

            elif service == "":
                break
            print("    Service Configured.\n")
        servers[server] = service_configs
    return servers


def check_echo_server(echo_address="127.0.0.1", frequency=60, show_time=False):
    """Tests echo server with general ping network monitoring function. Default parameter set to local host IP (127.0.0.1)."""

    start = input("CTRL + C to stop the application. Type any key to Confirm.\n")
    try:
        while True:
            if show_time == True:
                print(datetime.datetime.now())
            print(ping(echo_address))
            time.sleep(frequency)
    except:
        KeyboardInterrupt


if __name__ == '__main__':
    check_server_status()
