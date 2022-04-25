
#

from qchecker.substructures import IfElseReturnBool

code = """
class Foo:
    def __init__(self, x):
        self.x = x
    
    def bar(self):
        if self.x < 10:
            return True
        else:
            return False
""".strip()

matches = IfElseReturnBool.list_matches(code)
print(IfElseReturnBool.technical_description)
print(*matches, sep="\n")