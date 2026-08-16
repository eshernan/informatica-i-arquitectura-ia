# Modelo de software vs. arquitectura de software 

Diseño 1 

Diseño y Modelado del Sistema 1. Diseño - qué es Diseño y Especificación de Requerimientos Descomposición - Enfoques 

2. Arquitectura (distintos estilos) 

3. Técnicas y Herramientas 

4. Características de un buen diseño 

5. Documentación 

Diseño 2 

# 1. Diseño - qué es 

- Significado: 

   - **Proceso** por el que se genera una solución a un problema 

   - **Descripción** de la solución 



<!-- Start of picture text -->
Diseño 1<br>Requeri-<br>Diseño 2<br>mientos<br>...<br>Diseño n<br>Restricciones<br><!-- End of picture text -->

Distintos Diseños (Alternativas) permiten cumplir con los requerimientos, pero cada uno ofrece prestaciones específicas 

Diseño 3 

### Diseño y Especificación de Requerimientos(1) 

QUÉ CÓMO DISEÑO DISEÑO CONCEPTUAL TÉCNICO Diseñadores forma función del Sistema Constructores Clientes del Sistema 

Diseño 4 

### Diseño y Especificación de Requerimientos(2) 

“El usuario podrá enviar mensajes a cualquier usuario en cualquier otra computadora en red” DISEÑO CONCEPTUAL 



Topología de Red Protocolo Velocidad (bps) . . . 

DISEÑO TÉCNICO 

Diseño 5 

### Descomposición y Modularidad 

- e 

- Determinar un conjunto de componentes <u>interfaces entre ellos, que satisfacen un conjunto</u> especificado de requerimientos (De Marco 1982) 

- Métodos de descomposición (Wasserman 1995) * **Modular** (a partir de las **funciones** ) 

   - A partir de los **Datos** 

   - A partir de **Eventos** (y transiciones de **Estados** ) 

   - A partir de las **Entradas** (de afuera hacia adentro) 

   - Orientado a **Objetos** 

- <u>Sistema Modular: cuando cada una de las actividades la realiza</u> exactamente un único componente donde además están bien definidas c/u de sus entradas y salidas. 

Diseño 6 

### Proceso de Descomposición 



###### Nivel Superior 





Primer Nivel de descomposición Segundo Nivel de descomposición 

Diseño 7 

### Niveles de Diseño 



• (1) Arquitectura: => Requerimientos componentes del sistema sus interconexiones y • (2) Diseño del Código: => Módulos algoritmos y estructuras de datos • (3) Diseño de la Ejecución: => Algoritmos (código) asignación de memoria, tiempo de ejecución, optimizaciones de código **ENFOQUE:** trabajar desde lo general a lo particular 

Diseño 8 

### (Sommerville) Proceso genérico de Diseño 



<!-- Start of picture text -->
NIVEL 1<br>Diseño<br>Arquitectónico<br>Especificación<br>subsistemas<br>NIVEL 2<br>Diseño<br>elementos<br>Especificación<br>interfaces<br>Diseño<br>estructuras<br>de datos<br>Diseño<br>algoritmos<br>NIVEL 3: se realiza sobre el nivel 2<br><!-- End of picture text -->

Diseño 9 

# 2. Arquitectura (1) 

: **Definición, estilos y evaluación** 

- **Primer nivel** de descomposición, que muestra como se organiza el sistema en términos de sus componentes y las interacciones entre ellos. 

- **Cambiar** la **Arquitectura** de un producto ya construido en general exige mucho **esfuerzo** 

   - **=> Evaluación de Arquitecturas** 

- Distintos “ **estilos** ” que definen familias de sistemas en términos de patrones de organización estructural. 

- Un **estilo de arquitectura** implica sus componentes, conectores y exigencias al combinarlos. 

- Identificarlos y caracterizarlos para facilitar la **comunicación entre diseñadores** 

Diseño 10 

# 2. Arquitectura (2) 

: **Influencia y características** 

- Sus características **condicionan** las características del **producto final** (escalabilidad, capacidad, desempeño, consistencia, mantenibilidad, compatibilidad, etc.) 

- Estilo y estructura particular elegidos pueden depender de : 

- **Requerimientos No Funcionales** 

- **1 - Desempeño:** localizar operaciones críticas en un número reducido de . 

- subsistemas con poca comunicación. Componentes de **grano grueso** 

- **2 - Seguridad:** estructurar en capas con los recursos más críticos protegidos por las capas más internas con alto nivel de validación. 

- **3 - Mantenibilidad:** componentes autocontenidos que puedan ser intercambiados con facilidad, evitando estructuras de datos compartidas. Componentes de . 

- **grano fino** 

**<u>CONFLICTO DE INTERESES:</u>** entre los requerimientos 1 y 3, si se tienen ambos se deberá buscar una solución intermedia. 

Diseño 11 

# 2. Arquitectura (3) 

###### : **Elementos para la documentación** 

- salida del 

- **SAD (Software Architecture Description)** proceso de diseño de arquitectura, donde se incluyen modelos gráficos qu ~~e muestran perspectiva~~ s distintas del sistema y descripciones textuales. 

- **Documentarla** para que pueda ser utilizada y mantenida por otros, con suficiente detalle, sin ambiguedades ni repeticiones, registrando decisiones tomadas. 

- **Notaciones: UML** general, accesible. 

   - **ADL’s (** Lenguaje de Descripción de 

   - Arquitectura **)** formales, para expertos. 

- **Complejidad** se maneja documentando diferentes **<u>vistas</u>** de la arq., proyección en una dimensión mostrada desde una perspectiva, sin tener en cuenta entidades no relevantes a esa perspectiva. “ ” ’ 

- • <u>The 4+1 View Model of Software Architecture – Kruchten 95</u> Vistas definidas: lógica, procesos, implementación, física y CU (Casos de Uso). Todas son guiadas por los CU (o escenarios) significativos a la arquitectura 

Diseño 12 

# 2. Arquitectura (4) 

: **Beneficios esperados de prestarle atención** 

- Mejorar la **comunicación** entre los **distintos interesados** : 

   - Cliente – diseñadores 

   - Diseñadores – desarrolladores 

- Clarificar **intenciones de diseño** 

   - la arquitectura concebida a menudo se pierde, comunicación en gral. informal (difícil) 

- Proporcionar bases para **análisis del diseño** 

   - predecir desempeño y otras características y ajustar el diseño como tarea rutinaria 

- Mejorar el **mantenimiento** 

   - gran parte del esfuerzo de mantenimiento se dedica a entender 

- Identificar **cuestiones interesantes** 

   - incluso careciendo de métodos formales 

Diseño 13 

# 2. Arquitectura (5) 

: **Métodos para evaluación de arquitecturas** 

- Analizar la arquitectura para ver si cumple requisitos de calidad establecidos (ej. confiabilidad, interoperabilidad) 

- Preferible realizar evaluaciones tempranas que permitan introducir cambios con menor impacto y mejorar los aspectos de riesgo identificados 

- Evaluaciones a posteriori resultan útiles como forma de aprendizaje y estudio de posibilidades de mejora, por ej. para una nueva versión del producto 

- Software Engineering Institute (SEI) propone: 

   - Architecture Tradeoff Analysis Method (ATAM) 

   - Software Architecture Analysis Method (SAAM) 

Diseño 14 

|Diseño:|Arquitectura v|s. Programas|
|---|---|---|
||**Arquitectura**|**Programas**|
|**Muestra**|Interacciones entre<br>partes|Implementaciones de<br>partes|
|**Considera**|Propiedades<br>estructurales|Propiedades<br>computacionales|
|**Análisis**|En general estático|En general dinámico|
|**Evaluación**|Desempeño a nivel<br>del Sistema|Desempeño de<br>algoritmos|
|**Visión**|Fuera de los límites de<br>módulo|Dentro de los límites<br>de módulo|
|**Reutilización**|Composición de<br>subsistemas|Copia de código o<br>llamado a bibliotecas|



Diseño 15 

### Arquitectura–Estilos (Garlan&Shaw, Sommerville,otros) **1. Flujo de Datos** 

