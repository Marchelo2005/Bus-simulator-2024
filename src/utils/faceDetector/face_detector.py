import cv2;import pygame;import random
from movementBus.pointsAndVideos.drawPoint.drawPoint import drawPoint
from utils.constants.constantPoint.constantPoint import coordinate
class detector():
    txtVideo=""
    def face():
        pygame.display.set_caption("Video Display")
        protoTxt = "utils/faceDetector/model/deploy.prototxt"
        model = "utils/faceDetector/model/res10_300x300_ssd_iter_140000.caffemodel"
        net = cv2.dnn.readNetFromCaffe(protoTxt, model)

        if detector.txtVideo == "exit":
            randomVideo = random.randint(1, 2)
            cap = cv2.VideoCapture("utils/faceDetector/video/videoPersonExit/" + detector.txtVideo + repr(randomVideo) + ".mp4")
        elif detector.txtVideo == "person":
            randomVideo = random.randint(1, 24)
            cap = cv2.VideoCapture("utils/faceDetector/video/videoPersonEntry/" + detector.txtVideo + repr(randomVideo) + ".mp4")

        screenVideo = pygame.display.set_mode((400, 800))
        accelerationFactor = 2 
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            height, width, _ = frame.shape
            frameResized = cv2.resize(frame, (300, 300))
            blob = cv2.dnn.blobFromImage(frameResized, 1.0, (300, 300), (104, 117, 123))
            net.setInput(blob)
            detections = net.forward()

            faceDetected = False

            for detection in detections[0][0]:
                if detection[2] > 0.5:
                    faceDetected = True
                    box = detection[3:7] * [width, height, width, height]
                    xStart, yStart, xEnd, yEnd = int(box[0]), int(box[1]), int(box[2]), int(box[3])
                    cv2.rectangle(frame, (xStart, yStart), (xEnd, yEnd), (0, 255, 0), 2)
                    cv2.putText(frame, "Conf: {:.2f}%".format(detection[2] * 100), (xStart, yStart - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

            """if detector.txtVideo == "person" and faceDetected:
                drawPoint(coordinate.points)
                faceDetected = False """

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.transpose(frame)
            frameSurface = pygame.surfarray.make_surface(frame)
            screenVideo.fill((0, 0, 0))
            screenVideo.blit(frameSurface, (0, 0))
            pygame.display.flip()

            if cv2.waitKey(1) & 0xFF == 27:
                break
            for _ in range(accelerationFactor - 1):
                cap.grab()
        cap.release()
        cv2.destroyAllWindows()
    pass
