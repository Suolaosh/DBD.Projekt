#!/usr/bin/env python

from time import sleep
from SX127x.LoRa import *
from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config import BOARD

BOARD.setup()

parser = LoRaArgumentParser("Continous LoRa Gateway.")
# global sending
sending = 0
class FinalApp(LoRa):
    tx_counter = 0
    sbcommend = 0
    bjcommend = 1
    def __init__(self, verbose=False):
        super(FinalApp, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        # self.set_dio_mapping([0] * 6)

    def on_rx_done(self):
        if (sending == 0):
            print("\nRxDone")
            self.clear_irq_flags(RxDone=1)
            payload = self.read_payload(nocheck=True)
            print("bytesmessage:")
            print(bytes(payload).decode("utf-8", 'ignore'))
            print(payload)
            mes=[]
            for i in payload[4:13]:
                mes.append(chr(i))
            print mes
            temp = mes[0] + mes[1]
            hum = mes[3] + mes[4]
            intens = mes[6] + mes[7] + mes[8]
            print temp
            print hum
            print intens

        else:
            return 0


        # print(int.from_bytes(payload, byteorder='little'))
        # print(chr(int.from_bytes(b'\xf3\x25', byteorder='little')))
        # .decode("utf-8", 'ignore')
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_tx_done(self):
        global args
        print "fuck"
        commend = [self.sbcommend, self.bjcommend]
        self.send_message(commend)
        print(commend)
            # commend = [self.sbcommend, self.bjcommend]
            # if (self.tx_counter % 5 == 0):
            #     self.send_message(commend)
            # self.send_
            #
            # self.set_mode(MODE.STDBY)
            # self.clear_irq_flags(TxDone=1)
            # sys.stdout.flush()
            # if (1):
            #     self.tx_counter += 1
            #     sys.stdout.write("\rtx #%d" % self.tx_counter)
            #
            # if args.single:
            #     print
            #     sys.exit(0)
            # # BOARD.led_off()
            # sleep(args.wait)
            #
            # self.write_payload([0xfe, 0xbb, self.tx_counter, 0x39, self.sbcommend, self.bjcommend])
            # BOARD.led_on()
            # self.set_mode(MODE.TX)
            # if self.get_irq_flags().tx_done:
            #     self.set_mode(MODE.RXCONT)

    def send_message(self,massage):
        global args
        global sending
        sending = 1
        self.set_mode(MODE.SLEEP)
        self.clear_irq_flags(TxDone=1)
        sys.stdout.flush()
        self.tx_counter += 1
        sys.stdout.write("\rtx #%d" % self.tx_counter)
        if args.single:
            print
            sys.exit(0)
        sleep(args.wait)
        # header = [0xfe, 0xbb]
        # self.write_payload(header+massage)
        # self.set_mode(MODE.TX)
        # if self.get_irq_flags().tx_done:
        #     self.set_mode(MODE.RXCONT)
        #     sending = 0

        self.write_payload([0xfe, 0xbb, self.tx_counter, 0x39, self.sbcommend, self.bjcommend])
        self.set_mode(MODE.TX)

    def start(self):
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        while True:
            sleep(.5)
            # self.set_dio_mapping([0] * 6)
            # if(commend<>lastcommend)

            self.set_mode(MODE.SLEEP)
            self.set_dio_mapping([1, 0, 0, 0, 0, 0])
            # commend = [self.sbcommend, self.bjcommend]
            # self.send_message(commend)
            # print(commend)
            rssi_value = self.get_rssi_value()
            status = self.get_modem_status()
            sys.stdout.flush()
            sys.stdout.write("\r%d %d %d" % (rssi_value, status['rx_ongoing'], status['modem_clear']))

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
    sys.stdout.flush()
    print("")
    lora.set_mode(MODE.SLEEP)
    print("lora")
    print(lora)
    BOARD.teardown()
