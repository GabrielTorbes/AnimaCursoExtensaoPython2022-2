class Pessoa:
  #Atributos
  id = None
  nome = None

  #Método Construtor
  def init(self, id, nome):
    self.id = id
    self.nome = nome

  #Método para ajudar na exibição
  def str(self):
    return(f"{self.nome} ({self.id})")