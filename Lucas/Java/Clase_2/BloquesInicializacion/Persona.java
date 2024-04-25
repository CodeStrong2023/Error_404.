package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;

    static{ //Bloque de inicializacion estatico
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadorPersonas;
    //  idPersona = 10; No es un atributo estático, por eso mismo da error 
    }

    {   // Bloque de inicialización no estático o contexto dinámico

        System.out.println("Ejecución del bloque no estático");
        this.idPersona = Persona.contadorPersonas++; // Incrementamos el atributo


    }

    // Los bloques de inicialización se ejecutan antes del constructor

    public Persona() {
        System.out.println("Ejecución del constructor");

    }

    public int getIdPersona() { //Recuperamos el ID
        return this.idPersona;
    }

}