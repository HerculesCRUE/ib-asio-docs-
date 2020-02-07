UM. Universidad de Murcia
CRUE. Conferencia de Rectores de las Universidades Espa�olas
SGI. Sistema de Gesti�n de Investigaci�n
SUE. Sistema Universitario Espa�ol
RDF (Resource Description Framework). RDF es un lenguaje para representar datos en Grafos.
Para ello, RDF ofrece un modelo de datos denominado Tripleta, compuesto por un sujeto, un
predicado y un objeto (�Facultad de Inform�tica�; �es parte de�; �Universidad de Murcia�). El
predicado (�es parte de�) y el objeto (�Universidad de Murcia�) describen una propiedad del
sujeto(�Facultad de Inform�tica�). Uniendo varias tripletas, se obtiene un Grafo. En un Grafo
RDF, todas las entidades (sujetos, predicados, u objetos) est�n identificadas mediante URIs.
Las bases de datos especializadas en almacenar RDF se denominan Triple Stores. RDF es un
est�ndar23 del WWW Consortium24 (W3C) cuyo objetivo es ofrecer un lenguaje simple para
representar datos de manera est�ndar, como en su d�a lo hizo HTML para los documentos
Web. RDF ser�a, por as� decirlo, �el HTML de los datos�. Es importante subrayar que RDF es
un modelo de datos abstracto que puede ser serializado en diferentes sintaxis (RDF/XML,
JSON-LD, Turtle, etc.).
SHACL (SHApes Constraint Language). SHACL es un lenguaje para validar Grafos RDF contra una
serie de condiciones, o �Shapes�. SHACL es un est�ndar25 del W3C.
SPARQL (SPARQL Protocol and RDF Query Language). SPARQL es un lenguaje de consulta para
extraer datos de Grafos RDF. SPARQL tambi�n es un protocolo Web est�ndar, de modo que
cualquier Triple Store que implemente SPARQL mediante un SPARQL endpoint ofrece los
mismos servicios. SPARQL es un est�ndar26 del W3C.
RDFS (RDF Schema). RDFS ofrece un mayor nivel de expresividad que RDF, ya que permite
describir propiedades generales de las entidades RDF. Por ejemplo, se pueden definir clases de
entidades (�Universidad�, �Persona�) con propiedades compartidas. RDFS es un est�ndar27 del
W3C. Todas las entidades en RDFS est�n identificadas mediante URIs.
OWL (Web Ontology Language). OWL es un lenguaje de representaci�n de conocimiento que a�ade
m�s expresividad a RDFS, ya que se basa en L�gica Descriptiva. OWL es un lenguaje para crear
ontolog�as: una ontolog�a es una descripci�n computacionalmente expl�cita de un dominio de
conocimiento, a la que se puede aplicar razonamiento autom�tico. OWL es un est�ndar28 del
W3C. Todas las entidades en una ontolog�a OWL (Clases, Individuos, Propiedades) est�n identificadas mediante URIs.

LOD. Linked Open Data
FAIR (Findable, Accesible, Interoperable, Reusable) 
ROH. Red de Ontolog�as H�rcules. Crearlo es el objetivo del proyecto