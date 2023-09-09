notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}


def promedioEstudiantes(notas_estudiantes):
    total=0
    
    for valor in notas_estudiantes:
        total += valor['Juan']+valor['Maria']+valor['Pedro']
        
    return total

cantidad_elementos = len(notas_estudiantes)
promedio = promedioEstudiantes(notas_estudiantes) / cantidad_elementos
print(f"El promedio es {promedio}")





