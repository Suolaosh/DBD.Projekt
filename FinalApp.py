#!/usr/bin/env python

from time import sleep
from SX127x.LoRa import *
from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config import BOARD
import httpfuncs

BOARD.setup()

parser = LoRaArgumentParser("Continous LoRa Gateway.")
# global sending
sending = 0

class FinalApp(LoRa):
    tx_counter = 0
    sbcommend = 0
    bjcommend = 0
    lastcommend = []
    commend = []
    def __init__(self, verbose=False):
        super(FinalApp, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        # self.set_dio_mapping([0] * 6)

    def on_rx_done(self):
        print("\nRxDone")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        print("bytesmessage:")
        print(bytes(payload).decode("utf-8", 'ignore'))
        # header=[]
        # for b in payload[0:4]:
        #     header.append(int(b,16))
        # print header
        if payload[0] == 187 and payload[1] == 254:
            if payload[4] == 0x30:     # data
                print(payload)
                mes = []
                for i in payload[5:]:
                    mes.append(chr(i))
                print mes
                temp = mes[0] + mes[1]
                hum = mes[2] + mes[3]
                intens = mes[4] + mes[5] + mes[6]
                # print httpfuncs.sendtemp(hum,temp,intens)
                print temp
                print hum
                print intens
            elif payload[4] == 0x31:
                # httpfuncs.sendstate(self.commend[0],self.commend[1])
                cmd=[]
                for i in payload[5:]:
                    cmd.append(chr(i))
                print cmd
                print "fuck"
                # self.commend = []
        else:
            print "\nmessage not for me"



        # print(int.from_bytes(payload, byteorder='little'))
        # print(chr(int.from_bytes(b'\xf3\x25', byteorder='little')))
        # .decode("utf-8", 'ignore')
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_tx_done(self):
        print("\nTxDone")
        print "irq"+self.get_irq_flags()

    def start(self):
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        global args
        while True:
            sleep(5)
            # self.set_dio_mapping([0] * 6)
            # if(commend<>lastcommend)
            self.commend = httpfuncs.getcommend()
            self.lastcommend = self.commend
            self.sbcommend = self.commend[0]
            self.bjcommend = self.commend[1]
            # print "type of commend:"
            # print type(self.commend)
            # print "commend:"
            # print self.commend
            # self.set_mode(MODE.STDBY)
            # self.clear_irq_flags(TxDone=1)
            # sys.stdout.flush()
            # self.tx_counter += 1
            # sys.stdout.write("\rtx #%d\n" % self.tx_counter)

            payload = [0xfe, 0xbb, self.tx_counter, 9,0x31]
            self.set_mode(MODE.STDBY)
            self.clear_irq_flags(TxDone=1)
            sys.stdout.flush()
            self.tx_counter += 1
            sys.stdout.write("\rtx #%d\n" % self.tx_counter)
            payload.extend(self.commend)
            self.write_payload(payload)
            print "txcommend:"
            print payload
            self.set_mode(MODE.TX)
            self.set_mode(MODE.SLEEP)
            self.reset_ptr_rx()
            self.set_mode(MODE.RXCONT)
            # if self.lastcommend != self.commend:
            #     self.set_mode(MODE.STDBY)
            #     self.clear_irq_flags(TxDone=1)
            #     sys.stdout.flush()
            #     self.tx_counter += 1
            #     sys.stdout.write("\rtx #%d\n" % self.tx_counter)
            #     payload.extend(self.commend)
            #     self.write_payload(payload)
            #     print "txcommend:"
            #     print payload
            #     self.set_mode(MODE.TX)

            # rssi_value = self.get_rssi_value()
            # status = self.get_modem_status()
            # sys.stdout.flush()
            # sys.stdout.write("\r%d %d %d" % (rssi_value, status['rx_ongoing'], status['modem_clear']))


lora = FinalApp(verbose=False)
args = parser.parse_args(lora)

lora.set_mode(MODE.STDBY)
lora.set_pa_config(pa_select=1)
lora.set_freq(433.5)

print(lora)
assert(lora.get_agc_auto_on() == 1)

try: input("Press enter to start...")
except: pass

try:
    lora.start()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    # sys.stdout.flush()
    print("")
    lora.set_mode(MODE.SLEEP)
    print("lora")
    print(lora)
    BOARD.teardown()