- Secuencial por lotes / Tubos y Filtros/ Circuitos de Control 

- **2. Llamada y Retorno** 

- Programa Principal y subrutinas / Orientada a Objetos 

- **3. Componentes Independientes** 

- Procesos que se comunican / Invocación implícita (Eventos) 

- **4. Centrado en los Datos (repositorios)** 

   - Bases de Datos / Pizarrones (Blackboards) 

**5. Máquinas Virtuales** 

- Intérpretes / Capas Jerárquicas 

- **6. Específicas del Dominio de Aplicación** 

- Modelos genéricos / Modelos de referencia 

- **7. Distribuidas** 

- Cliente-Servidor/ Objetos Dists. / Dist. Procesos, datos / SOAs 

- **8. Microservicios 9. Event Driver** 

**10. Capas 11. Cloud** 

Diseño 16 

### 1 - Flujo de Datos 

###### **Caracterizadas por:** 

- La disponibilidad de los **datos** controla la **ejecución** 

- La estructura del **diseño** está dominada por el **movimiento** ordenado de los **datos** de un componente a otro 

- El **patrón** del flujo de datos es **explícito** 

- En un sistema puro **no** hay otra **interacción** entre procesos 

- **Ejemplos:** 

- Secuencial por lotes (dominada por actualización de BD) 

- Tubos y Filtros - Filtros conectados en un grafo de flujo de datos 

- Circuitos de Control de Procesos 

Diseño 17 

### Tubos y Filtros (1) **Características:** 

- Por los tubos fluyen datos, transmisión de salidas de un filtro a la entrada de otro 

- Cada filtro admite una o varias entradas (tubos) y una o varias salidas (tubos) 

- Cada filtro es independiente del resto y no conocen la identidad de los filtros antes y después de él 

- La transformación del filtro puede comenzar antes de terminar de leer la entrada (distinto al proceso por lotes) 

- Respetando el grafo, no importa la secuencia (paralelismo) 

###### **Ejemplo:** pipelines (Unix) 

##### Tubo 

##### Filtro 





Diseño 18 

### Tubos y Filtros (2) 

###### **Bondades:** 

- **Fácil comprender** el comportamiento total de entrada/salida del sistema a partir de los efectos de cada filtro 

   - (entrada->transformación->salida) 

- **Permite reutilización** (simplicidad de interfaces, filtros reutilizables) 

- **Fácil evolución y mantenimiento** (agregar, sustituir, eliminar filtros) 

- **Permite evaluar desempeño** (independencia de filtros) 

- Permite **ejecución en paralelo** 

###### **Limitaciones:** 

- Orientado a procesamiento por lotes ( **no interactivo** ) 

- Necesidad de **consistencia entre flujos** de datos 

- La independencia entre filtros puede acarrear la repetición de procesos de preparación ( **ineficiencias** ) 

   - (ej. validaciones) 

Diseño 19 

### Circuitos de Control (de Procesos) (1) 

###### **Propósito:** 

- Proveer control dinámico de un entorno físico. Ej. sist. acond. ambiental 

- Mantener propiedades específicas de las **salidas del proceso** dentro o cerca de valores de referencia indicados ( **puntos fijos o referencias** ) 

- **Elementos a considerar:** 

- Variables a monitorear, sensores a utilizar, su calibración, temporización tanto del sensado como del control. 

- **Clasificación:** 

- **Bucle con retroalimentación (feedback loop)** 

   - Mide la variable controlada y ajusta el proceso para mantener el valor cerca o dentro de la referencia. 

- **Bucle con prealimentación o anticipador (feedforward loop)** 

   - Mide otras variables del proceso que actúan como indicadores e intenta anticipar los futuros efectos sobre la variable controlada. 

Diseño 20 

### Circuitos de Control (de Procesos) (2) Bucle con **retroalimentación** (feedback loop): 

<u>variables de Entrada</u> Proceso Controlad ~~or~~ Punto de Cambios en las fijación variables manipuladas 

Variable Controlada 

##### Bucle **anticipador** (feedforward loop): variables de Entrada 

Proceso Variable Controlada 

Controla ~~dor~~ Cambios en las Punto de fijación 

variables manipuladas 

Diseño 21 

### Flujo de Control vs. Flujo de Datos 

- Flujo de **Control** : 

   - La cuestión **dominante** es cómo se mueve el **control** a través del 

      - programa 

   - los **datos** pueden acompañar el control pero **no son dominantes** 

   - el razonamiento se refiere al **orden de ejecución** 

- Flujo de **Datos** : 

   - La cuestión **dominante** es cómo los **datos** se mueven a través de un conjunto de procesos atómicos 

   - a medida que se mueven los **datos** se **activa el control** 

   - el razonamiento se refiere a la **disponibilidad de los datos** , su **transformación** , las **demoras** 

Diseño 22 

### 2 - Llamada y retorno 

- **Programa Principal y Subrutinas:** 

   - Descomposición Funcional tradicional 

- **Orientada a Objetos** (tipos abstractos de datos) 

   - Ocultamiento de Información, especialmente de representaciones 

- **Otros** 

   - Capas Jerárquicas 

   - Sistemas Cliente/Servidor 

   - Remote Procedure Call 

Diseño 23 

### Programa Principal y Subrutinas (1) 

###### • **Características:** 

###### • **Descomposición jerárquica:** 

   - basada en la relación “usa” 

- **Único Hilo de Control (Thread of Control)** 

   - soportado directamente por los lenguajes de programación 

- **Estructura de subsistemas implícita** 

   - subrutinas agregadas en un módulo 

- **Razonamiento jerárquico:** * que una subrutina sea correcta depende de que sean correctas las subrutinas llamadas 

###### • **Bondades:** 

   - Permite analizar los flujos de control y saber como responderá el sistema a cierto tipo de entradas 

- **Limitaciones:** Manejo de excepciones 

Diseño 24 

### Programa Principal y Subrutinas (2) 



<!-- Start of picture text -->
Principal<br>Subr. A Subr.B Subr.C<br><!-- End of picture text -->

Subsistema 

###### Llamado/Retorno 

Diseño 25 

### Orientada a Objetos (1) 

###### **Caracterizada por:** 

- La solución está compuesta por un conjunto de agentes que interactúan 

- Representación de datos y operaciones asociadas se encapsulan en un objeto o TAD. 

- Herencia, Polimorfismo, Sobrecarga de operadores, enlace dinámico 

- **Bondades:** 

- Facilita el Mantenimiento (localización de impacto) 

- Promueve la reutilización de componentes 

- Permite cambiar la implementación de un objeto sin afectar al resto 

- **Limitaciones:** 

- Un objeto debe conocer las interfaces de aquellos que utiliza 

- Si se cambia una interfaz, se afectan todos los que la utilizan 

Diseño 26 

### Orientada a Objetos (2) 







Objeto Llamado 











Diseño 27 

### 3 - Componentes Independientes 

- **Procesos que se comunican** 

   - Pasan mensajes a los participantes **conocidos** 

- **Sistemas guiados por eventos** 

   - Invocación implícita de participantes **desconocidos** 

- **Otros** 

   - Envíos de mensajes múltiples con enlace dinámico 

   - Procesos guiados por interrupciones 

Controlador de interrupciones pasa el control a algún componente para su procesamiento 

Diseño 28 

### Procesos que se comunican (1) 

**Características:** 

- Muestra al sistema como un conjunto de unidades ejecutando concurrentemente y sus interacciones. 

- **Componentes:** procesos independientes 

   - típicamente implementados como tareas independientes 

- **Conectados por:** <u>mensajes</u> 

   - punto a punto 

   - asincrónicos y sincrónicos 

   - RPC y otros protocolos se pueden construir encima 

- **Ejemplos:** 

- procesos que monitorean ejecución de otros procesos. 

Diseño 29 

### Procesos que se comunican (2) 











Proceso Mensaje 







Diseño 30 

### Invocación Implícita (guiada por eventos) 

###### **Caracterizada por:** 

- Se registran procedimientos para los eventos 

