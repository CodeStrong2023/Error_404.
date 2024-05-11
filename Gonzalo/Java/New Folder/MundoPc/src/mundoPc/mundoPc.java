
package mundoPc;

import ar.com.System2023.mundopc.*;


public class mundoPc {
    public static void main(String [] args){
        Monitor monitorHP = new Monitor ("HP", 13); //Importar la clase
        Teclado tecladoHP = new Teclado ("Bluetooth", "HP");
        Raton ratonHP = new Raton ("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora ("Computadora HP",monitorHP, tecladoHP, ratonHP);
        
         Monitor monitorgamer = new Monitor ("gamer", 32); 
        Teclado tecladogamer = new Teclado ("Bluetooth", "gamer");
        Raton ratongamer = new Raton ("Bluetooth", "gamer");
        Computadora computadoragamer = new Computadora ("Computadora gamer",monitorgamer, tecladogamer, ratongamer);
        Orden orden1 = new Orden(); //Inicializamos el arreglo vacio
        Orden orden2 = new Orden(); //nueva lista para el objeto orden2
        Orden orden3 = new Orden();
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoragamer);
        orden1.mostrarOrden ();
        
        Computadora computadorasVarias = new Computadora ("Computadora de diferentes marcas", monitorHP, tecladogamer, ratonHP);
        orden2.agregarComputadora(computadorasVarias);
        
        Monitor monitorGIGABYTE = new Monitor ("GIGABYTE", 32); //Importar la clase
        Teclado tecladoHyper = new Teclado ("Hyper", "GAMER");
        Raton ratonRazer = new Raton ("razer", "VIPER ");
        Computadora computadoraAsus = new Computadora ("Computadora ASUS",monitorGIGABYTE, tecladoHyper, ratonRazer);
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.agregarComputadora(computadoraAsus);
        orden3.mostrarOrden ();
    }
       
    
}
//Crear mas objetos de tipo computadora con todos sus elementos
//Completar una lista en el objeto orden1 que llegue a los 10 elementos 
//Probar de esta manera los metodos al maximo rendimiento 