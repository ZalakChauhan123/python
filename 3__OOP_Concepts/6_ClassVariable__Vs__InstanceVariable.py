class ClassA:
    def __init__(self, insVar1):
        
        # This is Instance Variable
        self.insVar1 = insVar1


    # This is Class Variable
    ClassVar = "CLASS VARIABLE - DEFAULT"
    
    def ShowInsVariable(self):
        print(f"I am an Instane Variable = {self.insVar1}")

    def ShowClassVariable(self):
        print(f"Class Variable {self.ClassVar}")

# Instance Ins_A
Ins_A = ClassA("INS_1")
Ins_A.ClassVar = "--- I WORK FOR instance Ins_A"
Ins_A.ShowInsVariable()
Ins_A.ShowClassVariable()


# # Instance Ins_B
Ins_B = ClassA("INS_2")
Ins_B.ShowInsVariable()
Ins_B.ShowClassVariable()
