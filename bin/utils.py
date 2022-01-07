import logging
import os
import re
import const

def mkdir(path):
  try:
    os.mkdir(path)
  except FileExistsError:
    logging.info('Directory exists, skip creating')
    print('Directory exists, skip creating')

def _remove_files(path):
  with os.scandir(path) as it:
    for entry in it:
      if entry.is_file():
        os.remove(entry.path)

def remove_directory(path):
  _remove_files(path)

  os.rmdir(path)

def _atoi(text):
  return int(text) if text.isdigit() else text

def natural_keys(text):
  return [_atoi(c) for c in re.split(r'(\d+)', text)]

def get_file_name(path, wish_name):
  return path.split('/')[-1].split('.')[0] if wish_name == const.DEFAULT_FILE_NAME else wish_name

def get_fourcc(file_extension):
  if file_extension == 'mp4':
    return 'mp4v'
  elif file_extension == 'avi':
    return 'MJPG'
  else:
    raise NotImplementedError