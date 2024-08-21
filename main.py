"""
Work in progress. For the next while this file will contain top-level code for executing code during
the initial development, before this file is then delegated solely to instantiating the application
instance, whereby an applicaton controller will initialise the application.
"""

import sys
from app.utils import dpprint, unique
import app.words as words

keywords = ['American', 'Airlines', 'Pentagon', 'Flight77', '9:37a.m.', '9:37 a.m']

all_keywords_with_casing = unique(([*keywords, *[keyword.upper() for keyword in keywords], *[keyword.lower() for keyword in keywords]]))
# dpprint('all_keywords_with_casing', all_keywords_with_casing)

word_combo_lists = words.build_word_combo_lists(all_keywords_with_casing, 3)
# dpprint('word_combo_lists', word_combo_lists)

joined_combos = unique([*all_keywords_with_casing, *words.build_joined_combos(word_combo_lists, ['', ' ', '.', '-', '_'])])
# dpprint('joined_combos', joined_combos)

wrapper_combos = words.build_wrapper_combos(joined_combos, ['_', '-'])
# dpprint('wrapper_combos', wrapper_combos)

total_combos = [*joined_combos, *wrapper_combos]
dpprint('len', len(total_combos), 'size(mb)', sys.getsizeof(total_combos) / 1024 / 1024)
# dpprint('total_combos', total_combos)


# input = base64.b16decode('2c04b269c78391c69d70a550c2775e3300957ec301a08c9c'.upper())
# key = b'Pentagon'
# iv = b'Flight77'

# des = DES.new(key, DES.MODE_CBC, iv)

# output = des.decrypt(input)

# print(output.decode())