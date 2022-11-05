package aula04;


public class Aula04 {

    public static void main(String[] args) {
        Caneta c1 = new Caneta("BIC", true, "Azul");
        c1.setPonta((float) 1.0);
        String t1 = c1.isTampada()? "tampada":"destampada";
        System.out.println("Está caneta " + c1.getModelo() + " é " + c1.getCor()
        + ", " + "está " + t1 + " e a ponta é " + c1.getPonta());
        
        System.out.println("\n---------------\n");
        
        Caneta c2 = new Caneta("KKK", true, "Laranja");
        c2.setPonta((float) 0.7);
        String t2 = c1.isTampada()? "tampada":"destampada";
        System.out.println("Está caneta " + c2.getModelo() + " é " + c2.getCor()
        + ", " + "está " + t2 + " e a ponta é " + c2.getPonta());
    }
    
}
