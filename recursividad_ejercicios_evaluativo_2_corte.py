def multiplicacion(a, b):
  if b == 0:
    return 0
  if b % 2 == 0:
    return multiplicacion(a + a, b // 2)
  else:
    return a + multiplicacion(a + a, (b - 1) // 2)


print(multiplicacion(7, 5))  

# Análisis Big-O:

# Tiempo: \(O(\log b)\)

# Significa que el código es súper rápido porque reduce el problema a la mitad en cada paso.
# • Si \(b\) vale 8, solo hace 3 pasos (\(8 \rightarrow 4 \rightarrow 2 \rightarrow 1\)).
# • Si \(b\) fuera 1,000,000 (un millón), ¡solo necesitaría unos 20 pasos para terminar!
# • En resumen: El tiempo crece muy, muy lento aunque el número \(b\) sea gigante.

# Espacio: \(O(\log b)\)

# Como el código es recursivo, la computadora tiene que "recordar" cada paso que da guardándolo en una lista de tareas (la pila de llamadas).
# • Si el código da 3 pasos, la computadora guarda 3 notas en su memoria al mismo tiempo.
# • Si da 20 pasos, guarda 20 notas.
# • En resumen: La memoria que usa el programa es mínima, ya que solo necesita espacio para la cantidad de pasos que da (que ya vimos que son muy pocos).

#----------------------------------------------------------------------------------------------------------
def contar_vocales(cadena):
  if cadena == "":
    return 0
  es_vocal = 1 if cadena[0].lower() in "aeiouáéíóú" else 0
  
  return es_vocal + contar_vocales(cadena[1:])

print(contar_vocales("JefferLargaespada"))
#----------------------------------------------------------------------------------------------------------
def imprimir_patron(n):
  if n <= 0:
    return
  imprimir_patron(n - 1)
  print("*" * n)

imprimir_patron(30)

#----------------------------------------------------------------------------------------------------------
def caminos_tablero(n, m):
  if n == 1 or m == 1:
    return 1
  return caminos_tablero(n - 1, m) + caminos_tablero(n, m - 1)
print(caminos_tablero(3, 3)) 

#Análisis Big-O:

# Tiempo: \(O(2^{N+M})\) — El "Efecto Bola de Nieve"

# Esta eficiencia es muy lenta y costosa para la computadora. ¿Por qué?
# • La bifurcación: En el primer paso, tienes 2 opciones. En el siguiente, cada una de esas 2 opciones te da otras 2 opciones más (ya van 4 caminos). En el siguiente paso, se convierten en 8, luego en 16, luego en 32...
# • El problema de la amnesia: Como el código "no tiene memorización" (no tiene memoria), es un poco despistado. Si dos caminos diferentes lo llevan a la misma casilla, el código vuelve a calcular todo desde cero como si nunca hubiera estado ahí.
# • En resumen: El número de operaciones se duplica con cada paso que agregas. Si el tablero es un poco grande, la computadora se quedará atrapada calculando millones de caminos repetidos y tardará una eternidad.

# Espacio: \(O(N + M)\) — La "Cuerda de Seguridad"

# A pesar de que el código calcula muchísimos caminos en total, la memoria que usa al mismo tiempo es muy baja y eficiente.
# • El truco de la pila: La computadora no revisa todos los caminos a la vez. Lo que hace es agarrar un solo camino directo desde el inicio hasta el final (como si fuera una línea de hormigas).
# • La longitud del camino: Para cruzar el tablero de esquina a esquina, el camino más largo posible en línea recta mide exactamente lo que miden tus filas más tus columnas (\(N + M\)).
# • Una vez que ese camino termina y da una respuesta, la computadora lo "borra" de su mente y pasa a revisar el siguiente.
# • En resumen: La computadora solo necesita recordar la ruta en la que está parada en ese preciso momento. Nunca guarda todo el árbol de caminos a la vez, por lo que consume muy poca memoria.


#----------------------------------------------------------------------------------------------------------

def flatten(lista):
  if not lista:
    return []
  primero = lista[0]
  resto = lista[1:]
  if isinstance(primero, list):
    return flatten(primero) + flatten(resto)
  else:
    return [primero] + flatten(resto)
anidada = [1, [2, [3, 4], 5]]
print(flatten(anidada))
