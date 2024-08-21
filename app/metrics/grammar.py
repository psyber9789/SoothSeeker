from app.metric import Metric

# Base algorithm on the findings here https://aclanthology.org/D16-1228.pdf
class Grammar(Metric):
  def measure(self) -> float:
    return 1.0