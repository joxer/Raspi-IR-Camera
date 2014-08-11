from lib.config import *
from lib.camera import * 
from lib.switches import * 

import time
if __name__ == '__main__':
    conf = Config("camera.conf")
    switches = Switches()
    pic = PIC(conf.get_dictionary())
    while True:
        time.sleep(0.1)
        switches.get_value(pic.get_picture)
        
