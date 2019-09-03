from main import ti
from time import sleep


@ti()
def delay_ms(val):
    sleep(val / 1e3)


delay_ms(50)
