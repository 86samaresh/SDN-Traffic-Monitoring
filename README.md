# SDN Traffic Monitoring and Statistics Collector

## Objective
Build a controller module to monitor network traffic, collect statistics, and display packet/byte counts.

## Tools Used
- Mininet
- POX Controller
- OpenFlow

## Features
- Packet-level logging
- Periodic traffic statistics (packet/byte count)
- Flow table inspection
- Ping and bandwidth testing

## Steps to Run

1. Start POX:
   ./pox.py openflow.of_01 forwarding.l2_learning monitor

2. Start Mininet:
   sudo mn --topo single,3 --controller=remote,ip=127.0.0.1

3. Test:
   pingall  
   h1 ping -c 5 h2  
   iperf h1 h2  

4. Flow table:
   sudo ovs-ofctl dump-flows s1

## Output
- Packet logs  
- Periodic reports  
- Successful connectivity  
- Bandwidth results  

## Conclusion
The system successfully monitors traffic and generates statistics.