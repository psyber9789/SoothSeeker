from app.util.debug import dpprint
from app.metrics.substr_regularity import SubstrRegularity

def test():
  str = 'ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt'
  # str = 'test test test test this test this test test test this test this test test test this test this test test'
  # str = "The Turabay dynasty was a family of Bedouin emirs who governed the district of Lajjun in northern Palestine during Ottoman rule in the 16th–17th centuries. The family's forebears had served as chiefs of Jezreel Valley during Mamluk rule in the late 15th century. During the Ottoman conquest of the region in 1516–1517, the family aided Ottoman sultan Selim I. The Ottomans kept them as guardians of the strategic Via Maris and Damascus–Jerusalem highways and rewarded them with tax farms. Although in the 17th century several of their emirs lived in towns, the Turabays largely remained nomads, camping with their tribesmen near Caesarea in the winters and the plain of Acre in the summers. The eastward migration of their tribesmen to the Jordan Valley, Ottoman centralization, and falling tax revenues brought about their political decline and they were permanently stripped of office in 1677. Descendants of the family continue to live in the area."
  # str = 'sanfh3298eyq89fdhs8haf8ewdgs8uhuiewbudbsihcb3u2beqiufwcad'
  sr = SubstrRegularity(str)
  dpprint('str', str, 'len', len(str), 'minSize', sr.minSize, 'maxSize', sr.maxSize, 'max_regularity', sr.max_regularity(), 'measure', sr.measure(), 'normalised', sr.normalised())
