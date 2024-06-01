
package paquete2;

import paquete1.Clase1;

public class clase3 extends Clase1 {
    public clase3(){
        super("Protected");
        this.atributoProtected = "Accedemos desde la clase hija";
        System.out.println("AtributoProtected = " + this.atributoProtected);
        this.atributoPublic = "es totalmente publico";
    }
}
