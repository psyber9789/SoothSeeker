from app.transformation import Transformation

class AutoDecrypt(Transformation):
  hints: list[str] = []
  dictionary: list[str] = []

  def handle(self, input: str) -> str:
    return input

  def build_permutations(self) -> list[list[str]]:
    return [['']]

