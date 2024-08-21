import rich.pretty
import copy
from typing import cast

def unique[T](values: list[T]) -> list[T]:
  return list(set(values))

def dprint(*args) -> None:
  """
  Print data. Resolves nested map objects to prevent '<map object at 0x100b2db70>'.
  Useful for inspecting intermediary values.
  """
  for arg in [*args, '']:
    print(arg if isinstance(arg, str) else list_deep(arg))

def dpprint(*args) -> None:
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

def list_deep[T: object](target: T) -> T:
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

  return cast(T, do(target))

def flatten(value, depth: int = 1) -> list:
  """
  Flatten nested array structures.

  Keyword arguments:
  value -- the iterable
  """
  while depth > 0:
    value = [n for n1 in value for n in n1]
    depth -= 1

  return value