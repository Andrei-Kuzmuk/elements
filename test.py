class PEP():
    def __init__(self) -> None:
        self.name = __class__.__name__
    
p = PEP()
print(p.name)