- Un componente **comunica** un **evento** 

- Cuando se anuncia un **evento** los procedimientos asociados son invocados implícitamente 

- El orden de invocación es no determinista 

- **Bondades:** 

- Facilita la **reutilización** de componentes 

- Fácil cambiar los componentes que atienden un evento 

- **Limitaciones:** 

- No hay garantías respecto a qué va a pasar frente a un evento (quién responderá ni en que orden se dará la ejecución) 

- Limitaciones en la verificación (comprobar correctitud debido a dependencia del contexto y secuencia de eventos) 

###### **Ejemplos:** 

- Depurador de programas que invoca uno u otro editor 

Diseño 31 

### 4 - Centrados en los datos (repositorios) 

###### **Caracterizada por:** 

   - Hay un almacenamiento central de datos y un conjunto de componentes que operan sobre éste. 

- **Bases de Datos transaccionales** 

   - gran almacén de datos central 

   - orden de operación determinado por la entrada de datos 

- **Pizarrón (blackboard)** 

   - representación central compartida adecuada a una aplicación 

   - orden de operación determinado por estado actual de la estructura central 

###### • **Otros** 

- Herramientas CASE 

- Sistemas integrados de diseño 

Diseño 32 

### Pizarrón (Blackboard) (1) 

- **Fuentes de Conocimiento** 

   - Procesos independientes que corresponden a particiones del conocimiento del mundo y del dominio dependientes de la aplicación 

   - Responden a cambios en el pizarrón 

- **Estructura de datos del Pizarrón** 

   - Estado completo de la solución del problema 

   - Jerarquía de datos de estado para resolver el problema 

   - único medio por el cual las Fuentes de conocimiento interactúan para llegar a la solución 

###### • **Control** 

- Guíado enteramente por el estado del pizarrón 

- Las Fuentes de conocimiento (FC) responden oportunamente cuando los cambios en el pizarrón aplican 

- Puede implementarse en las FC, en el pizarrón, en un componente separado o cualquier combinación de éstos. 

Diseño 33 

### Pizarrón (2) 



<!-- Start of picture text -->
Memoria (Compartida)<br>FC 2<br>FC 1 FC 3<br>Pizarrón<br>FC 7<br>FC 4<br>FC 5<br>FC 6<br>Cálculos<br><!-- End of picture text -->

Diseño 34 

### 5 - Máquinas Virtuales 

- **Intérpretes:** 

   - crean una máquina virtual cuando no se dispone de la que se desea 

- **Capas Jerárquicas:** 

   - cada capa constituye una máquina virtual que provee servicios a las otras capas 

- **Otros:** 

   - Sistemas basados en Reglas 

      - ° tipo especial de intérpretes 

   - procesadores de lenguaje de comandos 

   - shells 

Diseño 35 

### Intérpretes (1) 

**Características:** 

- **procesador emulado por software** 

- **datos** 

   - representación del programa que se interpreta 

   - estado del programa que se interpreta 

   - estado interno del intérprete 

- El **control** reside en el ciclo de ejecución del intérprete 

Diseño 36 

###### Intérpretes (2) 



<!-- Start of picture text -->
Memoria Programa<br>siendo<br>entradas<br>interpretado<br>Datos<br>(estado del<br>programa)<br>Máquina de estado<br>de la ejecución<br>salidas Motor de  Instrucción seleccionada Estado<br>interpretación interno del<br>simulada interprete<br>Datos seleccionados<br>Acceso a datos<br>Recuperar/Almacenar<br><!-- End of picture text -->

Diseño 37 

### Capas Jerárquicas (1) **Caracterizada por:** 

- Hay diversas capas, cada una **provee un conjunto de servicios** a las capas superiores y **requiere servicios** de las inferiores. 

- **Modelo estricto: el acceso a servicios de otras capas está limitado,** una capa sólo utiliza servicios de la inmediata inferior, y ofrece servicios . 

- a la inmediata superior. Sino **Modelo relajado** 

- Definición de protocolos mediante los que interactúan las capas 

- **Bondades:** 

- Facilita **la comprensión** (basado en niveles de abstracción) 

- Facilita **mantenimiento** (posible modificar una capa sin afectar al resto) 

- • Facilita **reutilización** 

- Facilita **portabilidad** 

###### **Limitaciones:** 

- No siempre es fácil estructurar en capas ni identificar los niveles de abstracción a partir de los Requerimientos 

- Puede afectar el desempeño la coordinación entre los niveles 

Diseño 38 

### Capas Jerárquicas (2) 

##### Criptografía Interfaces de Archivos Gestión de Claves Autenticación 

Ejemplo: Capas de Sistema de Seguridad 

##### Usuarios 

Diseño 39 

#### 6 – Específicas del dominio de aplicación 

- Modelos específicos para un dominio de aplicación particular 

- **Modelos genéricos:** 

   - Abstracciones de sistemas existentes que encapsulan las características principales de los mismos. A menudo representan la arq. común de una familia de aplicaciones (línea de productos). Ejs. Módulos que se deben incluir en un compilador 

- **Modelos de referencia:** 

   - Modelos abstractos idealizados derivados de un estudio del dominio de aplicación. Proveen información sobre la estructura general del sistema y actúan como estándar contra el cual evaluar sistemas. Ejs. Modelo de capas OSI para sists. de comunicación 

Diseño 40 

### 7 – Distribuidas 

###### • **Cliente-Servidor:** 

   - servicios provistos por los servidores y requeridos por los clientes 

- **Objetos Distribuidos:** 

   - objetos brindan y requieren servicios de otros objetos 

- **Service Oriented Architecture (SOA):** 

   - composición de servicios (ej. web-services) 

- **Distribución de:** 

   - Datos (centralizados, distribuidos, replicados) 

   - Procesos (fija, variable) 

- **Comunicación:** 

   - Remote Procedure Call 

   - Pasaje de mensajes 

Diseño 41 

### 7 – Distribuidas 

**Características:** 

- El procesamiento de la info es distribuído sobre varias computadoras (procesadores)  conectados por una red 

- se requiere cierto software de “middleware” para administrar las partes y asegurar comunicación e intercambio de datos 

- el “middleware” es un software de propósito gral. que por lo regular se vende comercialmente, y actúa como mediador entre las partes 

- categorías de “middleware”: monitor transaccional (TPM), remote procedure call (RPC), message oriented mid.(MOM), distributed object mid., database access mid. 

###### **Bondades:** 

- Compartición de recursos, apertura, concurrencia, escalabilidad, tolerancia a fallas, transparencia. 

**Limitaciones:** 

- complejidad, seguridad, difíciles de gestionar, poco predecibles 

Diseño 42 

### Cliente - Servidor 

###### **Caracterizada por:** 

- hay un conjunto de servicios provistos por los servidores y un conjunto <u>de clientes</u> . que requieren esos servicios 

- Los clientes conocen a los servidores pero no a otros clientes y los servidores no tienen porque conocer a los clientes 

- tanto los clientes como los servidores son <u>procesos lógicos</u> 

- la asignación de procesos a procesadores no tiene porqué ser 1:1 

- **Ejemplo:** 



<!-- Start of picture text -->
c1 c2 c3, c4<br>CC1 CC2 CC3<br>Network<br>s1, s2 s3, s4 Server<br>computer<br>SC2 SC1<br>Client<br>computer<br>c5, c6, c7 c8, c9 c10, c11, c12<br>CC4 CC5 CC6<br><!-- End of picture text -->

C = clientes i 

S = servidores i 

Diseño 43 

### Cliente - Servidor en 2 niveles 

- Organización más simple de la distribución C/S, un conjunto de clientes y un servidor (o varios servidores idénticos): 

###### • **CLIENTE FINO:** 

   - el procesamiento de la aplicación y manejo de los datos se hace en <u>el servidor. El software en el cliente implementa solo la presentación</u> 

   - * Gran carga de procesamiento tanto en el servidor como en la red 

- **CLIENTE GRUESO:** 

   - <u>el servidor solo es responsable por el manejo de los datos. El</u> software en el cliente implementa la lógica de la aplicación y las <u>interacciones con el usuario.</u> 

   - Administración del sistema más compleja (actualizaciones) 

