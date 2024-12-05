class Aluno:
  def __init__(self, nome, sobrenome, nota): 
    if nota < 0 or nota > 10:
      raise ValueError("A nota não pode ser menor do que 0 ou maior do que 10.")

    self.nome = nome;
    self.sobrenome = sobrenome;
    self.nota = nota;

  def mostrarAluno(self):
    return f'Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota}'
