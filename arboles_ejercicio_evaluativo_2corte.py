
# 1. Implementa el método `eliminar(valor)` en la clase `ArbolBinarioBusqueda`. Asegúrate de manejar los 3 casos descritos en la teoría.
class Nodo:

  def __init__(self, valor):
    self.valor = valor
    self.izq = None
    self.der = None


class arbolbinario:

  def __init__(self):
    self.raiz = None

  def eliminar(self, valor):
    self.raiz = self._eliminar_rec(self.raiz, valor)

  def _eliminar_rec(self, nodo, valor):
    if nodo is None:
      return None

    if valor < nodo.valor:
      nodo.izq = self._eliminar_rec(nodo.izq, valor)
    elif valor > nodo.valor:
      nodo.der = self._eliminar_rec(nodo.der, valor)
    else:

      if nodo.izq is None:
        return nodo.der
      elif nodo.der is None:
        return nodo.izq

      sucesor = self._encontrart_min(nodo.der)
      nodo.valor = sucesor.valor
      nodo.der = self._eliminar_rec(nodo.der, sucesor.valor)

    return nodo

  def _encontrart_min(self, nodo):
    actual = nodo
    while actual.izq is not None:
      actual = actual.izq
    return actual
  
# 2. Implementa el recorrido por niveles (BFS - Breadth First Search) utilizando una Cola (`queue`).
from collections import deque


def recorrido_niveles(raiz):
  if raiz is None:
    return []

  resultado = []
  cola = deque([raiz])

  while cola:
    nodo_actual = cola.popleft()
    resultado.append(nodo_actual.valor)

    if nodo_actual.izq:
      cola.append(nodo_actual.izq)
    if nodo_actual.der:
      cola.append(nodo_actual.der)

  return resultado

# 3. Escribe una función que tome un árbol BST y retorne la suma de todos sus elementos sin modificar el árbol original.

def sumar_elementos(raiz):
  if raiz is None:
    return 0

  return (
      raiz.valor
      + sumar_elementos(raiz.izq)
      + sumar_elementos(raiz.der)
  )

# 4. Escribe un método `es_completo()` que valide si todos los nodos internos de un BST tienen exactamente dos hijos.

def es_completo(raiz):
  if raiz is None:
    return True

  if raiz.izq is None and raiz.der is None:
    return True

  if raiz.izq is not None and raiz.der is not None:
    return es_completo(raiz.izq) and es_completo(raiz.der)

  return False

# 5. Crea una función `balancear_arbol()` que tome un BST potencialmente degenerado, extraiga sus elementos y construya un nuevo

def balancear_arbol(arbol_original):
  def in_order(nodo, elementos):
    if nodo:
      in_order(nodo.izq, elementos)
      elementos.append(nodo.valor)
      in_order(nodo.der, elementos)

  elementos = []
  in_order(arbol_original.raiz, elementos)

  def construir_balanceado(lista):
    if not lista:
      return None

    medio = len(lista) // 2
    nodo = Nodo(lista[medio])

    nodo.izq = construir_balanceado(lista[:medio])
    nodo.der = construir_balanceado(lista[medio + 1:])

    return nodo

  nuevo_arbol = arbolbinario()
  nuevo_arbol.raiz = construir_balanceado(elementos)
  return nuevo_arbol