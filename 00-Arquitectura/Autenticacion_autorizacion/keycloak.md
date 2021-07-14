# Keycloak

## Arranque

Para el arranque del servicio es preciso ejecutar:

```bash
docker-compose up -d
```

Con esto se levantarán los siguientes servicios:

- Base de datos mysql
- Keycloak 12.0.2

## Configuración

Se precisa acceder a la URL de administración http://localhost:8080/auth/admin, usando los siguientes datos:

- Usuario: admin
- Contraseña: admin

### Crear un realm

Por defecto se crea un realm denominado `Master`. Se debería crear un real específico para la solución. Desde la opción incluida dentro del nombre del realm (parte superior izquierda) aparecerá un botón "Add realm"
![Add realm](/proyectos/universidaddemurcia/SEMANTMURC/authorization/keycloak/keycloak-add-realm-1024x615.webp)

En la siguiente pantalla se añadirá un nuevo realm denominado `umasio`.

### Crear un cliente

Una vez creado el realm, se creará un cliente para la aplicación. Para ello se irá a la sección `Clients`, donde se añadirá un nuevo cliente denominado `login-app` o el nombre identificativo para la aplicación. Una vez creado, será necesario indicar en la opción `Valid Redirect URIs`  la URL(s) que usará el cliente (aplicación) para la autenticación, por ejemplo en caso que la aplicación corra en el puerto 8081 `http://localhost:8081/*`.

## Autenticación local

Para la autenticación en entorno local, es preciso dar de alta los usuarios (también se permitiría autorregistro). 

### Creación de roles

Para ello, desde la opción `Roles` se pulsará en `Add role`. Por ejemplo se creará un rol con el nombre `user`.

### Creación ide usuarios

Desde la opción `Users`, se creará por ejemplo un usuario `user1`. Una vez creado, se irá a la pestaña `Credentials` para indicar la contraseña del usuario. También será necesario ir a la pestaña `Role Mappings` para asignar el rol previamente creado.

## Autenticación federada

Es posible configurar varios mecanismos de acceso, entre ellos una autenticación federada o IdP.

### SIR

En Keycloak, nos iremos a la parte de `Identity Providers` y crearemos uno de tipo SAML 2.0.

![SIR IdP](/proyectos/universidaddemurcia/SEMANTMURC/authorization/keycloak/sir-idp.png)

Nos saldrán múltiples opciones, pero antes de ponernos a rellenarlas, iremos a la parte de abajo donde pone `Import External IdP Config` importaremos los metadatos para que aparezcan los IdPs que queramos (en nuestro caso pondremos el enlace de los IdPs CRUE). 

- Opcioón 1: https://md.sir2.rediris.es/sirrr/metadata/service/aHR0cHM6Ly93d3cucmVkaXJpcy5lcy9zaXIvY3J1ZWlkcA~~/metadata.xml
- Opción 2: [metadata.xml](/proyectos/universidaddemurcia/SEMANTMURC/authorization/keycloak/metadata.xml)

Como podremos ver, se nos habrán rellenado automáticamente alguno de los campos:

![SIR SAML configuration 1](/proyectos/universidaddemurcia/SEMANTMURC/authorization/keycloak/sir-saml-config1.png)

Pero tenemos que rellenar nosotros algunos más como (los dos primeros campos que van aparecer abajo, les hemos puesto el nombre de la federación, pero podrá ser otro cualquiera): 

- En la parte de `Add Identity provider`:
    - Alias SIR2
    - Display Name SIR2
- En la parte de SAML Config:
    - Validate Signature ON (nos debería de salir justo abajo otro campo rellenado que se llama `Validating X509 Certificates`)
    - Want AuthnRequests Signed ON

Una vez tengamos todo lo anterior, guardamos y al volver a `Identity Providers` no debería de salir esto:

![SIR IdP list](/proyectos/universidaddemurcia/SEMANTMURC/authorization/keycloak/sir-idp-list.png)

Nuestro siguiente paso, será configurar los atributos para el acceso. Desde el punto anterior, seleccionamos el `Name` que nos aparece en azul (en nuestro caso, SIR2). Aquí nos saldrá otra vez los mismo que cuando estuvimos configurándolo, pero en la zona superior, saldrán tres pestañas:

- `Settings`: la configuración que hemos realizado con anterioridad
- `Mappers`: el mapeo de los atributos que haremos a continuación
- `Export`: los metadatos que nos tendréis que pasar una vez esté todo configurado

En el apartado de `Mappers`, tendremos que poner que atributos estamos solicitando para el acceso, veamos un ejemplo, de como añadir el atributo `eduPersonTargetedID` (ePTI):

