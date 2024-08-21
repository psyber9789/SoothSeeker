from app.util.list import flatten

def append_to_all(targets: list[list[str]], sources: list[str]) -> list[list[str]]:
  return flatten([
    [(target + [source]) for target in targets] for source in sources
  ])

def build_word_combo_lists(words: list[str], depth: int = 0) -> list[list[str]]:
  level = append_to_all([[]], words)
  combos = []

  while depth >= 1:
    level = append_to_all(level, words)
    combos.append(level)
    depth -= 1

  return flatten(combos)

def build_joined_combos(word_combo_lists: list[list[str]], delimiters: list[str]) -> list[str]:
  return flatten([
    [delimiter.join(word_combo) for word_combo in word_combo_lists] for delimiter in delimiters
  ])

def build_wrapper_combos(words: list[str], wrappers: list[str]) -> list[str]:
  return flatten([
    [[wrapper + word + wrapper, wrapper + word, word + wrapper] for word in words] for wrapper in wrappers
  ], 2)
