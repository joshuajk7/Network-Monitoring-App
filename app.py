from network_monitoring_examples import *
import datetime


def check_server_status(server_protocol: str, server_params, frequency=2, show_time=False):
    """
    Allows user to set the frequency or interval of checks for each service.
    Configure a list of servers (IP addresses or domain names) and services 
    they want to monitor (HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP).
 
    Parameters:
            server_protocol: e.g. http, https, icmp, dns, ntp, tcp, udp

            server_params / args for each protocol:
                http: 
                    :param url: URL of the server (including http://)
                    :return (tuple):(True/False, status code)
                        True if server is up (status code < 400), False otherwise

                https:
                    :param url (str): URL of the server (including https://)
                    :param timeout (str): Timeout for the request in seconds. Default is 5 seconds.
                    :return (tuple):(True/False for server status, status code, description) 

                ping:
                    :param host (str): The IP address or hostname of the target host.
                    :param ttl (int): Time-To-Live for the ICMP packet. Determines how many hops (routers) the packet can pass through.
                    :param timeout (int): The time in seconds that the function will wait for a reply before giving up.
                    :param sequence_number (int): The sequence number for the ICMP packet. Useful for matching requests with replies.
                    :return (tuple): A tuple containing the address of the replier and the total ping time in milliseconds.
                        If the request times out, the function returns None for the ping time. The address part of the tuple is also None if no reply is received.\
                        
                traceroute:
                    :param host (str): The IP address or hostname of the target host.
                    :param max_hops (int): Maximum number of hops to try before stopping.
                    :param pings_per_hop (int): Number of pings to perform at each hop.
                    :param verbose (bool): If True, print additional details during execution.
                    :return (str): The results of the traceroute, including statistics for each hop.

                dns:
                    :param server (str): DNS server name or IP address
                    :param query (str): Domain name to query
                    :param record_type: Type of DNS record (e.g., 'A', 'AAAA', 'MX', 'CNAME')
                    :return: Tuple (status, query_results)

                ntp:
                    :param server (str): The hostname or IP address of the NTP server to check. 
                    :return (tuple): A tuple containing a boolean indicating the server status
                        (True if up, False if down) and the current time as a string
                        if the server is up, or None if it's down.
                
                tcp:
                    :param ip_address (str): The IP address of the target server.
                    :param port (int): The TCP port number to check.
                    :return (tuple): A tuple containing a boolean and a string.
                        The boolean is True if the port is open, False otherwise.
                        The string provides a description of the port status.
                
                udp:
                    :param ip_address (str): The IP address of the target server.
                    :param port (int): The UDP port number to check.
                    :param timeout (int): The timeout duration in seconds for the socket operation. Default is 3 seconds.
                    :return (tuple): A tuple containing a boolean and a string.
                        The boolean is True if the port is open (or if the status is uncertain), False if the port is definitely closed.
                        The string provides a description of the port status.

            frequency (int): Cofigured time interval set between status upates of servers. 

            show_time (bool): Shows date/time of server status if True (year-month-day hour:minute:second:milisecond).
    """

    start = input("CTRL + C to stop the application. Type enter to start.\n")
    try:
        while True:     
            if server_protocol == "http":
                if show_time == True:
                    print(datetime.datetime.now())
                print(check_server_http(server_params))
            elif server_protocol == "https":
                if show_time == True:
                    print(datetime.datetime.now())
                print(check_server_http(server_params))
            elif server_protocol == "ping":
                if show_time == True:
                    print(datetime.datetime.now())
                print(ping(server_params))
            elif server_protocol == "traceroute":
                if show_time == True:
                    print(datetime.datetime.now())
                print(traceroute(server_params))
            elif server_protocol == "dns":
                if show_time == True:
                    print(datetime.datetime.now())
                print(check_dns_server_status(server_params[0], server_params[1], server_params[2],))
            elif server_protocol == "ntp":
                print(check_ntp_server(server_params))
            elif server_protocol == "tcp":
                if show_time == True:
                    print(datetime.datetime.now())
                print(check_tcp_port(server_params[0], server_params[1]))
            elif server_protocol == "udp":
                if show_time == True:
                    print(datetime.datetime.now())
                print(check_udp_port(server_params[0], server_params[1]))

            time.sleep(frequency)

    except:
        KeyboardInterrupt    


def check_echo_server(echo_address="127.0.0.1", frequency=2, show_time=False):
    """Tests echo server with general ping network monitoring function. Default parameter set to local host IP (127.0.0.1)."""

    start = input("CTRL + C to stop the application. Type any key to Confirm.\n")
    try:
        while True:
            if show_time == True:
                print(datetime.datetime.now())
            print(ping(echo_address))
            time.sleep(2)
    except:
        KeyboardInterrupt


# Server Tests (HTTP, HTTPS, ICMP, DNS, NTP, TCP, UDP)
# print(check_server_status("http", "http://example.com"))
# print(check_server_status("https", "https://example.com"))        
# print(check_server_status("ping", "8.8.8.8"))
# print(check_server_status("traceroute", "8.8.8.8"))        
# print(check_server_status("dns", ("8.8.8.8", 'google.com', 'A')))
# print(check_server_status('ntp', 'pool.ntp.org'))
# print(check_server_status('tcp', ("google.com", 80)))
# print(check_server_status('udp', ("8.8.8.8", 53)))        
# print(check_echo_server())        
