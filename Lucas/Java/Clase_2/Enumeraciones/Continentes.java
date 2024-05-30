package enumeraciones;

public enum Continentes {
    AFRICA(53, "1.2 billones"),
    EUROPA(46, "1.4 billones"),
    ASIA(44, "1.9 millones"),
    AMERICA(34, "2.8 millones"),
    OCEANIA(14, "1 billones");

    private final int paises; //Atributo constante
    private final string habitantes;

    Continentes(int paises, String habitantes) {
        this.paises = paises;
        this.habitantes = habitantes;
    }

    //Método GET //Accedemos al attributo

    public int getPaises(){
        return this.paises;
    }

    public String getHabitantes(){
        return this.habitantes;
    }
    
}