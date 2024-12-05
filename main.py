import aluno as a;
import turma as t;

alunos = []

alunos.append(a.Aluno('Fabio', 'Teixeira', 8));
alunos.append(a.Aluno('Fabiano', 'Teixeira', 10));

try:
  alunos.append(a.Aluno('Melissa', 'Teixeira', -1))
except ValueError as e:
  print(f"Erro ao adicionar aluno: {e}")

turmaObject = t.Turma();
turmaObject.cadastrarAlunos(alunos);

turmaObject.mostrarAlunos();

print('*'*30)

if turmaObject.menorNota:
  print('Aluno com menor nota:', turmaObject.menorNota.mostrarAluno())
if turmaObject.maiorNota:
  print('Aluno com maior nota:', turmaObject.maiorNota.mostrarAluno())
