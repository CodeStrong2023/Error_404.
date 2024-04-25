package test;

import enumeraciones.Dias;

public class TestEnumeraciones {

    public static void main(String[] args) {
    /*  System.out.println("Dia 1: "+Dias.LUNES); 
        indicadorDiaSemana(Dias.LUNES); /*Las enumeraciones se tratan como cadenas, 
        ahora no se deben utilizar comillas, se accede a través del operador punto  */

        System.out.println("Contiene No. 1:"+Continentes.AFRICA);
        System.out.println("No. de paises en el 1ro. continente: "+Continentes.AFRICA.getPaises());
        System.out.println("No. de paises en el 1ro. continente: "+Continentes.AFRICA.getHabitantes());

        System.out.println("Contiene No. 2:"+Continentes.EUROPA);
        System.out.println("No. de paises en el 2do. continente: "+Continentes.EUROPA.getPaises());
        System.out.println("No. de paises en el 2do. continente: "+Continentes.EUROPA.getHabitantes());

        System.out.println("Contiene No. 3:"+Continentes.ASIA);
        System.out.println("No. de paises en el 3ro. continente: "+Continentes.ASIA.getPaises());
        System.out.println("No. de paises en el 3ro. continente: "+Continentes.ASIA.getHabitantes());

        System.out.println("Contiene No. 4:"+Continentes.AMERICA);
        System.out.println("No. de paises en el 4to. continente: "+Continentes.AMERICA.getPaises());
        System.out.println("No. de paises en el 4to. continente: "+Continentes.AMERICA.getHabitantes());

        System.out.println("Contiene No. 5:"+Continentes.OCEANIA);
        System.out.println("No. de paises en el 5to. continente: "+Continentes.OCEANIA.getPaises());
        System.out.println("No. de paises en el 5to. continente: "+Continentes.OCEANIA.getHabitantes());

    }


    private static void indicadorDiaSemana(Dias dias){
        switch (dias) {
            case LUNES:
                System.out.println("Primer día de la semana");
                break;
            case MARTES:
                System.out.println("Segundo día de la semana");
                break;
                //Tarea
            case MIERCOLES:
                System.out.println("Tercer día de la semana");
                break;
            case JUEVES:
                System.out.println("Cuarto día de la semana");
                break;
            case VIERNES:
                System.out.println("Quinto día de la semana");
                break;
            case SABADO:
                System.out.println("Sexto día de la semana");
                break;
            case DOMINGO:
                System.out.println("Séptimo día de la semana");
                break;
            default:
                System.out.println("Día de la semana no válido");
                break;
        }
    }

}