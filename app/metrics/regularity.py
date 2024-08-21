from app.metric import Metric

class Regularity(Metric):
  def measure(self) -> float:
    return 0