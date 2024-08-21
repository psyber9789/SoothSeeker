class Metric:
  data: str

  def __init__(self, data: str) -> None:
    self.data = data

  def measure(self) -> float:
    raise NotImplementedError('Method not implemented')