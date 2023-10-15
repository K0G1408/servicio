# servicio
En esta actividad se desarrollará un servicio capaz de monitorear el estado de
cualquier aplicación con fines de tener más control sobre la misma.
Se trata de un servicio sencillo que verifica, cada treinta segundos, si un proceso
cualquiera (en este caso Firefox.exe) está en ejecución y, si no lo está, lo crea de nueva
cuenta, accediendo a la url https://www.youtube.com/.
*** El servicio depende del software NSSM, por lo que, para su uso, deberá instalarse esta dependencia.
