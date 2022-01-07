import const
from argparse import ArgumentParser, SUPPRESS

class Parser(object):
  def __init__(self):
    self._parser = ArgumentParser(prog='video-pixels')
    self._add_arguments()

  def _add_arguments(self):
    self._parser.add_argument(
      '-i', '--path-input',
      required=True,
      help='full path to a video file'
    )
    self._parser.add_argument(
      '-o', '--path-output',
      default=SUPPRESS,
      help='result file path'
    )
    self._parser.add_argument(
      '-d', '--debug',
      action='store_true',
      help='turn on debug mode'
    )
    self._parser.add_argument(
      '-k', '--keep-frames',
      action='store_true',
      help='keep frames after video creating'
    )
    self._parser.add_argument(
      '-n', '--file-name',
      default=const.DEFAULT_FILE_NAME,
      help='result file name'
    )
    self._parser.add_argument(
      '--fps',
      type=int,
      default=30,
      help='output fps value'
    )
    self._parser.add_argument(
      '--video-extension',
      choices=['mp4', 'avi'],
      default='mp4',
      help='extension of output video'
    )
    self._parser.add_argument(
      '-a', '--algorithm',
      required=True,
      choices=[algorithm.name for algorithm in const.Algorithms],
      help='choose an algorithm to process frames'
    )

  def parse(self, argv):
    arguments = argv[1:]

    return self._parser.parse_args(arguments)