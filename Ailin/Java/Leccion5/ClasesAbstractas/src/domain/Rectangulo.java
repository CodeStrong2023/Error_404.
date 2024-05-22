
package domain;

public class Rectangulo extends FiguraGeometrica {
    //Constructor
    public Rectangulo (String tipoFigura){
        super(tipoFigura);
    }

    @Override //implementamos el método
    public void dibujar() {
      System.out.println("Se imprime un: "+this.getClass().getSimpleName());
    }
    
}