![mapperseduperson.png](/images/mapperseduperson.png)

Lo primero, será poner en la casilla de `Mapper Type` el valor `Attribute Importer`. Una vez hecho esto, nos aparecerán las casillas de la imagen y las rellenaremos de la siguiente forma:

- En el campo `Name` ponemos el nombre que le queramos dar al mapeo 
- En el campo `Attribute Name` el nombre del atributo en formato oid
- En el campo `User Attribute Name` el nombre que le queramos dar en el usuario a ese atributo
- En el campo `Sync Mode Override` lo dejamos como viene por defecto, es decir, `inherit`

Lista de atributos:
- eduPersonPrincipalName: urn:oid:1.3.6.1.4.1.5923.1.1.1.6
- schacPersonalUniqueID: urn:oid:1.3.6.1.4.1.25178.1.2.15
- mail: urn:oid:0.9.2342.19200300.100.1.3
- givenName: urn:oid:2.5.4.42
- schacSn1 y SchacSn2: urn:oid:1.3.6.1.4.1.25178.1.2.6 y
- urn:oid:1.3.6.1.4.1.25178.1.2.7
- sn: urn:oid:2.5.4.4
- schacHomeOrganization: urn:oid:1.3.6.1.4.1.25178.1.2.9
- eduPersonEntitlement: urn:oid:1.3.6.1.4.1.5923.1.1.1.7
- eduPersonTargetedID: urn:oid:1.3.6.1.4.1.5923.1.1.1.10

Para el campo username del usuario se creará un mapeo específico. De esta forma se tomará el campo email que se reciba de SIR como username del usuario local.

![username.png](/images/username.png)

Una vez rellenado, guardamos y ya tendremos un atributo configurado. Este proceso habrá que repetirlo para cada atributo que necesitemos.
Con esto ya tendríamos todo configurado y solo quedaría ir a la pestaña de `Export` (mencionada con anterioridad), copiar los datos que salgan y enviarlo a la cola de sir2@rediris.es para que se den de alta en la federación.

Flujos: Será necesario crear un nuevo flujo para el primer login ya que no es necesaria una lógica tan compleja. Para ello desde el menu authentication se insertará un nuevo flujo.
![auth.png](/images/auth.png)
![simple.png](/images/simple.png)

Y se configurará en el identity provider.
![identity.png](/images/identity.png)
### Certificado
Será preciso generar una key que se incluirá a los metadatos. Para ello hay que ir a la opción Realm Settings -> Keys -> Providers. En caso que no exista ua de tipo rsa-generated, se creará una nueva, dejando los datos por defecto a excepción de la prioridad  que se indicará 100.
Una vez creado, habrá que ir a Identity Providers, dentro del que se ha creado, hay que activar Want AuthnRequests Signed (ponerlo a ON), donde aparecerán los campos:

Signature Algorithm
SAML Signature Key Name

Se indicará en el primero el valor RSA_SHA256.
Tras esto, si se exportan los metadatos ya debería aparecer el certificado.
## Importar 

Se ha realizado una exportación completa del realm listo para su importación

- [realm-export.json](/proyectos/universidaddemurcia/SEMANTMURC/authorization/keycloak/realm-export.json)


## Obtención de la configuración para OpenID

Una vez configurado el endopoint, se podrá obtener los datos de configuración para los clientes, para ello existe una URL en la que muestra esta información, por ejemplo si el Realm se llama "dev" sería `http://localhost:8080/auth/realms/dev/.well-known/openid-configuration`

De aquí lo importante son los siguientes parámetros:

* authorization_endpoint: `http://localhost:8080/auth/realms/dev/protocol/openid-connect/auth`
* token_endpoint: `http://localhost:8080/auth/realms/dev/protocol/openid-connect/token`
* jwks_uri: `http://localhost:8080/auth/realms/dev/protocol/openid-connect/certs`

## JWKS

JSON Web Key Set (JWKS) es un conjunto de claves que contienen las claves públicas usadas para verificar los JSON Web Tokens (JWT) creados por un servidor de autorización.

## Más información

- https://www.baeldung.com/spring-boot-keycloak
- https://suryaprakash-pandey.medium.com/azure-ad-idp-with-keycloak-as-sp-1ca933d71388
- https://www.npmjs.com/package/keycloak-angular
- https://blog.bitsrc.io/integrating-keycloak-with-angular-for-sso-authentication-9d1c6c2d2742
- https://github.com/jannie-louwrens/spring-boot-keycloak-angular
