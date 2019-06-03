import pigpio
import time

pi = None
slave_addr = None
int_handler = None
message_handler = None



def i2c_request_handler_example(id, tick):
    global pi
    global slave_addr
    global message_handler
    status, bytes_read, data = pi.bsc_i2c(slave_addr)  # pi.bsc_i2c(slave_addr, data=" ACK")
    if bytes_read:
        message_handler(data)


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

    pi = pigpio.pi()  # inicia a conexao
    message_handler=message_handler()
    int_handler = pi.event_callback(pigpio.EVENT_BSC, i2c_request_handler_example)
    pi.bsc_i2c(slave_addr)
    if not keep_alive:
        time.sleep(keep_alive_time)
        disconnect()