- Los applets descargables de Java permiten: 

   - Parte del software de procesamiento de la aplicación se descarga en el cliente como applets de Java, la interfaz de usuario se construye utilizando un navegador Web que los ejecuta 

Diseño 44 

### Cliente – Servidor en 3 y más niveles 

- **3 niveles:** 

   - Los procesos lógicos que tienen que ver con la presentación, lógica de aplicación y administración de datos pueden ser distribuídos en 3 sistemas de cómputo distintos. 

- **N niveles:** 

   - Se amplía la de 3 niveles agregando niveles según se requiera. Ej. aplicación que necesita acceder y utilizar datos de distintas fuentes (integración) 

###### **Bondades:** 

- Respecto a C/S en 2 niveles: son más escalables, se reduce el tráfico en la red (respecto a cliente fino), facilita la actualización del procesamiento de la aplicación (respecto a cliente grueso) 

Diseño 45 

### Objetos distribuidos 

###### **Características:** 

- No hay distinción entre clientes y servidores 

- Cada elemento distribuido es un objeto que provee servicios a otros objetos y requiere servicios de otros objetos. 

- Comunicación entre objetos es a través de un middleware llamado Object Request Broker (software bus) ej. CORBA 

- Más complejos de diseñar que los sistemas C/S 

###### **Ejemplo:** 



<!-- Start of picture text -->
o1 o2 o3 o4<br>S (o1) S (o2) S (o3) S (o4)<br>Software bus<br>o5 o6<br>S (o5) S (o6)<br><!-- End of picture text -->

Diseño 46 

### Service Oriented Architecture (SOA) **Características:** 

- Funcionalidades expuestas como servicios independientes mediante interfaces públicas bien definidas 

- Procesos del negocio se realizan estableciendo secuencias (coreografías) de invocación de éstas funcionalidades 

- Implementación con web-services brinda mayor interoperabilidad, utilización de protocolos estándares de comunicación e intercambio de información (SOAP, XML) 

**Funcionamiento gral.:** 



Diseño 47 

### Distribución de Datos 

**Motivación:** Costo de un acceso remoto en una red superrápida es aprox. 4 veces el costo de un acceso local. **Soluciones:** 

- **<u>Distribuir</u>** los datos en varias máquinas según cercanía a quienes más los acceden, el todo es la suma de las partes. 

- **<u>Replicar</u>** los datos en varias máquinas (caso extremo en cada una) de forma que los accesos sean mayormente locales. Se debe mantener consistencia de las copias 

Distribución de Procesos 

Puede ser estática o dinámica: 

**Estática** : está predefinido donde se ejecutará cada proceso 

**Dinámica** : la distribución de procesos se establece en tiempo de ejecución  permite migración de procesos 

Diseño 48 

### Comunicación 

**Remote Procedure Call:** 

- Llamada retorno entre módulos en distintas máquinas. 

- Aspectos a tener en cuenta: pasaje de parámetros (distintos espacios de memoria), manejo de excepciones. 

**Pasaje de mensajes:** 

- Cada módulo recibe mensajes de otros, los procesa y responde al módulo apropiado. 

- Aspectos a tener en cuenta: cantidad de mensajes que se pueden recibir. 

Ambos paradigmas son iguales en capacidades, uno puede simularse con el otro. RPC inherentemente sincrónico y pasaje de mensajes asincrónico. 

Diseño 49 



<!-- Start of picture text -->
Interfaz<br>de Usuario<br>Microservicio i Microservicio , Microsernicio yy Microservicio<br><!-- End of picture text -->

Base de Datos 

Base de Datos 

Base de Datos Base de Datos 

Tervaldes.com 

### 9 – Event-driven 

La arquitectura sin bloqueo (non-bloking) también se conoce como arquitectura reactiva o controlada por eventos(event-driven). Las arquitecturas basadas en eventos son bastante populares en los desarrollos modernos de aplicaciones web. 

Son capaces de manipular una gran cantidad de conexiones concurrentes con un consumo mínimo de recursos. Las aplicaciones modernas necesitan un modelo completamente asíncrono para escalar. Estos marcos web modernos proporcionan un comportamiento más confiable en un entorno distribuido. 

Diseño 51 



<!-- Start of picture text -->
io NN<br>Servicio A MMMY Logica de procesamientade eventos<br>Stream de eventos [eee]<br>Productores Consumidores<br>de eventos de eventos<br>fervaldes.com<br><!-- End of picture text -->

### 9 – En capas 

Este patrón se puede usar para estructurar programas que se pueden descomponer en grupos de subtareas, cada uno de los cuales se encuentra en un nivel particular de abstracción. Cada capa proporciona servicios a la siguiente capa superior. 

Las capas más comunes son: 

- Capa de presentación 

- Capa de aplicación 

- Capa de lógica de negocio 

- Capa de acceso a datos 

Diseño 53 

### 10 – Cloud 

Es la forma en que se organizan y conectan los servicios digitales (como servidores, redes y bases de datos) para crear programas seguros, rápidos y que pueden crecer sin gastar de más. 

La arquitectura de nube describe los métodos, tecnologías y marcos que utilizan los desarrolladores para diseñar aplicaciones en la nube. Esto incluye microservicios, API, contenedores y recursos que permiten implementar, mantener y escalar servicios en la nube. Puede pensar en la arquitectura de nube como un esquema que describe cómo interactúan las tecnologías de nube individuales. 

Diseño 54 

## ¿Cuántos capas debe tener la aplicación? 

Diseño 55 

Aplicación de una sola capa **_Pros:_** 

Sin latencia de red. 

Los datos están disponibles rápido y fácilmente Los datos no se transfieren a través de una red, lo que garantiza la seguridad de los datos. 

**_Contras:_** 

Poco control sobre la aplicación: es difícil implementar nuevas características o cambios de código una vez que se entrega. Las pruebas deben ser extremadamente exhaustivas con poco lugar para errores. 

Las aplicaciones de un solo nivel son vulnerables a modificaciones o ingeniería inversa. 

Diseño 56 

# Aplicación de dos capas 

###### **_Pros_** : 

Menos llamadas de red ya que el código y la interfaz de usuario están en la misma máquina 

El servidor de la base de datos y la lógica de negocio están físicamente cerca, ofreciendo un mayor rendimiento. 

###### **_Contras_** : 

Como el cliente posee la mayor parte de la lógica de la aplicación, surgen problemas para controlar la versión del software y redistribuir nuevas versiones. Carece de escalabilidad ya que solo admite un número limitado de usuarios. Cuando aumentan las solicitudes de varios clientes, el rendimiento de la aplicación puede disminuir debido a que los clientes necesitan más conexiones. Para procesar esta carga extra es necesario más memoria y CPU para responder. 

Dado que la lógica de la aplicación se combina con el cliente, es difícil reutilizar la lógica. 

Diseño 57 

# Aplicación de N capas 

**_Pros:_** Todas las ventajas de la arquitectura de tres niveles. El rendimiento aumenta, lo que le permite adaptarse a industrias de volumen medio a alto. **_Contras:_** 

Debido a la componentización de los niveles, la estructura es compleja y difícil de implementar o mantener. 

Diseño 58 

# Conclusión 

Elegir una arquitectura de una sola capa cuando no se desee ninguna latencia de red. 

Elegir una aplicación de dos capas cuando se necesite minimizar la latencia de la red y se necesite un mayor control de los datos dentro de la aplicación. 

Elegir una arquitectura de tres capas cuando se necesita control sobre el código/lógica de negocio de la aplicación, se quiere seguridad y control sobre los datos en la aplicación. Elegir una arquitectura de N capas cuando se necesite que la aplicación escale y maneje grandes cantidades de datos. 

Diseño 59 



<!-- Start of picture text -->
2 Core<br>16 GB<br><!-- End of picture text -->

Antes 



<!-- Start of picture text -->
4 Core<br>32 GB<br><!-- End of picture text -->

Después 

fervaldes,com 



