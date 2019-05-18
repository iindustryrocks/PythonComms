import pigpio
import time
import os

print("Listening...")

pi = None
slave_addr = None
int_handler = None


def i2c_request_handler_example(id, tick):
    global pi
    global slave_addr
    status, bytes_read, data = pi.bsc_i2c(slave_addr)  # pi.bsc_i2c(slave_addr, data=" ACK")
    if bytes_read:
        for byte in data:
            print(byte)


def disconnect():
    global pi
    global int_handler
    int_handler.cancel()
    pi.bsc_i2c(0)
    pi.stop()


def connect(slave_addr=0x04, i2c_request_handler=i2c_request_handler_example, keep_alive=False, keep_alive_time=500):
    global pi
    global int_handler

    pi = pigpio.pi()  # inicia a conexao
    int_handler = pi.event_callback(pigpio.EVENT_BSC, i2c_request_handler)
    pi.bsc_i2c(slave_addr)
    if not keep_alive:
        time.sleep(keep_alive_time)
        disconnect()
