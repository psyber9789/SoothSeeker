from app.transformation import Transformation

class AutoDecrypt(Transformation):
  hints: list[str] = []
  dictionary: list[str] = []

  def handle(self, input: str) -> str:
    pass

  def build_permutations() -> list[list[str]]:
    pass

