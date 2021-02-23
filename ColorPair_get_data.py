import ColorPair as cp

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(cp.MAJOR_COLORS)
  if major_index >= len(cp.MAJOR_COLORS):
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % len(cp.MINOR_COLORS)
  if minor_index >= len(cp.MINOR_COLORS):
    raise Exception('Minor index out of range')
  return cp.MAJOR_COLORS[major_index], cp.MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = cp.MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = cp.MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(cp.MINOR_COLORS) + minor_index + 1
