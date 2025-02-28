import json

class PerfilCandidato:
    """Clase base que representa un perfil de candidato genérico."""
    
    def __init__(self, nombre, experiencia, habilidades):
        self.nombre = nombre
        self.experiencia = experiencia  # Años de experiencia
        self.habilidades = habilidades  # Lista de habilidades técnicas

    def mostrar_info(self):
        return f"Candidato: {self.nombre}, Experiencia: {self.experiencia} años, Habilidades: {', '.join(self.habilidades)}"


class Desarrollador(PerfilCandidato):
    """Candidato desarrollador con lenguaje de programación principal."""
    
    def __init__(self, nombre, experiencia, habilidades, lenguaje):
        super().__init__(nombre, experiencia, habilidades)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        return f"[DEV] {super().mostrar_info()}, Lenguaje: {self.lenguaje}"


class Gerente(PerfilCandidato):
    """Candidato gerente con experiencia en gestión de equipos."""
    
    def __init__(self, nombre, experiencia, habilidades, equipo_dirigido):
        super().__init__(nombre, experiencia, habilidades)
        self.equipo_dirigido = equipo_dirigido  # Número de personas dirigidas

    def mostrar_info(self):
        return f"[GERENTE] {super().mostrar_info()}, Equipo dirigido: {self.equipo_dirigido} personas"


class Vacante:
    """Define una vacante con requisitos específicos."""
    
    def __init__(self, titulo, experiencia_requerida, habilidades_requeridas):
        self.titulo = titulo
        self.experiencia_requerida = experiencia_requerida
        self.habilidades_requeridas = habilidades_requeridas

    def mostrar_info(self):
        return f"Vacante: {self.titulo}, Experiencia requerida: {self.experiencia_requerida} años, Habilidades: {', '.join(self.habilidades_requeridas)}"


class Reclutador:
    """Clase que analiza perfiles y decide si un candidato es adecuado para una vacante."""
    
    @staticmethod
    def evaluar_candidato(candidato, vacante):
        experiencia_valida = candidato.experiencia >= vacante.experiencia_requerida
        habilidades_validadas = set(vacante.habilidades_requeridas).issubset(set(candidato.habilidades))
        
        if experiencia_valida and habilidades_validadas:
            return f"✅ {candidato.nombre} es adecuado para la vacante {vacante.titulo}."
        else:
            return f"❌ {candidato.nombre} NO cumple con los requisitos de {vacante.titulo}."


def main():
    """
    Función principal que ejecuta la evaluación de candidatos para vacantes específicas.
    """
    # Simulación de perfiles JSON (como si fueran recibidos de un sistema externo)
    json_perfiles = '''
    [
        {"tipo": "Desarrollador", "nombre": "Ana", "experiencia": 5, "habilidades": ["Python", "Django", "SQL"], "lenguaje": "Python"},
        {"tipo": "Gerente", "nombre": "Luis", "experiencia": 8, "habilidades": ["Liderazgo", "Gestión de equipos", "Scrum"], "equipo_dirigido": 10}
    ]
    '''

    # Convertimos el JSON a objetos Python
    perfiles_data = json.loads(json_perfiles)
    candidatos = []

    # Creación dinámica de objetos según el tipo de perfil
    for perfil in perfiles_data:
        if perfil["tipo"] == "Desarrollador":
            candidatos.append(Desarrollador(perfil["nombre"], perfil["experiencia"], perfil["habilidades"], perfil["lenguaje"]))
        elif perfil["tipo"] == "Gerente":
            candidatos.append(Gerente(perfil["nombre"], perfil["experiencia"], perfil["habilidades"], perfil["equipo_dirigido"]))

    # Definimos una vacante de ejemplo
    vacante_dev = Vacante("Desarrollador Backend", 4, ["Python", "Django", "SQL"])
    vacante_gerente = Vacante("Gerente de Proyectos", 5, ["Liderazgo", "Scrum"])

    # Evaluamos candidatos para cada vacante
    for candidato in candidatos:
        print(candidato.mostrar_info())
        if isinstance(candidato, Desarrollador):
            print(Reclutador.evaluar_candidato(candidato, vacante_dev))
        elif isinstance(candidato, Gerente):
            print(Reclutador.evaluar_candidato(candidato, vacante_gerente))
        print("-" * 50)


if __name__ == "__main__":
    main()