<!-- Start of picture text -->
2 Core 2 Core 2 Core<br>16 GB 16 GB 16 GB<br>Antes Después<br><!-- End of picture text -->

fervaldes.com 

## Cuándo usar la arquitectura de microservicios 

La arquitectura de microservicios se ajusta mejor para casos de uso complejos y para aplicaciones que esperan que el tráfico aumente exponencialmente en el futuro, como una aplicación de red social o una plataforma de streaming. 

Una aplicación de red social típica tiene varios componentes, como mensajería, chat en tiempo real, transmisión de video en vivo, carga de imágenes, me gusta, compartir, etc. En este caso, es mejor desarrollar cada componente por separado, manteniendo presente la responsabilidad única y los principios de la separación de conceptos (separation of concerns). 

Diseño 62 

## 3. Técnicas y Herramientas 

- **Concurrencia** 

- **Interfaz de Usuario** 

- **Principios para guiar el Diseño** 

- **Modelo de Análisis de Jacobson** 

- **Tarjetas CRC** 

- **Diagramas UML** 

- **Patrones de Diseño** 

- **Marcos de trabajo (Frameworks)** 

- **Desarrollo basado en componentes** 

Diseño 63 

### **Procesos Concurrentes** 

- Control de Acceso a Recursos Compartidos * <u>Exclusión mutua (Prueba y Bloqueo en una</u> operación indivisible) 

- <u>Guardián (un “demonio” que acepta requerimientos</u> si el recurso está disponible) 

- * <u>Monitores (un objeto abstracto que exporta</u> servicios garantizando exclusión) 

- • Tiempo Real 

* Procesos Concurrentes + tiempo crítico Según gravedad de no suministrar servicio en el plazo: ° Soft – operación se degrada si no se cumplen los reqs. de tiempo (ej: central telefónica) ° Hard – operación es incorrecta si no se cumplen los reqs. de tiempo (ej: central nuclear) 

Diseño 64 

### **Complejidad en el diseño** 

- Sist. Secuencial 

- Sist. Concurrente performance 

tiempo solo afecta 

- Sist. Tiempo Real 

   - Soft 

   - Hard 

tiempo también afecta correctitud 

- Los Sists. de Tiempo Real en gral. interactúan con ambiente externo que produce estímulos en forma autónoma a los cuales el software debe responder en un tiempo límite establecido. 

Diseño 65 

Diseño de la Interfaz de Usuario (1) Principios generales (Sommerville) 

- **<u>Familiaridad</u>** : utilizar términos familiares a los usuarios 

- **<u>Consistencia</u>** : menúes y comandos con el mismo formato y significado en toda la aplicación 

- <u>: misma acción en contextos</u> 

- **<u>Mínima sorpresa</u>** comparables produzcan un cambio similar 

- **<u>Recuperabilidad</u>** : recuperación frente a errores cometidos por el usuario, brindar: * confirmación de acciones destructivas 

- * recursos para deshacer en varios niveles 

- **<u>Guía al usuario</u>** : proveer ayuda en varios niveles 

- **<u>Diversidad de usuarios</u>** : tener en cuenta distintos tipos de usuarios. 

Diseño 66 

### Diseño de la Interfaz de Usuario (2) Elementos Claves (Pfleeger): 

- **<u>Metáforas</u>** : imágenes fundamentales y conceptos 

- **<u>Modelo del método</u>** : la organización y representación de la información 

- **<u>Reglas de navegación para el modelo</u>** : cómo moverse y el modelo espacial 

- **<u>Apariencia</u>** : transmite información y significado para los usuarios 

- **<u>Sensación</u>** : la que proporciona experimentar las técnicas de interacción 

Diseño 67 

### Color en el diseño de la Interfaz (1) 

Lineamientos clave (Shneiderman 1998) 

- Limitar cantidad de colores utilizados, no más de cuatro o cinco colores distintos por ventana 

- Utilizar un cambio de color para indicar un cambio en el estado del sistema 

- Utilizar el código de colores para apoyar tarea de usuarios, por ej. resaltar similitudes o diferencias 

- , 

- Utilizar el código de colores en forma consistente por ej. desplegar mensajes de error en rojo siempre! 

- Tener cuidado al combinar colores que puedan producir cansancio en la vista 

Diseño 68 

### Color en el diseño de la Interfaz (2) 

##### Elementos culturales 

- ¿Qué color utilizar? ¿Púrpura? 

   - En Inglaterra representa la realeza 

   - En Japón, dignidad y nobleza 

   - En Grecia representaba al diablo y la muerte 

- Dos pasos para hacer nuestros sistemas multiculturales 

   - (1) eliminar sesgos o referencias a una cultura específica 

   - (2) ajustar (1) para las culturas que utilizarán el software 

Diseño 69 

### Preferencias de Usuario 

- A ella le gusta, a él no... 

- No hay una interfaz universal aplicable a todo el mundo 

- construir un prototipo y evaluarlo con la audiencia objetivo 

- permitir adaptar la interfaz de usuario 

   - ejemplo: Microsoft Word vs. WordPerfect 

Diseño 70 

### Guía para definir la interfaz de usuario 

Alto Medio Bajo 

Reconocimiento     Línea de     Formu-       Pantalla OCR de Voz Comandos   larios           sensible optical character al tacto recognition Entrada de datos 

Diseño 71 

### Soporte al Usuario 

- Sistema de ayuda debe proveer: 

   - <u>Mensajes de error</u> 

      - ° Amables, concisos, consistentes y constructivos, si es posible incluir sugerencia para correción 

   - <u>Ayuda en línea</u> 

      - ° Páginas web con hipervinculos, ventanas múltiples 

      - ° Cuidar la estructura de navegación, si es compleja los usuarios se pierden 

   - <u>Documentación de usuario</u> 

      - ° Incluyendo secciones de: instalación, descripción general, descripción funcional, mensajes de error. 

Diseño 72 

### Mensajes de error 

###### **Mensaje orientado al sistema** 



<!-- Start of picture text -->
Error #27<br>Identificador de paciente no<br>? válido<br>Aceptar Cancelar<br>Mensaje orientado al usuario<br><!-- End of picture text -->

**El paciente J. Bates no está registrado Seleccione: Pacientes para listado de pacientes registrados Reintentar para reingresar el nombre del paciente Ayuda para más información Pacientes Ayuda Reintentar Cancelar** 

Diseño 73 

### Diseño - Principios 

- Diseño para el Cambio 

- Separación de Intereses 

- Modularización (localización del impacto de los cambios) 

- Niveles de Abstracción (facilita comprensión) 

- Ocultamiento de Información (encapsular) 

- Alta Cohesión, Bajo Acoplamiento 

Diseño 74 

### Diseño para el cambio 

- ¿Qué puede cambiar? 

   - Algoritmos 

      - ° requerimientos de desempeño, escala 

   - Representación de los datos 

      - ° requerimientos de desempeño, escala 

      - ° cambios en interfaces 

   - equipos externos 

   - ambiente social 

- Para reducir el impacto de los cambios: Modularizar 

Diseño 75 

### Modularización (1) 

- Módulo: un componente bien definido de un sistema de software que provee recursos y servicios 

   - Están bien definidos: 

      - ° Recursos y Servicios 

      - ° La forma de suministrarlos (Interfaces) 

   - Un módulo puede ser un programa o varios, una subrutina o varias 

- Principio de Separación de Intereses 

   - cada módulo se ocupa de aspectos específicos 

Diseño 76 

- Modularización (2) 

- • <u>interfaces</u> 

- Definir módulos e 

   - Interfaces definen el acoplamiento entre módulos 

   - Comportamiento (Pre-Post condiciones) y colaboraciones 

- Ocultamiento de Información 

   - La información de un módulo debe ser privada a menos que se declare pública, única garantía de que otros módulos no la utilicen    ( - impacto de cambios, + fácil de comprender y usar) 

   - * Diseño interfaz:¿Qué servicios brindar, qué ocultar? ° Mínima, bien definida, independiente de implementación 

