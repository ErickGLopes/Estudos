package aula10;
 
public class Funcionario extends Pessoa implements InterfaceFuncionario {

    private String setor;
    private boolean trabalhando;
    
    public Funcionario() {
        this.trabalhando = false;
    }

    public String getSetor() {
        return setor;
    }

    public void setSetor(String setor) {
        this.setor = setor;
    }

    public boolean isTrabalhando() {
        return trabalhando;
    }

    public void setTrabalhando(boolean trabalhando) {
        this.trabalhando = trabalhando;
    }
    
    
    @Override
    public void mudarTrabalho() {
        if (this.getSetor() != null)
            this.setTrabalhando(!(this.isTrabalhando()));
    }
    
    public void statusFuncionario() {
        String n = this.getNome();
        String resp = this.isTrabalhando()?"Sim":"Não";
        System.out.println("Setor: " + this.getSetor());
        System.out.println("Está trabalhando? " + resp);
        String linha[] = new String[28 + n.length()];
        for (int i = 0; i < linha.length; i++) {
            linha[i] = "=";
        }
        for (String c : linha) {
            System.out.print(c);
        }
        System.out.println("");
    }
}
