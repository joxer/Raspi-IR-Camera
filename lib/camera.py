import picamera
import os
import time
import functools
import io
import time
import cv2
import numpy as np
class PIC:

    def __init__(self, cameraconf):
        self._config = cameraconf

    def open_close_camera(func):
        def inner(*args, **kwargs):
            args[0].open_camera()
            value = func(*args)
            args[0].close_camera()
            return value
        return inner

    @open_close_camera
    def get_picture(self):
        self.camera.resolution = (int(self._config['resolution_x']), int(self._config['resolution_y']))
        filename = self.__getNextFileNameImage(self._config['directory'])
        self.camera.capture(filename, 'png',False)
        return filename

    @open_close_camera
    def get_cv(self):
        self.camera.resolution = (int(self._config['resolution_x']), int(self._config['resolution_y']))
        filename = self.__getNextFileNameImage(self._config['directory'])
        stream = io.BytesIO()
        self.camera.capture(stream, format='jpeg')
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        blur = cv2.medianBlur(image,1)
        cv2.imwrite(filename,blur)
        return filename


    @open_close_camera
    def get_raw_picture(self):
        self.camera.resolution = (int(self._config['resolution_x']), int(self._config['resolution_y']))
        filename = self.__getNextFileNameImageRaw(self._config['directory'])
        self.camera.capture(filename, 'rgb',False,bayer=True)
        return filename

    @open_close_camera
    def get_video(self):
        filename = self.__getNextFileNameVideo(self._config['directory'])
        self.camera.start_recording(filename)
        self.camera.wait_recording(int(self._config['wait_recording']))
        self.camera.stop_recording()
        return filename

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

    def __getNextFileNameImageRaw(self,directory):
        fullpath = os.path.realpath(directory)
        if(os.path.isdir(fullpath)):
            return fullpath +"/"+time.strftime("%Y-%m-%d-%H-%M-%S", time.gmtime())+".jpg"
                                       
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
        self.camera.exposure_mode = 'auto'
        self.camera.awb_mode = 'auto'
        self.camera.led = True

    def close_camera(self):
        self.camera.close()