- Alta Cohesión – Bajo acoplamiento 

   - <u>Alta cohesión interna de cada módulo (los elementos del módulo</u> están fuertemente relacionados entre sí) 

   - <u>Bajo acoplamiento entre módulos (débiles conexiones entre</u> módulos -impacto reducido de cambios) 

Diseño 77 

##### Categorías de módulos 

- Sin persistencia (estado) 

   - Abstracciones de procedimientos (algoritmo) 

   - Bibliotecas (ej. rutinas matemáticas) 

- Sólo Datos 

   - Repositorio común de datos (ej. Configuración) 

- Algoritmos + Estado 

   - Objetos abstractos (ej. Stack) 

- Tipos Abstractos de Datos 

   - paramétrico en tipo (ej. Stack (?) ) 

- Clases (OO) 

Diseño 78 

### Criterios para modularizar 

- Descomposición 

   - Descomponer el problema en sub-problemas (diseño top-down) 

- Composición 

   - A partir de los componentes es posible obtener un nuevo sistema (diseño bottom-up) 

- Continuidad del impacto por cambios * Pequeños cambios en la especificación afectan pocos módulos 

- Protección durante ejecución 

   - Efectos de anomalías durante la ejecución están localizados 

Diseño 79 

### Principio Abierto/Cerrado 

- “los módulos debieran ser a la vez abiertos y cerrrados” 

- Abierto para permitir extensiones 

   - Agregar operaciones o atributos para extender el comportamiento 

   - Cambiar representaciones internas e implementaciones en caso necesario 

- Cerrado para permitir ser usado por otros módulos 

   - La interfaz debe mantenerse cerrada a los cambios y asegurar que se mantiene el comportamiento (pre- y postcondiciones) 

Diseño 80 

### Principio de elección única 

- Cuando un sistema de software debe soportar un conjunto de alternativas, un módulo y sólo uno debe conocer la lista completa de alternativas 

- Minimiza 

   - Código a escribir 

   - Impacto de cambios en la lista 

   - Reduce la complejidad y por lo tanto facilita comprensión 

- En general, se debe minimizar la distribución de conocimiento 

Diseño 81 

### Modularización - Beneficios 

- Separar aspectos del diseño 

   - Permitir cambiar algunos sin afectar al resto 

###### • Permite 

   - Extender fácilmente artefactos (extensibilidad) 

   - Reusar artefactos existentes (reusabilidad) 

   - Ocultar dependencias de la plataforma (portabilidad) 

   - Diseñar interfaces que se adapten a otras (compatibilidad) 

   - Minimizar impacto de cambios (mantenibilidad) 

   - Facilitar la comprensión 

   - Organizar y distribuir el trabajo 

- **Alta modularización** => Alta cohesión – Bajo acoplamiento 

Diseño 82 

### Cohesión 

- **Coincidente** (no relacionados) 

- **Lógica** (tipo de función) 

- **Temporal** (se usan en el mismo momento) 

- **de Procedimiento** (asegurar el orden de ejecución) 

- **de Comunicación** (operan sobre o generan los mismos datos) 

- **Secuencial** (salida de una parte es entrada de otra) 

- **Funcional** (cada parte es esencial para cumplir una función) 

- **de Información** (TAD – extensión para OO) 

Diseño 83 

### Cohesión Coincidente 

- Poca o ninguna relación entre los elementos de un módulo 

   - Dificulta el mantenimiento 

   - Módulos no reusables 

- Manifestaciones en el caso de OO 

   - Clase no representa un único concepto OO 

   - Conjunto de código usado frecuentemente como una clase con herencia múltiple 

Diseño 84 

### Cohesión Lógica 

- El módulo cumple varias funciones relacionadas. Al invocar al módulo se debe indicar mediante un parámetro qué función llevar a cabo 

   - Interfaz difícil de entender 

   - El código para más de una función puede entremezclado 

   - Difícil de reusar 

##### Solución: 

- Aislar cada función en operaciones separadas 

Diseño 85 

### Cohesión Temporal 

- Los elementos del módulo están agrupados porque se usan en el mismo período 

   - No reusable 

##### Ejemplo: 

- Módulo que concentra la inicialización de valores a objetos 

- Módulos que se encargan de limpiar al fin de un trabajo 

Diseño 86 

### Cohesión de Procedimiento 

- Los elementos del módulo están agrupados sobre la base de participar en un proceso o algoritmo 

   - Específicos para una aplicación 

   - Difícilmente reusable 

   - En el contexto el módulo es razonable, pero difícil de entender fuera de este 

### Solución: 

- Rediseñar 

Diseño 87 

### Cohesión de Comunicación 

- Los elementos del módulo usan y/o generan el mismo conjunto de datos 

   - Difícilmente reusable 

##### Solución: 

- Aislar cada elemento en módulos separados 

Diseño 88 

### Cohesión Funcional 

- Las operaciones de un módulo se pueden describir colectivamente como una única función 

   - más reusable 

   - Mantenimiento correctivo más fácil 

##### En OO: 

- Cada operación de la interfaz pública debiera presentar cohesión funcional 

- Cada objeto debe representar un único concepto cohesivo 

Diseño 89 

### Cohesión de Información 

- Un módulo tiene cohesión de información si cumple varias funciones: 

   - Varios puntos de entrada 

   - Cada entrada desempeña una función específica 

   - Todas las funciones están relacionadas por un concepto, estructura de datos, o recurso que el módulo oculta 

Diseño 90 

### Acoplamiento 

- Acoplamiento por Contenido 

   - modificación de variable interna, ejecución de una porción de procedimiento 

- Area Común (cualquiera modifica) 

- De Control (No hay ocultamiento de información) 

   - Parámetro (de entrada o salida) que gobierna ejecución 

- Estructura de Datos (comparten la estructura) 

- Datos (lo deseable) – mínima 

- No acoplado 

Diseño 91 

### Tarjetas CRC (1) 

- Clase 

- el nombre 

##### • Responsabilidades - lo que sabe y lo que hace • Collaboraciones - quiénes le ayudan 

> **Clase: Model Responsabilidad: Colaboradores:** • 

• Proporciona el núcleo de funcionalidad de la aplicación 

- View 

   - Registra los View y Controller dependientes 

   - • Notifica a los componentes dependientes acerca de cambios en los datos 

- Controller 

Diseño 92 

### Tarjetas CRC (2) 

- Permite una rápida visión de los elementos esenciales de las clases al encarar la descomposición 

- Se usan como técnica de diseño con participación de usuarios 

   - Cada uno desempeña el rol de una clase 

   - Cada uno describe lo que hace al “ejecutar” un determinado escenario de cierto caso de uso 

Diseño 93 

### Diagramas UML (1) 

- <u>Paquetes</u> (visión de alto nivel mostrando dependencias) 

- mecanismo para agrupación de elementos 

- * la dependencia significa que cambios en uno afectan al otro 

- • <u>Subsistemas</u> (visión de paquetes, comportamiento de clases) 

- agrupación lógica de elementos de diseño, con interface de servicios que brinda (implementados por las clases) 

- • <u>De Interacción</u> (dos visiones distintas de lo mismo) * <u>Secuencia</u> (deja en claro la evolución temporal) * <u>Comunicación</u> (muestra más claramente las interacciones, pero el orden está dado por números) 

- • <u>Clases</u> (relaciones estáticas, operaciones,navegabilidad) 

- • <u>Componentes</u> (dependencias entre componentes) 

- • <u>Despliegue</u> (Deployment del software en el hardware) 

Diseño 94 



<!-- Start of picture text -->
a - Parka<br>eee+ 2 Pact<br>: “ = Es<br>+Aitrehate |<br>a —_— +Atrirete J<br>-Atmibune 3<br>*Alnbeete |<br>*Atmbute2<br>~AREine 3<br><!-- End of picture text -->



<!-- Start of picture text -->
a<br><!-- End of picture text -->



<!-- Start of picture text -->
mec<br><<subsystemn==<br>thhSubsystem<br><!-- End of picture text -->

IhtySubsystemSe 

elided Fee 



