import collections
import scipy.stats
from app.metric import Metric

class Entropy(Metric):
  def measure(self) -> float:
    bases = collections.Counter([char for char in self.data])
    bases_values = bases.values()
    bases_sum = sum(bases_values)
    distribution = [x / bases_sum for x in bases_values]

    return float(scipy.stats.entropy(distribution, base=2))
  
  def normalised(self) -> float:
    return max(min(self.measure() / 8, 1), 0)
    