package aula02;

public class Aula02 {

    
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.modelo = "Bic cristal";
        c1.cor = "Azul";
        c1.carga = 80;
        //c1.tampada = false;
        //c1.ponta = (float) 0.5;
        c1.tampar(); 
        /*   O atributo tampada (ex: o caixa do supermercado  
         *  está privado, mas por meio do método tampar (ex:  
         *  o atendente) é possível ter acesso ao mesmo.         
         */
        c1.status();
        c1.rabiscar();
    }
    
}