<!-- Start of picture text -->
Ld<br>=<interace>= <<subsystem=><br>IMySubsystem = j=] — hySubsysten<br>ee<br>Pe<br>Canonical Form<br><!-- End of picture text -->



<!-- Start of picture text -->
m7 Component<br>.- —— Component<br>m7 Component<br><!-- End of picture text -->



<!-- Start of picture text -->
C<br>pctor<br>—) feonditian| |<br>wae Lili |<br>| |<br>| Gonckiin] [eantitine]<br>MESGT hihi! bie5 Sins Teint<br><!-- End of picture text -->



<!-- Start of picture text -->
12> penta<br>| eg beeeigt<br>eid<br>Late— (bgect: cla — Esc(rae: char<br>Ach<br>23: keebiticeg<br>Bk<br><!-- End of picture text -->



<!-- Start of picture text -->
=a a<br>: Ty hat] erat Tap<br>; f<br>l...* es as<br>arta bus fale le puliiake<br>Ue ees bat tere by bail moun trp<br><!-- End of picture text -->



<!-- Start of picture text -->
ore<br>z=)<br>|<br>Som|<br>= DEEL<br><!-- End of picture text -->

### Patrones de Diseño 

- “ Un patrón es una solución a un problema en un contexto”  (Christopher Alexander) **=>** Reuso y Diseminación 

- Surgen en la arquitectura (de casas) y los principios se aplicaron exitosamente a OOP. 

- **Nombre del patrón** . Hace posible referirse a él. 

- **El problema.** Un  patrón particular es aplicable a ciertos tipos de problemas. Un aspecto relevante de la definición de un patrón es la descripción de para qué tipos de problemas es útil. 

- • **La solución.** Un patrón define una solución 

- conceptual particular al problema. 

- **Consecuencias.** Las decisiones de implementación implican  ciertos compromisos. Las consecuencias de esas decisiones y las fuerzas que están por detrás del patrón son aspectos esenciales de este. 

Diseño 102 

Patrones de Diseño para Sistemas Interactivos 

- Mecanismos complicados de GUI 

   - Cambios y adaptaciones frecuentes 

   - Múltiples estándares de apariencia 

- Funcionalidad Compleja 

   - Usualmente permanece relativamente estable 

- El problema: 

- mantener la funcionalidad del núcleo independiente de Interfaz de Usuario 

- • Patrones: 

   - Model-View-Controller (MVC) 

   - Presentation-Abstraction-Control (PAC) 

Diseño 103 

### Model-View-Controller (MVC) 

###### • Model 

   - Núcleo de la Funcionalidad 

- View 

   - Desplegar la Información 

### **GUI** 

- Controller 

   - manejar la entrada de usuario 



<!-- Start of picture text -->
Datos del Núcleo Jan Food12 Gas17 Motel10<br>Feb 17 11 21<br>Mar 22 29 14<br>Apr 14 10 17<br>May 12 17 10<br>Ejemplo: Jun 19 15 20<br>35<br>30 35 Jan Jan<br>25 30 30<br>20 25 25 30 Jun<br>1510 2015 201510 252015 Mar AprAprMayMayJun<br>50 1050 FoodFood Gas Gas MotelMotel Food50 10Food50 GasGasMotelMotelJanJanFebFeb Mar<br><!-- End of picture text -->



<!-- Start of picture text -->
Food Gas<br>Food Gas<br>Jan 12 17<br>Jan 12 17<br>Feb 17 11<br>Feb 17 11<br>Mar 22 29<br>Mar 22 29<br>Apr 14 10<br>Ma Apr y 12 14 17 10<br>Jun May 19 12 15 17<br>Jun 19 15<br><!-- End of picture text -->

Diseño 104 

### MVC - Fuerzas 

- La misma información se presenta distinto en diferentes ventanas 

- El despliegue y comportamiento de la aplicación debe reflejar inmediatamente las manipulaciones de los datos 

- Cambios a la IU debieran ser fáciles y posibles en tiempo de ejecución 

- Soportar distintos estándares de apariencia o portar la IU no debiera afectar el núcleo de la aplicación 

Diseño 105 

### MVC - Clases (1) 

###### **Clase: Model Responsabilidad:** 

###### **Colaboradores:** 

- View 

- Controller 

- Proporciona el núcleo de funcionalidad de la aplicación 

• Registra los View y Controller dependientes 

• Notifica a los componentes dependientes acerca de cambios en los datos 

- Encapsula los datos, proporciona métodos de acceso para las vistas 

- “Controllers” invocan los métodos exportados para el procesamiento de 

- la aplicación 

- El patrón “Observer” se puede usar para propagar los cambios 

Diseño 106 

### MVC - Clases (2) 

**Clase: View Colaboradores:** 

- Controller 

- • Model 

###### **Responsabilidad:** 

   - Crea e inicializa su _Controller_ asociado 

   - • Obtiene datos de _Model_ 

   - Despliega información al usuario 

   - • Implementa el procedimiento _update_ 

- Cada _View_ crea un _Controller_ adecuado (uno a uno) 

- Ofrece interfaces que habilitan a _Controller_ para algunas 

- manipulaciones de despliegue que no afectan el modelo (p.e. scroll) 

Diseño 107 

### MVC - Clases (3) 

###### **Clase: Controller** 

###### **Responsabilidad:** 

###### **Colaboradores:** 

- View 

- Model 

• Acepta entradas del usuario como eventos 

• Traduce eventos en solicitudes de servicio para Model o View 

• Si se precisa, implementa el procedimiento _update_ 

• EL procedimiento update se implementa en caso de que el comportamiento de Controller depende del estado de Model (p.e. un cambio del modelo habilita o deshabilita un menú) 

Diseño 108 

### Diagrama de Clases 



<!-- Start of picture text -->
Observer<br>Observer<br>update<br>update<br>call update<br>call update<br>Model<br>Model<br>coreData<br>coreData<br>Controller<br>setOfObservers Controller<br>setOfObservers<br>myModel<br>myModel<br>attach(Observer)<br>attach(Observer) myView<br>View myView<br>detach(Observer) View<br>detach(Observer)<br>myModel initialize(Model,View)<br>notify myModel initialize(Model,View)<br>notify<br>handleEvent<br>myController handleEvent<br>myController<br>update<br>getData update<br>getData initialize(Model)<br>initialize(Model)<br>service attach manipulate attach<br>service attach makeController manipulate attach<br>makeController<br>getData display call service<br>getData activate display call service<br>activate<br>create<br>display create<br>display<br>update<br>update<br><!-- End of picture text -->

Curso 2007 

Ingeniería de Software 

Diseño 109 

### Distintas opciones Cliente/Servidor 



<!-- Start of picture text -->
Cliente<br><!-- End of picture text -->

###### **Servidor** 



<!-- Start of picture text -->
Int. Int. Int. Int. Int.<br>Usuario Usuario Usuario Usuario Usuario<br>Lógica Lógica Lógica<br>Int. Aplic. Aplic. Aplic.<br>Usuario<br>DBMS<br>Lógica Lógica Lógica<br>Aplic. Aplic. Aplic.<br>DBMS DBMS DBMS DBMS DBMS<br>Interfaz  Aplic.   Aplic.   DBMS  DBMS<br>distribuida Remota distribuida Remoto distribuido<br><!-- End of picture text -->

Diseño 110 

### Patrones para Distribución 

- Además, se pueden tener otros niveles... 

   - ¿cuál es el costo de cambiar la forma de distribución? 

   - ¿cómo incide en el esfuerzo de desarrollo la comunicación entre los componentes? 

##### • Problema: 

- Componentes remotos debieran aparecer como locales 

- Cliente y Servidores no debieran preocuparse de la comunicación 

Diseño 111 

# Proxy 

##### • Solución: 

- Un sustituto del servicio que permite el acceso local 



<!-- Start of picture text -->
No es<br>Servicio Abstracto directamente<br>Cliente accesible al<br>servicio Cliente<br>Proxy representa<br>al Servicio y<br>Proxy Servicio<br>asegura el<br>1 1<br>acceso a él<br>servicio servicio<br>(misma interfaz)<br><!-- End of picture text -->

Diseño 112 

