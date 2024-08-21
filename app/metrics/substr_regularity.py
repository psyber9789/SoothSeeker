"""
Metric to test for the regularity of substrings of a string, and give an estimation as to the amount of structure above the individual character level
"""

from collections import Counter
from app.metric import Metric
from app.util.string import get_all_substrs
from statistics import mean
import math

class SubstrRegularity(Metric):
  minSize: int = 3
  maxSize: int = 9

  def measure(self) -> float:
    return math.sqrt(mean(self.get_substr_counts()))
  
  def normalised(self) -> float:
    return self.measure() / self.max_regularity()
  
  def get_max(self) -> int:
    return min(self.maxSize, len(self.data)) + 1
  
  def get_min(self) -> int:
    return max(self.minSize, 1)
  
  def get_substr_counts(self) -> list[int]:
    all_substrs = get_all_substrs(self.data, self.get_min(), self.get_max())
    counter = Counter(all_substrs)
    
    return [counter[group] - 1 for group in set(all_substrs)]
  
  def max_regularity(self) -> float:
    return math.sqrt(
      mean([(len(self.data) - size) + (self.get_max() - size) for size in range(self.get_min(), self.get_max())])
    )
