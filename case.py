class MinhaClasse:
    def __enter__(self):
        print("Entrei!!!")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saí!!!")
    
with MinhaClasse() as mc:
    print("Estou aqui dentro!")