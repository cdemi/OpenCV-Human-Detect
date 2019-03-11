import logging
import sys
import datetime
import time
import cv2
logging.basicConfig(stream=sys.stdout, level=logging.INFO,format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p %Z")

logging.info("Started")
cap = cv2.VideoCapture("rtsp://192.168.2.8:554/user=admin&password=&channel=1&stream=0.sdp?real_stream--rtp-caching=100")
hog = cv2.HOGDescriptor()
hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
hogParams = {'winStride': (8, 8), 'scale': 1.4}
while True:
    # Read frame from camera
    ret, frame = cap.read()
    # found,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
    # (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)
    (rects, weights) = hog.detectMultiScale(frame, **hogParams)

    logging.info(rects)

    if len(rects)>0:
        logging.info(weights)
        # draw the original bounding boxes
        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imwrite("/out/" + str(time.time()) + ".jpg", frame)
