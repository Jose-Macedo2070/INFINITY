
# exemplo de associação unilateral:
# class Curso:
#     def __init__(self,nome, carga_hora):
#         self.nome = nome
#         self.carga_hora = carga_hora

#     def __str__(self):
#         return f"Curso: {self.nome}, Carga Horária: {self.carga_hora}h"
    

# class Aluno:
#     def __init__(self, nome, curso):
#         self.nome = nome
#         self.curso = curso


#     def __str__(self):
#         return f"Aluno: {self.nome}, Curso: {self.curso}"




# cursoPy = Curso("Python", 40)

# aluno1 = Aluno("José", cursoPy)

# print(aluno1)



# exemplo de associação bidirecional:










# exemplo de encapsulamento:






class Autor:
    def __init__(self, nome, nacionalidade):
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    def __str__(self):
        return f" {self.__nome}, nacionalidade: {self.__nacionalidade}"






class Livro:
    def __init__(self, titulo, ano, autor):
        self.__titulo = titulo
        self.__ano =  ano
        self.__autor = autor



    
    def __str__(self):
        return f"nome: {self.__titulo}, ano: {self.__ano}, autor: {self.__autor}"
    


autor1 = Autor('joão', 'br')
autor2 = Autor('apollo', 'br')

livro1 = Livro(' o auto da compadecida', 1900, autor1)
livro2 = Livro('o reino da putaria', 1400, autor2)

print(livro1)
print(livro2)





