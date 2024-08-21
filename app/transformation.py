from collections.abc import Callable

class Transformation:
  def handle(self, input: str) -> str:
    raise NotImplementedError('Method handle has not been defined')

