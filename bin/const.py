import enum

DEFAULT_FILE_NAME = 'DEFAULT'

RANDOM_MIX_CONFIG_NAME = 'RandomMix'
WIDTH_NAME = 'Width'
HIGHT_NAME = 'Hight'

class AutoName(enum.Enum):
  def _generate_next_value_(name, start, count, last_values):
    return name

class Algorithms(AutoName):
  RANDOM_MIX = enum.auto()