"""
"""

import sys
import app.utils as utils
import app.words as words

keywords = ['American', 'Airlines', 'Pentagon', 'Flight77', '9:37a.m.', '9:37 a.m']

all_keywords_with_casing = set([*keywords, *[keyword.upper() for keyword in keywords], *[keyword.lower() for keyword in keywords]])
# utils.dpprint('all_keywords_with_casing', all_keywords_with_casing)

word_combo_lists = words.build_word_combo_lists(all_keywords_with_casing, 3)
# utils.dpprint('word_combo_lists', word_combo_lists)

joined_combos = set([*all_keywords_with_casing, *words.build_joined_combos(word_combo_lists, ['', ' ', '.', '-', '_'])])
# utils.dpprint('joined_combos', joined_combos)

wrapper_combos = words.build_wrapper_combos(joined_combos, ['_', '-'])
# utils.dpprint('wrapper_combos', wrapper_combos)

total_combos = set([*joined_combos, *wrapper_combos])
utils.dpprint('len', len(total_combos), 'size(mb)', sys.getsizeof(total_combos) / 1024 / 1024)


# input = base64.b16decode('2c04b269c78391c69d70a550c2775e3300957ec301a08c9c'.upper())
# key = b'Pentagon'
# iv = b'Flight77'

# des = DES.new(key, DES.MODE_CBC, iv)

# output = des.decrypt(input)

# print(output.decode())