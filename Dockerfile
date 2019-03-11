FROM valian/docker-python-opencv-ffmpeg:py3
WORKDIR /app
COPY ./camera_human_detect.py /app
CMD python3 camera_human_detect.py