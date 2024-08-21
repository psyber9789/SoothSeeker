def get_all_substrs(subject: str, min: int, max: int) -> list[str]:
  groups: list[str] = []

  for size in range(min, max):
    for i in range(0, len(subject) - size):
      groups.append(subject[i:i+size])

  return groups