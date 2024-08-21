import rich.pretty
from app.util.list import list_deep

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
