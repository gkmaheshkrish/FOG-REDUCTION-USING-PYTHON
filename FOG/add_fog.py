video_src="./video.mp4"
fog="./ezgif.com-crop.mp4"
import cv2
import numpy as np
video=cv2.VideoCapture(video_src)
fog_video=cv2.VideoCapture(fog)
shape=None
fog_frames=[]

while(video.isOpened()):
	flag,frame1=video.read()
	shape=frame1.shape
	break
print(shape)

while(fog_video.isOpened()):
	flag,frame=fog_video.read()
	if flag:
		frame=cv2.resize(frame,(shape[1],shape[0]))
		fog_frames.append(frame)
	else:
		break
count=0
alpha=0.8
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
print(shape)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (shape[0],shape[1]),True)

while(video.isOpened()):
	flag,frame1=video.read()
	if flag:
		if(count<len(fog_frames)-1):
			# apply the overlay
			cv2.addWeighted(fog_frames[count], alpha, frame1, 1 - alpha,0, frame1)
		count+=1
		# write the flipped frame
		out.write(frame1)
		cv2.imshow('frame',frame1)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
out.release()
cv2.destroyAllWindows()
print(len(fog_frames))
