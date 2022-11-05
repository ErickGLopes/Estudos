package ex02;


public class Garrafa {
    String cor;
    String modelo;
    int capacidade;
    boolean tampada;
    int carga;
    
    void status() {
        System.out.println("Cor da garrafa: " + this.cor);
        System.out.println("Modelo da garrafa: " + this.modelo);
        System.out.println("Capacidade: " + this.capacidade + "ml");
        System.out.println("Está tampada?: " + this.tampada);
        System.out.println("Carga: " + this.carga + "ml");
    }
    
    void tampar() {
        this.tampada = true;
    }
    
    void destampar() {
        this.tampada = false;
    }
    
    void encher() {
        if (this.tampada == true) {
            System.out.println("Erro! Não posso encher");
        } else {
            this.carga += 10;
        }
        
    }
    
    void esvaziar() {
        if (this.tampada == true) {
            System.out.println("Erro! Não posso esvaziar");
        } else {
            this.carga -= 10;
        }
        
    }
}
