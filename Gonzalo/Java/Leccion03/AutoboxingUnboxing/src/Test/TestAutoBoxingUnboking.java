
package Test;

public class TestAutoBoxingUnboking {
    public static void main(String[] args) {
        //Clases envolventes o Wrapper
        /*
            Clases envolventes de tipos primitivos
            int = la clase  envolvernte es integer
            long = la clase envolvente es Long
            float = la clase envolvente es Float
            Boolean = la clase envolvente es Boolean
            byte = la clase envolvente es byte
            char = la clase envolvente es char
            short = la clase envolvente es short
        */
        
        int enteroPrim = 10; //Tipo primitivo
        System.out.println("enteroPrim = " + enteroPrim);
        Integer entero = 10; //Tipo object con la clase Integer
        System.out.println("entero = " + entero);
        int entero2 = entero; //Unboxing
        System.out.println("entero2 = " + entero2);
    }
}
