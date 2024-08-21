import rich.pretty
import copy

def dprint(*args):
  """
  Print data. Resolves nested map objects to prevent '<map object at 0x100b2db70>'.
  Useful for inspecting intermediary values.
  """
  for arg in [*args, '']:
    print(arg if isinstance(arg, str) else list_deep(arg))

def dpprint(*args):
  """
  Pretty dprint.
  """
  for arg in [*args, '']:
    print(arg) if isinstance(arg, str) else rich.pretty.pprint(list_deep(arg))

def dprint_thru[T](label: str, value: T, *args) -> T:
  """
  Pass-thru debug print. Useful for inspecting lamdas.
  See: dprint, dpprint
  """
  dprint(label, value, *args)
  return value

def dpprint_thru[T](label: str, value: T, *args) -> T:
  """
  Pretty dprint_thru
  """
  dpprint(label, value, *args)
  return value

def list_deep(target):
  """
  Resolve nested map objects to lists.
  """
  def do(target):
    if isinstance(target, map|list):
      return [do(item) for item in target]

    if isinstance(target, set):
      return set([do(item) for item in target])

    if isinstance(target, tuple):
      return tuple(do(item) for item in target)

    if isinstance(target, dict):
      return {key: do(value) for key, value in target.values()}

    return target
  
  # Clone as resolving the map object affects other references
  target = copy.deepcopy(target)

  return do(target)

def flatten[T: list](deep: list[T], depth: int = 1) -> T:
  while depth > 0:
    deep = [n for n1 in deep for n in n1]
    depth -= 1

  return deep