import torch
import cv2
import numpy as np
import threading


cap_right = cv2.VideoCapture(0)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s') 
results_lock = threading.Lock()
results=None
stop_flag=False

def detect_object():
    global results,stop_flag
    while True:
        ret_right, frame_right = cap_right.read()

        if ret_right==False:
            break
        else:
            _results = model(frame_right)
            # for res in results.xyxy[0]:
            #     print(results.names[int(res[5])])
            with results_lock:
                results=_results

            cv2.imshow("frame-right",np.squeeze(results.render()))

            if cv2.waitKey(1) & 0xFF == 27:
                break
    cap_right.release()
    cv2.destroyAllWindows()
    stop_flag=True

def print_results():
    global results,stop_flag
    while not stop_flag:
        with results_lock:
            if results is not None:
                for res in results.xyxy[0]:
                    print(results.names[int(res[5])])

thread1=threading.Thread(target=detect_object)
thread2=threading.Thread(target=print_results)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

