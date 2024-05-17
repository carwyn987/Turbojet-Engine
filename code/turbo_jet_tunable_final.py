from tkinter import *
import threading
import time

# uncomment when I run irl
# import RPi.GPIO as GPIO

class UI(Frame):
    def __init__(self, parent):
       Frame.__init__(self, parent)
       self.parent = parent
       self.initialize_user_interface()

    def initialize_user_interface(self):
       # # Setup UI for spark frequency / s    
        self.spark_freq_label = Text(root, state='disabled', width=44, height=1)
        self.spark_freq_label.configure(state='normal')
        self.spark_freq_label.insert('end', 'Spark frequency per second')
        self.spark_freq_label.configure(state='disabled')
        self.spark_freq_label.pack()

        # Setup spark frequency / s slider
        self.spark_freq = Scale(root, from_=0.0, to=600.0, length=600, tickinterval=50, orient=HORIZONTAL, command=self.update_spark)
        self.spark_freq.pack()
        self.spark_freq.set(0)

        self.injector_freq_label = Text(root, state='disabled', width=44, height=1)
        self.injector_freq_label.configure(state='normal')
        self.injector_freq_label.insert('end', 'Injector frequency per second')
        self.injector_freq_label.configure(state='disabled')
        self.injector_freq_label.pack()

        # Setup injector frequency / s slider
        self.injector_freq = Scale(root, from_=0.0, to=100.0, length=600, tickinterval=10, orient=HORIZONTAL, command=self.update_injector_freq)
        self.injector_freq.pack()
        self.injector_freq.set(0)

        self.injector_dur_label = Text(root, state='disabled', width=44, height=1)
        self.injector_dur_label.configure(state='normal')
        self.injector_dur_label.insert('end', 'Injector duration per fire')
        self.injector_dur_label.configure(state='disabled')
        self.injector_dur_label.pack()

        # Setup spark frequency / s slider
        self.injector_dur = Scale(root, from_=0.0, to=1.0, digits = 3, resolution = 0.01, length=600,tickinterval=0.1, orient=HORIZONTAL, command=self.update_injector_dur)
        self.injector_dur.set(0.01)
        self.injector_dur.pack()

    def update_spark(self, b):
        global spark_frequency
        spark_frequency = self.spark_freq.get()
        print(spark_frequency)

    def update_injector_freq(self, b):
        global injector_frequency
        injector_frequency = self.injector_freq.get()
        print(injector_frequency)

    def update_injector_dur(self, b):
        global injector_duration
        injector_duration = self.injector_dur.get()
        print(injector_duration)

def setup(injector_pin, spark_pin):
    GPIO.setmode(GPIO.BCM)

    # Setup injector
    GPIO.setup(injector_pin, GPIO.OUT)

    # Setup spark
    GPIO.setup(spark_pin, GPIO.OUT)

def cleanup(injector_pin, spark_pin):
    GPIO.output(injector_pin, GPIO.LOW)
    GPIO.output(spark_pin, GPIO.LOW)
    GPIO.cleanup()

def spark_gpio_functions():
    global spark_frequency
    while True:
        # If exiting, stop the control thread:
        if stop_threads:
            break

        # Do stuff
        if spark_frequency != 0:
            time.sleep(1.0/spark_frequency)
            print("still running spark @ ", spark_frequency)

def injector_gpio_functions():
    global injector_frequency
    global injector_duration
    while True:
        # If exiting, stop the control thread:
        if stop_threads:
            break

        # Do stuff
        if injector_frequency != 0:
            time.sleep(1.0/injector_frequency)
            print("still running injector @ ", injector_frequency, " and duration ", injector_duration)

if __name__ == '__main__':

    # uncomment when I run irl
    # setup(injector_pin, spark_pin)
    global spark_frequency
    global injector_frequency
    global injector_duration
    
    spark_frequency = 0
    injector_frequency = 0
    injector_duration = 0.01

    stop_threads = False
    spark_gpio_thread = threading.Thread(target=spark_gpio_functions)
    spark_gpio_thread.start()

    injector_gpio_thread = threading.Thread(target=injector_gpio_functions)
    injector_gpio_thread.start()

    root = Tk()
    run = UI(root)
    root.mainloop()

    # on end of mainloop, end thread.
    print("mainloop ended")
    stop_threads = True
    spark_gpio_thread.join()
    injector_gpio_thread.join()

    # uncomment when I run irl
    # cleanup(injector_pin, spark_pin)