package aula06;

public class ControleRemoto implements Controlador {
    private int volume;
    private boolean ligado;
    private boolean tocando;
    
    public ControleRemoto() {
        this.setVolume(50);
        this.setLigado(true);
        this.setTocando(false);
    }
    
    private int getVolume() {
        return this.volume;
    }
    
    private boolean isLigado() {
        return this.ligado;
    }
    
    private boolean isTocando() {
        return this.tocando;
    }
    
    private void setVolume(int v) {
        this.volume = v;
        
    }
    
    private void setLigado(boolean l) {
        this.ligado = l;
    }
    
    private void setTocando(boolean t) {
        this.tocando = t;
    }

    @Override
    public void ligar() {
        this.setLigado(true);
    }
    
    @Override
    public void desligar() {
        this.setLigado(false);
    }
    
    @Override
    public void abrirMenu() {
        if (this.isLigado()) {
            System.out.println("-----MENU-----");
            System.out.println("Ligado? " + this.isLigado());
            System.out.println("Tocando? " + this.isTocando());
            System.out.print("Volume: ");
            for (int i = 0; i < this.getVolume(); i += 10) {
                System.out.print("|");
            }
            System.out.println(" " + this.getVolume());
        }
    }
    
    @Override
    public void fecharMenu() {
        System.out.println("Fechando Menu...");
    }
    
    @Override
    public void maisVolume() {
        if (this.isLigado()) {
            this.setVolume(this.getVolume() + 5);
        }
    }
    
    @Override
    public void menosVolume() {
        if (this.isLigado() && this.getVolume() > 0) {
            this.setVolume(this.getVolume() - 5);
        }
    }
    
    @Override
    public void ligarMudo() {
        if (this.isLigado() && this.getVolume() > 0) {
            this.setVolume(0);
        }
    }
    
    @Override
    public void desligarMudo() {
        if (this.isLigado() && this.getVolume() == 0) {
            this.setVolume(50);
        }
    }
    
    @Override
    public void play() {
        if (this.isLigado() && !this.isTocando()) {
            this.setTocando(true);
        }
    }
    
    @Override
    public void pause() {
        if (this.isLigado() && this.isTocando()) {
            this.setTocando(false);
        }
    }
}
