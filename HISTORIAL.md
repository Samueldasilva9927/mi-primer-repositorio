# HISTORIAL — Clase06_Ejercicio28

## 2026-11-26 — Clonar `mi-primer-repositorio` con usuario y correo dados

- **Pedimos:** Instalar Git (si faltaba) y clonar
  `https://github.com/Samueldasilva9927/mi-primer-repositorio.git` en
  `C:\IAGenerativa\Clase06_Ejercicio28`, configurando el usuario
  `Samueldasilva9927` y el correo `esamueldasilva9@gmail.com` del punto a.
  En el pedido original esos dos datos estaban como marcadores
  (`PONÉ ACÁ TU USUARIO DEL PUNTO a` / `PONÉ ACÁ TU CORREO DEL PUNTO a`); se
  pidieron los valores reales y el usuario los confirmó.
- **Hicimos:** Verifiqué que Git no estaba instalado y lo instalé con
  `winget install --id Git.Git` (versión 2.56.1). Configuré
  `git config --global user.name` y `user.email` con los datos recibidos y
  cloné el repo en la carpeta pedida. Verificación: `origin` apunta a la URL
  indicada, rama `main` sin cambios locales, último commit
  `af244d7` de Samueldasilva9927 <esamueldasilva9@gmail.com>, contenido
  `README.md` (23 bytes) más `.git/`.
- **Falta:** Nada.

## 2026-11-26 — Configurar Git localmente en el repositorio

- **Pedimos:** Configurar Git dentro de la carpeta del repositorio con el
  nombre `samueldasilva9927` y el correo `esamueldasilva9@gmail.com`.
- **Hicimos:** Ejecuté `git config --local user.name 'samueldasilva9927'` y
  `git config --local user.email 'esamueldasilva9@gmail.com'` dentro de
  `C:\IAGenerativa\Clase06_Ejercicio28`. Verifiqué con `git config --local
  --list` y con `git config user.name` / `user.email`: ambos devuelven los
  valores pedidos (la configuración local tiene prioridad sobre la global,
  que tenía el nombre con mayúscula inicial). El `status` sigue en `main`
  sincronizada con `origin/main`; el único archivo sin seguimiento es este
  `HISTORIAL.md`, creado por la regla del workspace.
- **Falta:** Nada.

## 2026-11-26 — Guardar las reglas de Git en AGENTS.md

- **Pedimos:** Dejar en `AGENTS.md` de esta carpeta las acciones ante tres
  frases: «subí los cambios» → commit con mensaje descriptivo y push;
  «bajá los cambios» → `git pull`; «guardá una versión» → solo commit.
  Siempre sobre el repositorio de esta carpeta.
- **Hicimos:** Creé `AGENTS.md` en la raíz del repo con una tabla de frases
  disparadoras, la indicación de trabajar siempre en
  `C:\IAGenerativa\Clase06_Ejercicio28`, y notas sobre revisar `git status`,
  mensajes de commit concretos y avisar si no hay cambios. No hice commit ni
  push: el pedido fue solo guardar las instrucciones.
- **Falta:** Nada.

## 2026-11-26 — Word con los datos personales

- **Pedimos:** Crear en la carpeta del repositorio un archivo Word con
  nombre Samuel da silva, DNI 43331509, correo electrónico y usuario
  `samueldasilva9927`.
- **Hicimos:** Dejé `crear_datos_word.py` (con `python-docx`) y generé
  `mis_datos.docx`: título «Mis datos» y una tabla de 4 filas con las etiquetas
  en negrita. Verifiqué releyendo el documento que las 4 celdas tengan los
  valores correctos. El correo se escribió `esamueldasilva9@gmail.com` (con
  `@`, tal como se confirmó en el punto a); en el pedido llegó sin la `@`.
  No se hizo commit ni push.
- **Falta:** Confirmar si se quiere el correo exactamente como se escribió en
  el pedido (sin `@`), en cuyo caso se corrige el documento.

## 2026-11-26 — Subir los cambios al repositorio

- **Pedimos:** «subí los cambios al repositorio». Según `AGENTS.md`, eso implica
  commit con mensaje que explique el cambio y luego push.
- **Hicimos:** Revisé `git status` (4 archivos nuevos: `AGENTS.md`,
  `HISTORIAL.md`, `crear_datos_word.py`, `mis_datos.docx`), hice
  `git add` + `git commit -m 'Agrega reglas de Git, documento con datos
  personales e historial de tareas'` (commit `e815e56`) y
  `git push origin main`: `af244d7..e815e56  main -> main`. Después agregué
  esta entrada al historial y la subí en un commit de registro.
- **Falta:** Nada.

## 2026-11-26 — Ampliar el Word con carrera, domicilio y provincia

- **Pedimos:** Agregar al Word los datos carrera `contador publico`, domicilio
  `alpatauca 1810` y provincia `catamarca`.
- **Hicimos:** Actualicé la lista `DATOS` en `crear_datos_word.py` y regeneré
  `mis_datos.docx`, que ahora tiene 7 filas. Verifiqué por relectura que las
  7 celdas muestren los valores pedidos, respetando la escritura literal del
  usuario (sin tildes ni mayúsculas corregidas). No se hizo commit ni push.
- **Falta:** Nada.

## 2026-11-26 — Actualizar el repositorio con los cambios del Word

- **Pedimos:** «actualiza el repositorio»: bajar posibles cambios remotos y
  subir los cambios locales pendientes del documento.
- **Hicimos:** `git pull origin main` indicó «Already up to date». Commiteé
  `crear_datos_word.py`, `mis_datos.docx` y este historial con un mensaje que
  describe el cambio, y luego hice push a `origin/main`.
- **Falta:** Nada.
