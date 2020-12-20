# -*- coding: utf-8 -*-
from multiprocessing import Process
from datetime import datetime
import time

class Timer(Process):
    def __init__(self, server_point):
        Process.__init__(self)
        self.server_point = server_point

    def run(self):
        while 1:
            current_time = datetime.now()
            time.sleep(1)
            self.server_point.send(current_time)
        self.server_point.close()
