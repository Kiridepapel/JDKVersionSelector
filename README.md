#

> Tener al menos [Python 3.11.4](https://www.python.org/downloads/) instalado _(instalarlo para todos los usuarios en la ruta C:\Python311)_.

#

> Crear una variable de entorno en las variables de entorno de USER llamada PYTHONHOME con el valor de C:\Python311:

```powershell
PYTHONHOME | C:\Python311
```

![PYTHONHOME](https://i.ibb.co/KyYHjP0/awasd.png)

#

> Editar la variable de entorno llamada Path y agregarle los valores de:

```powershell
%PYTHONHOME%\
%PYTHONHOME%\Scripts\
```

![Path1](https://i.ibb.co/Q63ydNX/Path.png)

#

> Tener al menos [Java 17 para Windows](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) instalado.

#

> Crear una variable de entorno en las variables de entorno de USER llamada JAVA_HOME con el valor de \bin de la version de JDK instalada en el sistema:

```powershell
JAVA_HOME | C:\Program Files\Java\jdk-17.0.7\bin
```

![JAVA_HOME](https://i.ibb.co/kxDWw19/java-home.png)

#

> Editar la variable de entorno llamada Path y agregarle el valor de:

```powershell
%JAVA_HOME%
```

![Path2](https://i.ibb.co/qkVQgK4/path2.png)

#

> Ir a [Properties] del archivo de tipo Shortcut (ejecutable).

![Open shortcut properties](https://i.ibb.co/yRTHJb9/shortcut.png)

> Pegar la ruta donde se clonó el repositorio en tu computadora local.

![Base shortcut 1](https://i.ibb.co/3rYYBMd/base-1.png)
![Base shortcut 2](https://i.ibb.co/47P2x80/base-2.png)

> Ejemplo de como debe quedar.

![Edit shortcut properties 1](https://i.ibb.co/SKWJNgf/real-1.png)
![Edit shortcut properties 2](https://i.ibb.co/0QSnXds/real-2.png)

> Save y crear un acceso directo del archivo en el escritorio

![Direct](https://i.ibb.co/H4xSrg9/shortcut-access.png)
