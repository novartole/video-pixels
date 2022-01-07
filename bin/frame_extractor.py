import logging
import cv2
import time

class Extractor(object):
  def __init__(self, path_input):
    self._path_input = path_input
    self._video_capture = cv2.VideoCapture(path_input)

  def get_width(self):
    return int(self._video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))

  def get_hight(self):
    return int(self._video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

  def extract_frames(self, frames_path_output):
    video_capture = cv2.VideoCapture(self._path_input)

    video_length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    logging.info('Number of frames: %d', video_length)
    print('\nNumber of frames: ', video_length)

    time_start = time.time()

    logging.info('Extracting..')
    print('\nExtracting..')

    count = 0
    success, image = video_capture.read()
    while success:
      cv2.imwrite(frames_path_output + '/frame%d.jpg' % count, image)
      success, image = video_capture.read()
      count += 1

    time_end = time.time()

    logging.info('Done extracting frames. %d frames extracted', count)
    logging.info('It took %d seconds for conversion', time_end - time_start)
    print ('\nDone extracting frames.\n%d frames extracted' % count)
    print ('It took %d seconds for conversion.' % (time_end - time_start))