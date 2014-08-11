import picamera
import os
import time
import functools

class PIC:

    def __init__(self, cameraconf):
        self._config = cameraconf

    def open_close_camera(func):
        def inner(*args, **kwargs):
            args[0].open_camera()
            func(*args)
            args[0].close_camera()
        return inner

    @open_close_camera
    def get_picture(self):
        self.camera.resolution = (int(self._config['resolution_x']), int(self._config['resolution_y']))
        filename = self.__getNextFileNameImage(self._config['directory'])
        self.camera.capture(filename, 'png',False)

    @open_close_camera
    def get_video(self):
        filename = __getNextFileNameVideo(self._config['directory'])
        self.camera.start_recording(filename)
        self.camera.wait_recording(self._config['wait_recording'])
        self.camera.stop_recording()

    @open_close_camera
    def get_continous_pictures(self,number):
        filename = self.__getNextFileNameContinuous(self._config['directory'])       
        for i, filename in enumerate(self.camera.capture_continuous(filename)):
            print(filename)
            time.sleep(1)
            if i == number:
                break

    def __getNextFileNameImage(self,directory):
        fullpath = os.path.realpath(directory)
        if(os.path.isdir(fullpath)):
            return fullpath +"/"+time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())+".png" 

                
                                       
    def __getNextFileNameVideo(self,directory):
        fullpath = os.path.realpath(directory)
        if(os.path.isdir(fullpath)):
            return fullpath +"/"+time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())+".h264" 


    def __getNextFileNameContinuous(self,directory):
        fullpath = os.path.realpath(directory)
        if(os.path.isdir(fullpath)):
            return fullpath +"/img{timestamp:%Y-%m-%d-%H-%M-%S}.png" 
            
    def open_camera(self):
        self.camera = picamera.PiCamera()
        self.camera.led = True

    def close_camera(self):
        self.camera.close()

