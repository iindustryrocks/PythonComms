import pigpio
import time

pi = None
slave_addr = None
int_handler = None
remote_message_handler = None


def i2c_interrupt(id, tick):
   global pi
   global slave_addr

   status, bytes_read, data = pi.bsc_i2c(slave_addr)

   if bytes_read:
        remote_message_handler(data)


def disconnect():
    global pi
    global int_handler
    int_handler.cancel()
    pi.bsc_i2c(0)
    pi.stop()

def default_message_handler(message):
    print(message)


def connect(slave_addr=0x04, message_handler=default_message_handler, keep_alive=False, keep_alive_time=500):
    global pi
    global int_handler
    global remote_message_handler

    pi = pigpio.pi()
    remote_message_handler=message_handler
    int_handler = pi.event_callback(pigpio.EVENT_BSC, i2c_interrupt)
    pi.bsc_i2c(slave_addr)
    print("Listening")
    if not keep_alive:
        time.sleep(keep_alive_time)
        disconnect()
