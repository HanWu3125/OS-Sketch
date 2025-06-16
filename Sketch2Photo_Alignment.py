import os
import cv2
import dlib
import numpy as np

def align_faces(image1, image2):
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    faces1 = detector(img1, 1)
    faces2 = detector(img2, 1)

    if len(faces1) != 1 or len(faces2) != 1:
        print("Ensure exactly one human face is present in each image.")
        return

    landmarks1 = predictor(img1, faces1[0])
    landmarks2 = predictor(img2, faces2[0])

    eyes1 = (landmarks1.part(36).x, landmarks1.part(36).y), (landmarks1.part(45).x, landmarks1.part(45).y)
    nose1 = (landmarks1.part(30).x, landmarks1.part(30).y)
    mouth1 = (landmarks1.part(48).x, landmarks1.part(48).y), (landmarks1.part(54).x, landmarks1.part(54).y)

    eyes2 = (landmarks2.part(36).x, landmarks2.part(36).y), (landmarks2.part(45).x, landmarks2.part(45).y)
    nose2 = (landmarks2.part(30).x, landmarks2.part(30).y)
    mouth2 = (landmarks2.part(48).x, landmarks2.part(48).y), (landmarks2.part(54).x, landmarks2.part(54).y)

    src_pts = np.float32([eyes1[0], eyes1[1], nose1, mouth1[0], mouth1[1]])
    dst_pts = np.float32([eyes2[0], eyes2[1], nose2, mouth2[0], mouth2[1]])
    M = cv2.estimateAffinePartial2D(src_pts, dst_pts)[0]  #

    aligned_img = cv2.warpAffine(img1, M, (img2.shape[1], img2.shape[0]))

    print("Alignment completed.")
    filename = os.path.basename(image1)
    save_path = "/path/to/your/save_path/" + filename
    cv2.imwrite(save_path, aligned_img)


if __name__ == "__main__":
    raw_image = "/path/to/your/raw_image"  # Raw image path (photo or sketch to be aligned)
    reference_image = "/path/to/your/reference_image" # Reference image path (target image for alignment)
    align_faces(raw_image, reference_image)

