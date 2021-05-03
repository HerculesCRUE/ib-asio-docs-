![](./img/logos_feder.png)

| Entregable   | Ejemplos reales de aplicación de razonamiento automático     |
| ------------ | ------------------------------------------------------------ |
| Fecha        | 03/05/2021                                                   |
| Revisado por | Paloma Terán Pérez                                           |
| Proyecto     | [ASIO](https://www.um.es/web/hercules/proyectos/asio) (Arquitectura Semántica e Infraestructura Ontológica) en el marco de la iniciativa [Hércules](https://www.um.es/web/hercules/) para la Semántica de Datos de Investigación de Universidades que forma parte de [CRUE-TIC](https://www.crue.org/proyecto/hercules/) |
| Módulo       | Ejemplos reales de aplicación de razonamiento automático     |
| Tipo         | Software                                                     |
| Objetivo     | Documentar el razonamiento automático implementado por el triplestore empleado en el proyecto ASIO. |
| Estado       | **100%**                                                     |


# Ejemplos reales de aplicación de razonamiento automático
La aplicación de razonamiento automático sobre datos RDF generalmente se hace infiriendo conocimiento latente en el grafo. Esto significa que si por ejemplo María es una profesora y tenemos otra sentencia que nos indique que los profesores son personas, se podría inferir que María es una persona. Como vemos este ejemplo es muy simple. Pero se pueden expandir las capacidades de razonamiento e inferencia mucho más.

En la actualidad existen un montón de razonadores, algunos de los más famosos son:
- [Pellet](https://github.com/stardog-union/pellet)
- [openllet](https://github.com/Galigator/openllet)
- [FaCT++](https://github.com/ethz-asl/libfactplusplus)
- [HermiT](http://www.hermit-reasoner.com/)
- [ELK](https://github.com/liveontologies/elk-reasoner)
- [Whelk](https://github.com/balhoff/whelk)
- [OWL-RL](https://github.com/RDFLib/OWL-RL)
- [RacerPro](https://franz.com/agraph/racer/)
- [Manchester List of Reasoners](http://owl.cs.manchester.ac.uk/tools/list-of-reasoners/)
- [elephant-reasoner](https://github.com/sertkaya/elephant-reasoner)
- [HyLAR](https://github.com/ucbl/HyLAR-Reasoner)
- [ruby-rdf/rdf-reasoner](https://github.com/ruby-rdf/rdf-reasoner)
- [cel](https://github.com/julianmendez/cel) -A lightweight Description Logic reasoner for large-scale biomedical ontologies.
- [reasonable](https://github.com/gtfierro/reasonable) - OWL 2 Reasoner built on DataFrog
- [eye](https://github.com/josd/eye) - Euler Yet another proof Engine.
- [Sequoia](https://github.com/andrewdbate/Sequoia) - Sequoia is a consequence-based OWL 2 DL Reasoner supporting multithreaded reasoning.
- [konclude](http://www.derivo.de/en/produkte/konclude.html) - Konclude is a high-performance reasoner for large and expressive ontologies.
- [owlproofs](https://github.com/klinovp/owlproofs) - Extension to the OWL API to request proofs of entailments from the reasoner.

En el caso del proyecto Hércules ASIO se emplea Trellis como plataforma de Linked Data. Esta plataforma soporta razonadores basados en RDFSchema. Es decir, que emplea el esquema de los datos para poder inferir información latente del grafo sobre aquellos nodos que no hayan completado toda su expresividad. Dicho con otras palabras. Si tenemos el ejemplo anterior donde María era una profesora y los profesores eran personas, un razonador basado en rdf schema detectará que María podría tener otra sentencia diciendo que es persona y no la tiene. Entonces introduciría esta sentencia en María.

Como trabajo futuro se deja explorar el rendimiento de este tipo de razonadores. Pues si bien trabajan muy bien para grafos de tamaño medio y pequeño no tienden a escalar muy bien, tal y como se explica en [Time – Space Trade-offs in Scaling up RDF Schema Reasoning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.96.5651&rep=rep1&type=pdf). 