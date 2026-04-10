# SDN Traffic Monitoring and Statistics Collector

## Objective
Build a controller module to monitor network traffic, collect statistics, and display packet/byte counts.

## Tools Used
- Mininet
- POX Controller
- OpenFlow Protocol
- Ubuntu (Virtual Machine)

## Project Features
- Packet-level logging (Packet #1, Packet #2, ...)
- Periodic traffic statistics (packet count and byte count)
- Flow table inspection
- Connectivity testing using ping
- Bandwidth testing using iperf

## Network Topology
Single switch with 3 hosts:

h1 ---\
       \
h2 ---- s1 ---- Controller
       /
h3 ---/

---

## Step-by-Step Execution

### 1. Create the Controller File

Open terminal and run:
cd ~/pox
nano monitor.py


Paste the controller code into the file.

Save the file:
- Press CTRL + X, then Y
- Press ENTER

---

### 2. Start POX Controller
   cd ~/pox
   ./pox.py openflow.of_01 forwarding.l2_learning monitor
---
### 3. Start Mininet:
   Open a new terminal and run:
   sudo mn -c
   sudo mn --topo single,3 --controller=remote,ip=127.0.0.1
---

### 4. Test Network Connectivity 
   pingall
---

### 5. Ping Test
   h1 ping -c 5 h2
---

### 6. Bandwidth Test
   iperf h1 h2

---

### 7. View Flow Table

   open new terminal
   Then run:
      sudo ovs-ofctl dump-flows s1
---

## Explanation

- The controller logs only initial packets (PacketIn events)
- After learning, the switch handles traffic directly
- Flow statistics include all packets handled by the switch
- Packet logs represent control-plane activity
- Statistics represent full data-plane traffic

---

## Conclusion

The project successfully implements an SDN-based traffic monitoring system that:
- Collects traffic statistics
- Displays packet and byte counts
- Performs periodic monitoring
- Generates simple reports

---

## Repository Contents

- monitor.py → Controller code  
- Screenshots → Execution proof  