# Proxy – diagrama de secuencia 

|Cliente<br>Proxy<br>Servicio|
|---|
|servicio|
|Pre-proceso y<br>asignación|
|servicio|
|Post-proceso y<br>devolución|



Diseño 113 

### ¿Cuántos proxys precisamos? 

- Problema: 

   - Muchos servicios pueden ser remotos 

   - Las ubicaciones de estos pueden cambiar 

   - Se deben poder agregar, cambiar y suprimir servicios dinámicamente 

   - Los detalles debieran quedar ocultos para el desarrollador 

Diseño 114 

# Broker 

- Solución: 

   - *Un intermediario entre proxys cliente y servidor 



<!-- Start of picture text -->
Proxy-Cliente mensajes Broker mensajes Proxy-Servidor<br>Servicio_p<br>llama<br>llama<br>Servicio Abstracto Servidor<br>Call_servicio_p Servicio_i<br><!-- End of picture text -->

Diseño 115 



<!-- Start of picture text -->
Client-side Proxy Server-side Proxy<br>Send req.<br>Forward req.<br>Call service<br>Cf Run service<br>Forward resp.<br>Return<br>Result<br><!-- End of picture text -->

### Marcos de trabajo (Frameworks) (1) 

- Aplicación reusable, semi-completa que puede ser especializada 

   - Proporciona un esqueleto extensible 

   - Soporta reuso del diseño y del código 

- Gran parte del esfuerzo y costo proviene de: 

   - Redescubrir y reinventar el diseño de clases básicas y de sus interacciones 

- Clases de frameworks: 

   - infraestructura de sistemas (ej. interfaces usuario Struts) 

   - integración de middleware (ej. Corba, Com) 

   - aplicaciones empresariales (ej. sists. Financieros) 

Diseño 117 

### Marcos de trabajo (Frameworks) (2) 

- Diferencias con otras bibliotecas de clases: 

   - Principio de “inversión del control” 

   - Basado en el patrón de diseño “template method 

   - Captura las interacciones entre objetos en un “template method”, postergando algunos pasos (“hook methods”) 

   - Especificando los “hook methods” los desarrolladores pueden ajustar las interacciones provistas por el framework 

   - Son los “template methods” los que invocan a los “hook methods” => inversión del control 

Diseño 118 

### Marcos de trabajo (Frameworks) (3) 

**aplicación** 

**biblioteca** 









Reescribiendo los “hook methods”el desarrollador inserta la personalización Framework invoca “hook methods” como parte de su interacción 

###### **Framework** 

**aplicación** 



El desarrollador  implementa las clases del núcleo y sus interacciones reusando funcionalidad ya existente 

**biblioteca** 







**Biblioteca de Clases** 

Conjunto de clases con funcionalidad preexistente 

Diseño 119 

### Marcos de trabajo (Frameworks) (4) 

- Problemas: 

   - No existe metodología: 

      - ° cómo desarrollarlos 

      - ° Cómo usarlos 

   - Curva de aprendizaje 

° En general lleva mucho tiempo y esfuerzo aprender a utilizar un marco de forma eficiente. Cuanto más complejo el marco, mayor es la curva de aprendizaje 

Diseño 120 

#### Desarrollo basado en componentes (1) 

- Surgimiento a fines de los ’90, originado por el no cumplimiento de las expectativas de reutilización que había prometido el desarrollo OO, debido a: 

   - Clases demasiado detalladas, específicas y ligadas a las aplicaciones 

   - Muchas veces hacía necesario disponer del código fuente => dificultades en comercialización 

- Visión de componente: proveedor de servicios 

   - Entidad ejecutable e independiente 

   - Publica interfaz de servicios suministrados y las interacciones son a través de ésta 

   - Generalmente también define interfaz de servicios que debe proveer el sistema que lo utiliza 

Diseño 121 

#### Desarrollo basado en componentes (2) 

- Distintos niveles de abstracción (Meyer ’99) * <u>Funcional:</u> implementa una sola función (ej.matematica) 

   - : colección de entidades 

   - <u>Agrupamiento casual</u> relacionadas débilmente (ej. declaraciones de datos, funciones) 

   - <u>Abstracciones de datos: abstracción o clase de datos en</u> OO (crear, modificar, acceder) 

   - <u>Abstracciones de clúster:</u> grupo de clases relacionadas 

   - que trabajan conjuntamente (también marcos de trabajo o frameworks) 

   - <u>Abstracciones de sistemas: sistema autocontenido</u> 

      - (también COTS) 

Diseño 122 

## 4. Características de un buen Diseño 

- Independencia de Componentes 

- Tratamiento de Anomalías 

- Prevención de Fallas 

Diseño 123 

### Independencia de componentes 

- Cuanto mayor es la independencia, más fácil es: 

   - La comprensión 

   - Mejorar, extender, adaptar, corregir 

   - Mantenimiento 

- Medida de independencia (Myers, Constantine) 

   - <u>Cohesión: medida de cuán focalizado está el módulo</u> 

      - en una cosa 

   - <u>Acoplamiento: medida de cuán conectado está el</u> módulo con otros y con el ambiente 

- Se busca alta cohesión y bajo acoplamiento 

Diseño 124 

##### Identificación y Tratamiento de Anomalías 

- **Diseño defensivo** 

   - tratando de anticipar situaciones que podrían llevar a problemas en el sistema 

- Anomalías incluyen: 

   - imposibilidad de brindar un servicio 

   - proporcionar un servicio o datos incorrectos 

   - corrupción de datos 

- Tratamiento: 

   - <u>Reintentar: restaurar e intentar nuevamente con</u> 

      - estrategia distinta 

   - <u>:</u> 

   - <u>Corregir</u> restaurar, corregir algo e intentar de nuevo con misma estrategia 

   - <u>Informar:</u> de la imposibilidad a alguien, restaurar pero 

   - no intentar nuevamente 

Diseño 125 

Prevención de Faltas y Tolerancia a Faltas 

- Tratar de anticipar faltas y manejarlas de forma de minimizar los efectos negativos y maximizar la seguridad 

Falta: el error cometido por una persona se traduce en una falta en un producto de software (o productos) Falla: desvío del sistema del comportamiento requerido <u>No toda falta produce una falla, las condiciones para</u> que una falta resulte en falla pueden no producirse nunca 

- Prevenir o tolerar faltas para evitar fallas, construyendo el sistema para que reaccione de manera aceptable 

Diseño 126 

##### Técnicas  para evitar fallas (1) 

- **Detección activa de faltas (antes de ser falla)** * <u>Periódicamente verifcar síntomas de faltas, anticipar</u> si van a ocurrir: 

      - ° control de totales, dígitos verificadores (redundancia) 

   - : 

   - <u>Sospecha mutua</u> cada componente verifica sus entradas, supone que los demás tienen defectos 

   - <u>Procesos independientes sincronizados:</u> arquitectura especial, realizan en paralelo el mismo trabajo y comparan resultados continuamente 

   - <u>Ejecutar</u> **<u>n versiones</u>** <u>distintas del programa:</u> 

      - ° diseño y construcción independiente 

      - ° con mecanismos de votación para decidir acción siguiente 

Diseño 127 

##### Técnicas  para evitar fallas (2) 

- **Respuesta a la Falta Detectada:** 

   - Dependiendo de la criticidad del sistema, falta, requerimientos de disponibilidad, mantenibilidad, se puede: 

      - ° Detener el sistema (más fácil determinar causa) 

      - ° Registrar y continuar a partir de un estado seguro 

   - reparar el daño causado por la falta 

   - cambiar el sistema para eliminar la falta 

- **Tolerancia a Faltas:** 

   - aislamiento del daño causado por la falta 

   - prevenir que la falta se convierta en falla 

   - * basada en la predicción de las ubicaciones de las faltas y definición de caminos alternativos de operación 

Diseño 128 

## 5. Documentando el Diseño 

- Un producto importante del proceso de Diseño es un conjunto de documentos que describen el sistema a construir. 

- Referencia Cruzada a los Requerimientos 

- Es la solución del problema 

Diseño 129 

