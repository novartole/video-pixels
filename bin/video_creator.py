import logging
import time
import cv2
import glob
import utils

def create_video(frames_path_input, video_fps, image_extention, video_extension, video_width, video_hight, path_output, file_name):
  time_start = time.time()

  logging.info('Converting..')
  print('\nConverting..')

  fourcc = cv2.VideoWriter_fourcc(*utils.get_fourcc(video_extension))
  video_writer = cv2.VideoWriter(path_output + '/{0}.{1}'.format(file_name, video_extension), fourcc, video_fps, (video_width, video_hight))

  for item in sorted(glob.glob(frames_path_input + '/*.%s' % image_extention), key=utils.natural_keys):
    image = cv2.imread(item)
    video_writer.write(image)

  video_writer.release()

  time_end = time.time()

  logging.info('Done creating a video')
  logging.info('It took %d seconds for conversion', time_end - time_start)
  print ('\nDone creating a video\n')
  print ('It took %d seconds for conversion.' % (time_end - time_start))