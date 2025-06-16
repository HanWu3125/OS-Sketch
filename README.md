# OS-Sketch
![image](https://github.com/HanWu3125/OS-Sketch/blob/main/OS-Sketch.png)

**OS-Sketch** comprises a diverse style of sketches. It not only includes sketches previously used in research but also incorporates out-of-distribution (OOD) style sketches selected from the internet. Additionally, sketches selected from the internet are also available for researchers to conduct experimental studies. At the same time, the dataset not only contains traditional research photos with a single background but also includes numerous in-the-wild photos. It includes photos with different backgrounds, ages, sexes, expressions, perspectives and illumination. For a solid out-of-distribution evaluation, we select only one pair of images for training at each time, with the rest used for inference. By exposing the model to a variety of photos in a one-shot context, its performance can be intuitively demonstrated. 

It comprises four distinct components: 
(i) 40 photo-sketch pairs selected from online amateur artists and bloggers; 
(ii) 100 pairs from the Simple Color Backgrounds Face Sketch dataset CUFS; 
(iii) 110 pairs from the Dark Lighting Backgrounds dataset CUFSF; 
(iv) 150 pairs from the In-the-Wild dataset WildSketch.


## OS-Sketch Dataset Acquisition
1.Google Drive: [downloading link](https://drive.google.com/file/d/1FGmPlz84-C40XF50V92YYhzp7OMnnA0Q/view?usp=drive_link) 

2.Due to copyright restrictions, part of the CUFSF dataset must be obtained independently via the following link. Select photos and sketches ranging from "00043fb001d_931230.jpg" to "00152fa001d_931230.jpg" as test data:
https://mmlab.ie.cuhk.edu.hk/archive/cufsf/.

You can download the pre-trained facial landmark detection model file "shape_predictor_68_face_landmarks.dat" from: [downloading link](https://drive.google.com/file/d/1mkOKLUYtPBCGjM2TfxkpQ6qY-iD1YimH/view?usp=drive_link). And then modify the file path in `Sketch2Photo_Alignment.py` and execute the script to perform alignment between photos and sketches.

Then run `sketch_contrast_normalizer.py` to convert sketches into high-contrast grayscale images, ensuring sketches exhibit uniform pure black-and-white tonality.

3.All sketches are uniformly converted into high-contrast grayscale images during evaluation. If you wish to use the original Internet-sourced sketches for research, you can find them in the **original-ood-sketches** folder.


## Dataset Agreement
* The OS-Sketch dataset is available for **non-commercial research purposes** only.
* All images obtained from the Internet are not property of us. We are not responsible for the content nor the meaning of these images.
* You agree **not to** reproduce, duplicate, copy, sell, trade, resell or exploit for any commercial purposes, any portion of the images and any portion of derived data.
* You agree **not to** further copy, publish or distribute any portion of the OS-Sketch dataset. Except, for internal use at a single site within the same organization it is allowed to make copies of the dataset.
* We reserves the right to terminate your access to the OS-Sketch dataset at any time.
