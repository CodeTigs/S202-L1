class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        # Retorna a string com a mensagem da aula
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."


class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        # Retorna a string  de presença
        return f"O aluno {self.nome} está presente."


class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        self.assunto = assunto
        # Caso não for passada uma lista de alunos, inicia com uma lista vazia
        self.alunos = alunos if alunos is not None else []
    
    def adicionar_aluno(self, aluno):
        # Adiciona o objeto aluno à lista de alunos
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        # Gera a lista de strings chamando o método presenca de cada aluno
        presencas = [aluno.presenca() for aluno in self.alunos]
        lista_alunos = "\n".join(presencas)
        return (f"Presenca na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n"
                f"{lista_alunos}")


professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())
