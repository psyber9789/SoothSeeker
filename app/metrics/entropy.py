import collections
import scipy.stats
from app.metric import Metric

class Entropy(Metric):
  def value(self, data: str):
    bases = collections.Counter([char for char in data])
    bases_values = bases.values()
    bases_sum = sum(bases_values)
    distribution = [x / bases_sum for x in bases_values]

    entropy = float(scipy.stats.entropy(distribution, base=2))

    # Scale metric to between 0 and 1
    return max(min(entropy / 8, 1), 0)