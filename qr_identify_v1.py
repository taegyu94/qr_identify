import picamera
import time
import datetime


while True : 
    s = raw_input()

    print(s)
    s = s + "\n"
    now = datetime.datetime.now()
    filename = now.strftime('%Y-%m-%d- %H:%M:%S')
    f = open('/home/pi/qr_identify/logfiles_txt/'+filename+'READ.txt','w')
    f.write(s)
    f.close()

    with picamera.PiCamera() as camera :
        camera.resolution = (1024,768)
        #now = datetime.datetime.now()
        filename = now.strftime('%Y-%m-%d- %H:%M:%S'+'.jpg')
        camera.start_preview()
        time.sleep(2)
        camera.stop_preview()
        path = ('/home/pi/qr_identify/logfiles_jpg/'+filename)
        camera.capture(path)
