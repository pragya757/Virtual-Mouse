import cv2
import mediapipe as mp
import numpy as np

class EyeDetector:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        # Define eye landmarks
        self.LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
        self.RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
        
    def find_eyes(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(img_rgb)
        if results.multi_face_landmarks:
            mesh_points = np.array([np.multiply([p.x, p.y], [img.shape[1], img.shape[0]]).astype(int) 
                                  for p in results.multi_face_landmarks[0].landmark])
            
            # Draw eye contours
            left_eye = mesh_points[self.LEFT_EYE]
            right_eye = mesh_points[self.RIGHT_EYE]
            
            cv2.polylines(img, [left_eye], True, (0, 255, 0), 1)
            cv2.polylines(img, [right_eye], True, (0, 255, 0), 1)
            
            # Calculate eye centers
            left_center = np.mean(left_eye, axis=0).astype(int)
            right_center = np.mean(right_eye, axis=0).astype(int)
            
            cv2.circle(img, tuple(left_center), 3, (255, 0, 0), -1)
            cv2.circle(img, tuple(right_center), 3, (255, 0, 0), -1)
            
            return mesh_points
        return None