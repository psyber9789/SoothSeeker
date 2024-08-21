from collections import Counter
from app.metric import Metric
from app.util.string import get_all_substrs
import statistics
import math

class SubstrRegularity(Metric):
  minSize: int = 3
  maxSize: int = 6

  def measure(self) -> float:
    return statistics.geometric_mean(self.get_substr_counts())
  
  def get_max(self) -> int:
    return min(self.maxSize, len(self.data)) + 1
  
  def get_min(self) -> int:
    return max(self.minSize, 1)
  
  def get_substr_counts(self) -> list[int]:
    all_substrs = get_all_substrs(self.data, self.get_min(), self.get_max())
    counter = Counter(all_substrs)
    
    return [counter[group] for group in set(all_substrs)]
  
  def max_regularity(self) -> float:
    return statistics.geometric_mean(
      [(len(self.data) - size) + (self.get_max() - size) for size in range(self.get_min(), self.get_max())]
    )
