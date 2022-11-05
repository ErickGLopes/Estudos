package aula02;

public class Aula02 {

    
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.cor = "Azul";
        c1.ponta = (float) 0.5;
        c1.tampar();
        c1.status();
        c1.rabiscar();
        System.out.println("\n------------------------\n");
        Caneta c2 = new Caneta();
        c2.modelo = "Bic";
        c2.cor = "Preta";
        c2.destampar();
        c2.status();
        c2.rabiscar();
    }
    
}
