import utils
import glob
import sys
import const
import configparser
import cv2
import algorithms.random_mix as random_mix

def _get_config():
  config = configparser.ConfigParser()
  config.read('algorithms/config.ini')
  return config

def apply_algorithm(frames_path, image_extention, algorithm):
  count = 1
  for item in sorted(glob.glob(frames_path + '/*.%s' % image_extention), key=utils.natural_keys):
    print(count)
    _apply_algorithm_per_frame(item, algorithm)
    count += 1

def _apply_algorithm_per_frame(frame_full_path, algorithm):
  if algorithm == const.Algorithms.RANDOM_MIX:
    config = _get_config()[const.RANDOM_MIX_CONFIG_NAME]
    random_mix.call(frame_full_path, int(config[const.WIDTH_NAME]), int(config[const.HIGHT_NAME]))

if __name__ == '__main__':
  # print(sys.argv[1], 'jpg', sys.argv[2], sys.argv[3])
  apply_algorithm(sys.argv[1], 'jpg', sys.argv[2], sys.argv[3], sys.argv[4])