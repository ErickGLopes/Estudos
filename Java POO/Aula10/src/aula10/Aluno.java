package aula10;
 
public class Aluno extends Pessoa implements InterfaceAluno {
    
    private boolean matr;
    private String curso;
    
    
    public Aluno() {
        if (this.getCurso() == null) {
            this.matr = true;
        } else {
            this.matr = false;
        }
    }

    public boolean isMatr() {
        return matr;
    }

    public void setMatr(boolean matr) {
        this.matr = matr;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }
    
    
    @Override
    public void cancelarMatr() {
        this.setMatr(false);
    }
    
    public void statusAluno() {
        String resp = this.isMatr()?"Sim":"Não";
        String resp2 = this.getCurso() == null?"Indefinido":this.getCurso();
        String n = this.getNome();
        System.out.println("Está matriculado? " + resp);
        System.out.println("Curso: " + resp2);
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
