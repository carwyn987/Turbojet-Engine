# uncomment when I run irl
# import RPi.GPIO as GPIO
from tkinter import *
import threading
import time

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

class App(threading.Thread):

    def __init__(self, root):
        threading.Thread.__init__(self)
        self.start()

        self.root = root

    def callback(self):
        self.root.quit()

    def setup_ui(self):

        # Setup UI for spark frequency / s    
        self.root.spark_freq_label = Text(self.root, state='disabled', width=44, height=1)
        self.root.spark_freq_label.configure(state='normal')
        self.root.spark_freq_label.insert('end', 'Spark frequency per second')
        self.root.spark_freq_label.configure(state='disabled')
        self.root.spark_freq_label.pack()

        # Setup spark frequency / s slider
        self.root.spark_freq = Scale(self.root, from_=0, to=600, length=600,tickinterval=50, orient=HORIZONTAL)
        self.root.spark_freq.pack()

        self.root.injector_freq_label = Text(self.root, state='disabled', width=44, height=1)
        self.root.injector_freq_label.configure(state='normal')
        self.root.injector_freq_label.insert('end', 'Injector frequency per second')
        self.root.injector_freq_label.configure(state='disabled')
        self.root.injector_freq_label.pack()

        # Setup spark frequency / s slider
        self.root.injector_freq = Scale(self.root, from_=0, to=100, length=600,tickinterval=10, orient=HORIZONTAL)
        self.root.injector_freq.pack()


        self.root.injector_dur_label = Text(self.root, state='disabled', width=44, height=1)
        self.root.injector_dur_label.configure(state='normal')
        self.root.injector_dur_label.insert('end', 'Injector duration per fire')
        self.root.injector_dur_label.configure(state='disabled')
        self.root.injector_dur_label.pack()

        # Setup spark frequency / s slider
        self.root.injector_dur = Scale(self.root, from_=0.0, to=1.0, digits = 3, resolution = 0.01, length=600,tickinterval=0.1, orient=HORIZONTAL)
        self.root.injector_dur.set(0.01)
        self.root.injector_dur.pack()

        # GPIO.output(18, GPIO.HIGH)
        # time.sleep(3)

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.setup_ui()
        self.root.mainloop()
        

def main(injector_pin, spark_pin):
    root = Tk()

    app = App(root)

    for i in range(100):
        print(app.root.injector_dur.get())

if __name__ == "__main__":

    injector_pin = 17
    spark_pin = 27

    # uncomment when I run irl
    # setup(injector_pin, spark_pin)
    main(injector_pin, spark_pin)
    # uncomment when I run irl
    # cleanup(injector_pin, spark_pin)





# #Import all the necessary libraries
# from tkinter import *
# import time
# import threading

# #Define the tkinter instance
# root= Tk()

# #Define the size of the tkinter frame
# root.geometry("700x400")

# #Define the function to start the thread
# def thread_fun():
# #    root.spark_freq_label.config(text="You can Click the button or Wait")
# #    time.sleep(5)
# #    root.spark_freq_label.config(text= "5 seconds Up!")

#    print(root.spark_freq.get())

# # Setup UI for spark frequency / s    
# root.spark_freq_label = Text(root, state='disabled', width=44, height=1)
# root.spark_freq_label.configure(state='normal')
# root.spark_freq_label.insert('end', 'Spark frequency per second')
# root.spark_freq_label.configure(state='disabled')
# root.spark_freq_label.pack()

# # Setup spark frequency / s slider
# root.spark_freq = Scale(root, from_=0, to=600, length=600,tickinterval=50, orient=HORIZONTAL, command=threading.Thread(target=thread_fun).start())
# root.spark_freq.pack()

# root.injector_freq_label = Text(root, state='disabled', width=44, height=1)
# root.injector_freq_label.configure(state='normal')
# root.injector_freq_label.insert('end', 'Injector frequency per second')
# root.injector_freq_label.configure(state='disabled')
# root.injector_freq_label.pack()

# # Setup spark frequency / s slider
# root.injector_freq = Scale(root, from_=0, to=100, length=600,tickinterval=10, orient=HORIZONTAL)
# root.injector_freq.pack()

# root.injector_dur_label = Text(root, state='disabled', width=44, height=1)
# root.injector_dur_label.configure(state='normal')
# root.injector_dur_label.insert('end', 'Injector duration per fire')
# root.injector_dur_label.configure(state='disabled')
# root.injector_dur_label.pack()

# # Setup spark frequency / s slider
# root.injector_dur = Scale(root, from_=0.0, to=1.0, digits = 3, resolution = 0.01, length=600,tickinterval=0.1, orient=HORIZONTAL)
# root.injector_dur.set(0.01)
# root.injector_dur.pack()

# root.mainloop()