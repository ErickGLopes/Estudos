package aula10;

import java.util.Locale;

public class Professor extends Pessoa implements InterfaceProfessor {

    private String especialidade;
    private float salario;

    public Professor() {
        this.salario = 0.0f;
    }

    public String getEspecialidade() {
        return especialidade;
    }

    public void setEspecialidade(String especialidade) {
        this.especialidade = especialidade;
    }

    public float getSalario() {
        return salario;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }
    
    
    @Override
    public void receberAum(float aum) {
        this.setSalario(this.getSalario() + aum);
    }
    
    public void statusProfessor() {
        String n = this.getNome();
        String sal = String.format("R$%.2f", this.getSalario());
        System.out.println("Especialidade: " + this.getEspecialidade());
        System.out.println("Salário Atual: " + sal);
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
