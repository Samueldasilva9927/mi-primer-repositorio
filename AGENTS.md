# AGENTS.md — Clase06_Ejercicio28

Todas las operaciones de Git se hacen **siempre sobre el repositorio de esta
carpeta** (`C:\IAGenerativa\Clase06_Ejercicio28`). Ejecutar los comandos con
esta carpeta como directorio de trabajo (o con `git -C C:\IAGenerativa\Clase06_Ejercicio28 ...`).

## Frases disparadoras

| Pedido del usuario | Acción |
|---|---|
| «subí los cambios» | Hacer `git add` de los cambios correspondientes y `git commit` con un mensaje que explique **qué cambió** (no mensajes genéricos como "update"); después `git push`. |
| «bajá los cambios» | Ejecutar `git pull`. |
| «guardá una versión» | Hacer solo `git add` + `git commit` con mensaje descriptivo. **No** hacer `push`. |

## Notas

- El mensaje de commit debe describir el cambio concreto, en español, por
  ejemplo: `Agrega instrucciones de Git en AGENTS.md`.
- Antes de commitear, revisar `git status` para saber qué archivos entran.
- Si no hay cambios para commitear, avisar en lugar de inventar un commit.
- Al terminar cada tarea, registrar qué pedimos / qué hicimos / qué falta en
  `HISTORIAL.md` de esta carpeta, según la regla del workspace.
