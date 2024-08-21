from app.util.debug import dpprint
from app.metrics.substr_regularity import SubstrRegularity

def test():
  # str = 'ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt'
  # str = 'test test test test this test this test test test this test this test test test this test this test test test this test this test test test this test this test test test this test this test test test this test this test test test this test this test test test this test this test'
  str = 'sanfh3298eyq89fdhs8haf8ewdgs8uhuiewbudbsihcb3u2beqiufwcad'
  sr = SubstrRegularity(str)
  dpprint('len', len(str), 'minSize', sr.minSize, 'maxSize', sr.maxSize, 'max_regularity', sr.max_regularity(), 'measure', sr.measure(), 'scaled', sr.measure() / sr.max_regularity())
  