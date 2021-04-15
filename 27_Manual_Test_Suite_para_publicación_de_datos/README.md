![](./img/logos_feder.png)

| Entregable     | Manual Test Suite para publicación de datos                         |
| -------------- | ------------------------------------------------------------ |
| Fecha          | 15/04/2021                                                   |
| Proyecto       | [ASIO](https://www.um.es/web/hercules/proyectos/asio) (Arquitectura Semántica e Infraestructura Ontológica) en el marco de la iniciativa [Hércules](https://www.um.es/web/hercules/) para la Semántica de Datos de Investigación de Universidades que forma parte de [CRUE-TIC](https://www.crue.org/proyecto/hercules/) |
| Módulo         | Manual Test Suite para publicación de datos                 |
| Tipo           | Documento                                                     |
| Objetivo       | Manual Test Suite para publicación de datos  |
| Estado         | **100%**  |



# Manual Test Suite para publicación de datos 

Desde el punto de vista del cumplimento LDP, [Trellis](https://github.com/trellis-ldp/trellis/wiki) en su documentación, asegura un cumplimiento completo de los [requisitos de un servidor LDP](https://www.w3.org/TR/ldp/).

Para evaluar el cumplimiento de dichos requisitos de primera mano, se ha usado el [LDP Test Suit](https://dvcs.w3.org/hg/ldpwg/raw-file/default/tests/ldp-testsuite.html), creado exprofeso por la LDP, para evaluar el nivel de cumplimiento.

Los resultados, y las causas de los *"errores"* en los test, están descritos de forma exhaustiva en el documento [Test Suite para publicación de datos ](../26-Test_suite_para_publicación_de_datos/README.md)

**Comentarios sobre resultados de test**

Como resumen del mismo podemos ver los resultados en la tabla bajo estas líneas (por claridad solo se muestran los test fallados distintos).

| Tipo de contenedor | Ejecutados | Fallos MUST | Fallos SHOULD | Fallos MAY |
| ------------------ | ---------- | ----------- | ------------- | ---------- |
| Basic              | 112        | 1           | 5             | 1          |
| Direct             | 112        | 1           | 6             | 1          |
| Indirect           | 112        | 1           | 5             | 1          |

En cuanto a los requisitos MUST, indican obligación, por lo tanto son los mas restrictivos, y en la medida de lo posible,se debería de intentar asegurar el cumplimiento.

Los requisitos SHOULD, expresan un consejo, por lo tanto son menos restrictivos que los requisitos MUST, es decir expresan la forma deseada de actuar, pero no una obligación.

Los requisitos MAY, son los menos restrictivos, y expresan solo un deseo.

Como se aprecia en la tabla, solo existe un requisito obligatorio **MUST**, incumplido, en cualquier caso, funcionalmente el funcionamiento del servidor es correcto (la entidad no es insertada, y el código de error es correcto), pero el test falla por que no aparece la causa en la cabecera Link con una relación http://www.w3.org/ns/ldp#constrainedBy 

El resto de casos son **SHOULD** (consejos).

En estos casos se aprecia un patrón en los test fallados por Trellis:

- **Casos de fallo por reutilización de URIs ** (fallo de 3 test en 4 casos)

  - **testRestrictUriReUseSlug** (SHOULD)
  - **testPutRequiresIfMatch **(SHOULD)
  - **testRestrictPutReUseUri: **(SHOULD)

 

En estos casos básicamente el servidor permite la reutilización de URIs. La implementación de este tipo de requisitos entra en conflicto con el requisito para este proyecto de [Versinado de entidades](#Versionado de entidades) implementado por Trellis siguiendo el estándar Memento, especificado en el documento [Memento Guía y Normativa.md](./Memento%20Gu%C3%ADa%20y%20Normativa.md) . En dicho estándar aparece el concepto de estados de entidades en distintas líneas temporales, es decir una misma entidad, no será modificada al recibir una modificación (borrado o actualización), sino que se creara un estado nuevo, el una nueva línea temporal, de forma que sea posible acceder al estado de cualquier entidad, en cualquier instante de tiempo. Esto **Obliga** a la reutilización de URIs, y causa el fallo del test, ya que el servidor interpreta la acción del test (borrado y después creación de la entidad), como distintos estados de la misma entidad. En resumen, **no se puede cumplir la recomendación de la LDP**, sin mermar la capacidad del servidor.



- **Casos de fallo interpretativos sobre la LDP **(fallo de 1 test en 1 casos)

  - **testTypeRdfSource** (MUST)
  
    

  En este caso, se puede considerar fallo o no depende de la interpretación que se realice de los requisitos LDP, ya que aplican 2 requisitos, que al menos en lo evaluado por el test son opuestos. En mi pion, aplica el requisito mas especifico, y en ese caso cumpliría el, requisito, y el test no estaría bien implementado. para mas información se recomienda ver la documentación [Analisis de Test LDP (caso de uso Trellis).md](./Analisis%20de%20Test%20LDP%20(caso%20de%20uso%20Trellis).md), en la sección especifica sobre el test testTypeRdfSource.
- **No advertir de las restricciones** (fallo de 3 test en 6 casos)

  - **testPublishConstraintsUnknownProp **(SHOULD y MAY)
  - **testPutSimpleUpdate **(SHOULD y MAY)
  - **testResponsePropertiesNotPersisted** (SHOULD y MAY)

  En este patrón de fallo, el comportamiento funcional del servidor es robusto, es decir actúa de la forma  especificada por la LDP (no creando el recurso, con un codigo de error 4xx).

  No cumple la parte de la normativa **MAY**, que indica que seria bueno dar información de fallo en el cuerpo del mensaje. 

  Podría evaluarse la opción de re-implementar la parte de Trellis, que gestiona este caso, pero probablemente la inversión en tiempo sea mayor al beneficio obtenido, teniendo en cuenta que únicamente afecta a la parte MAY, del requisito, y que funcionalmente el comportamiento es correcto. 

- **Fallo al expresar preferencia de contenido:**

  - **testPreferMembershipTriples** (SHOULD)

  En este caso el test falla por que se expresa la preferencia de obtener solo las tripletas de pertenencia, y se recuperan todas las tripletas. 

  Podría evaluarse la opción de re-implementar la parte de Trellis, que gestio

