#!/usr/bin/env python
# encoding=utf-8

from time import sleep
from SX127x.LoRa import *
from SX127x.LoRaArgumentParser import LoRaArgumentParser
from SX127x.board_config import BOARD

BOARD.setup()

parser = LoRaArgumentParser("Continous LoRa receiver.")


class LoRaRcvCont(LoRa):
    tx_counter = 0
    sbcommend = 0
    bjcommend = 1
    def __init__(self, verbose=False):
        super(LoRaRcvCont, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        self.set_dio_mapping([0] * 6)
        # self.set_freq(433.5)

    def on_rx_done(self):
        BOARD.led_on()
        print("\nRxDone")
        self.clear_irq_flags(RxDone=1)
        payload = self.read_payload(nocheck=True)
        print("bytesmessage:")
        print(bytes(payload).decode("utf-8", 'ignore'))
        print(payload)
        message = []
        for i in payload[4:13]:
            message.append(chr(i))
        print message
        temp = message[0] + message[1]
        hum = message[3] + message[4]
        intens = message[6] + message[7] + message[8]
        print temp
        print hum
        print intens

        # print(int.from_bytes(payload, byteorder='little'))
        # print(chr(int.from_bytes(b'\xf3\x25', byteorder='little')))
        # .decode("utf-8", 'ignore')
        self.set_mode(MODE.SLEEP)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)

    def on_tx_done(self):
        print("\nTxDone")
        print(self.get_irq_flags())
        # global args
        # self.set_mode(MODE.STDBY)
        # self.clear_irq_flags(TxDone=1)
        # sys.stdout.flush()
        # self.tx_counter += 1
        # sys.stdout.write("\rtx #%d" % self.tx_counter)
        # if args.single:
        #     print
        #     sys.exit(0)
        # BOARD.led_off()
        # sleep(args.wait)
        # self.write_payload([0x0f])
        # BOARD.led_on()
        # self.set_mode(MODE.TX)

    def start(self):
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        # global args
        while True:
            sleep(1)
            self.set_mode(MODE.STDBY)
            self.clear_irq_flags(TxDone=1)
            sys.stdout.flush()
            self.tx_counter += 1
            sys.stdout.write("\rtx #%d" % self.tx_counter)
            # if args.single:
            #     print
            #     sys.exit(0)
            # BOARD.led_off()
            sleep(1)

            # self.write_payload([0xfe, 0xbb, self.tx_counter, 0x39, self.sbcommend, self.bjcommend])
            self.write_payload([0x30, 0x31, 0x32, 0x33])
            # BOARD.led_on()
            self.set_mode(MODE.TX)
            sleep(2)
            self.set_mode(MODE.RXCONT)
        #     rssi_value = self.get_rssi_value()
        #     status = self.get_modem_status()
        #     sys.stdout.flush()
        #     sys.stdout.write("\r%d %d %d" % (rssi_value, status['rx_ongoing'], status['modem_clear']))


lorarx = LoRaRcvCont(verbose=False)
args = parser.parse_args(lorarx)

lorarx.set_mode(MODE.STDBY)
lorarx.set_pa_config(pa_select=1)
lorarx.set_freq(433.5)
#lora.set_rx_crc(True)
#lora.set_coding_rate(CODING_RATE.CR4_6)
#lora.set_pa_config(max_power=0, output_power=0)
#lora.set_lna_gain(GAIN.G1)
#lora.set_implicit_header_mode(False)
#lora.set_low_data_rate_optim(True)
#lora.set_pa_ramp(PA_RAMP.RAMP_50_us)
#lora.set_agc_auto_on(True)

print(lorarx)
assert(lorarx.get_agc_auto_on() == 1)

try: input("Press enter to start...")
except: pass

try:
    lorarx.start()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    print("")
    lorarx.set_mode(MODE.SLEEP)
    print("lorarx")
    print(lorarx)
    BOARD.teardown()
