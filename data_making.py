
import os
import numpy as np
import cv2

file_names = []

for root, dirs, files in os.walk("AudioVisualClip/"):
    for file in files:
        if file.endswith(".avi"):
            # print(os.path.join(root, file))
            file_names.append(os.path.join(root, file))

def get_images_from_video(filename,frame_count):
        # Create a VideoCapture object and read from input file 
    cap = cv2.VideoCapture(filename)

    # Check if camera opened successfully 
    if (cap.isOpened()== False): 
        print("Error opening video file") 

    complete_frames = []

    no = 0
    # Read until video is completed 
    while(cap.isOpened()): 
        
        # Capture frame-by-frame 
        ret, frame = cap.read() 
        if ret == True: 

            # Display the resulting frame 
            # cv2.imshow('Frame', frame) 
            no = no+1
            frame = cv2.resize(frame,(64,64))
            complete_frames.append(frame)
            # cv2.imwrite('rough/img/'+str(no)+'.png',frame)

            # Press Q on keyboard to exit 
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break

        # Break the loop 
        else: 
            break
    
    complete_frames = np.array(complete_frames)

    frame_numbers = np.linspace(0,complete_frames.shape[0]-1,frame_count).astype('int')

    # print(frame_numbers)

    return complete_frames[frame_numbers]
    
import pickle
from tqdm import tqdm

for f in tqdm(file_names):
    # print(f.split('/')[1].split('\\'))
    
    person,ff = f.split('/')[1].split('\\')

    outfile = open('data/'+person+'_'+ff[:-4],'wb')

    facials  = get_images_from_video(f,96)

    pickle.dump(facials,outfile)

    # break




