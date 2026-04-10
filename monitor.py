from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time

log = core.getLogger()


class Monitor(object):
    def __init__(self, connection):
        self.connection = connection
        self.mac_to_port = {}

        self.total_packets = 0
        self.total_bytes = 0

        self.packet_counter = 0

        connection.addListeners(self)

        # request stats frequently
        Timer(5, self.request_stats, recurring=True)

        # print every 1 minute
        Timer(60, self.print_report, recurring=True)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        in_port = event.port

        if not packet.parsed:
            return

        self.packet_counter += 1

        log.info("Packet #%s: %s -> %s",
                 self.packet_counter, packet.src, packet.dst)

        self.mac_to_port[packet.src] = in_port

        out_port = of.OFPP_FLOOD

        if packet.dst in self.mac_to_port:
            out_port = self.mac_to_port[packet.dst]

            flow_mod = of.ofp_flow_mod()
            flow_mod.match.dl_dst = packet.dst
            flow_mod.actions.append(of.ofp_action_output(port=out_port))
            self.connection.send(flow_mod)

        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=out_port))
        self.connection.send(msg)

    def request_stats(self):
        self.connection.send(of.ofp_stats_request(
            body=of.ofp_flow_stats_request()))

    def _handle_FlowStatsReceived(self, event):
        total_packets = 0
        total_bytes = 0

        for stat in event.stats:
            total_packets += stat.packet_count
            total_bytes += stat.byte_count

        # update latest values
        self.total_packets = total_packets
        self.total_bytes = total_bytes

    # print every 1 minute
    def print_report(self):
        log.info("===== PERIODIC REPORT @ %s =====",
                 time.strftime("%H:%M:%S"))

        log.info("TOTAL PACKETS: %s", self.total_packets)
        log.info("TOTAL BYTES: %s", self.total_bytes)

        log.info("===================================")


def launch():
    def start_switch(event):
        log.info("Monitoring started on switch %s", event.connection)
        Monitor(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
