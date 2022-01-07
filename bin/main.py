import sys
import uuid
import logging
import video_creator
import utils
import frame_processor
import configparser
import const
from frame_extractor import Extractor
from argument_parser import Parser

def _get_arguments():
  parser = Parser()
  return parser.parse(sys.argv)

def _create_dirs(images_path_output, path_output):
  utils.mkdir(path_output)
  utils.mkdir(images_path_output)

def _setup_logger(debug):
  logging.basicConfig(
    filename='run_log.log', 
    encoding='utf-8', 
    level=logging.DEBUG if debug else logging.NOTSET, 
    filemode='w', 
    format='%(asctime)s %(message)s')

def _get_config():
  config = configparser.ConfigParser()
  config.read('config.ini')
  return config

def main():
  config = _get_config()
  args = _get_arguments()

  _setup_logger(args.debug)
  
  config_default = config['DEFAULT']
  image_extention = config_default['ImageExtention']
  algorithm = const.Algorithms(args.algorithm)
  frame_extractor = Extractor(args.path_input)
  video_width = frame_extractor.get_width()
  video_hight = frame_extractor.get_hight()
  unique_string = '_%s' % uuid.uuid4()
  frames_path_output = args.path_output + '/%s' % config_default['FramesDirName'] + unique_string
  file_name = utils.get_file_name(args.path_input, args.file_name)
  if args.keep_frames:
    file_name += unique_string

  _create_dirs(frames_path_output, args.path_output)

  frame_extractor.extract_frames(frames_path_output)
  frame_processor.apply_algorithm(frames_path_output, image_extention, algorithm)
  video_creator.create_video(frames_path_output, args.fps, image_extention, args.video_extension, video_width, video_hight, args.path_output, file_name)

  if not args.keep_frames:
    utils.remove_directory(frames_path_output)

if __name__ == '__main__':
  main()