from .class_example import ClassExample
from .submodule.submodule_example import SubmoduleExample


def main():
    print(ClassExample().hello())
    print(SubmoduleExample().hello())
