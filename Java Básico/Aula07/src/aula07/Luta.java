package aula07;

import java.util.Random;

public class Luta {
    private Lutador desafiado;
    private Lutador desafiante;
    private int rounds;
    private boolean aprovada;
    private Random num = new Random();
    private int vencedor = num.nextInt(3);

    private Lutador getDesafiado() {
        return desafiado;
    }

    private void setDesafiado(Lutador desafiado) {
        this.desafiado = desafiado;
    }

    private Lutador getDesafiante() {
        return desafiante;
    }

    private void setDesafiante(Lutador desafiante) {
        this.desafiante = desafiante;
    }

    private int getRounds() {
        return rounds;
    }

    private void setRounds(int rounds) {
        this.rounds = rounds;
    }

    private boolean isAprovada() {
        return aprovada;
    }

    private void setAprovada(boolean aprovada) {
        this.aprovada = aprovada;
    }
    
    
    public void marcarLuta(Lutador l1, Lutador l2){
        if (l1.getCategoria().equals(l2.getCategoria()) && l1 != l2) {
                System.out.println("Luta marcada!");
                this.setAprovada(true);
                this.setDesafiado(l1);
                this.setDesafiante(l2);
        } else {
            System.out.println("Não foi possível marcar a luta!");
            this.setAprovada(false);
            this.desafiado = null;
            this.desafiante = null;
        }
        
    }
    
    public void lutar() {
        if (this.isAprovada()) {
            System.out.println("## DESAFIADO ##");
            this.getDesafiado().apresentar();
            System.out.println("##  DESAFIANTE ##");
            this.getDesafiante().apresentar();
            switch (this.vencedor) {
                case 0:
                    System.out.println("Empatou!");
                    this.getDesafiado().empatarLuta();
                    this.getDesafiante().empatarLuta();
                    break;
                case 1:
                    System.out.println(this.getDesafiado().getNome() + " ganhou!");
                    this.getDesafiado().ganharLuta();
                    this.getDesafiante().perderLuta();
                    break;
                case 2:
                    System.out.println(this.getDesafiante().getNome() + " ganhou!");
                    this.getDesafiado().perderLuta();
                    this.getDesafiante().ganharLuta();
                    break;
            }
        } else {
            System.out.println("A luta não pode acontecer");
        }
    }
}
