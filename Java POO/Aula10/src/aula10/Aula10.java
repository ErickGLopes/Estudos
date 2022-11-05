package aula10;

public class Aula10 {

    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();
        Aluno p2 = new Aluno();
        Funcionario p3 = new Funcionario();
        Professor p4 = new Professor();
        
        p1.setNome("Marcos");
        p2.setNome("Maria");
        p3.setNome("Pedro");
        p4.setNome("Teogenes");
        
        // MARCOS (p1)
        p1.setIdade(42);
        p1.setSexo('M');
        p1.fazerAniversario();
        
        // MARIA (p2)
        p2.setIdade(17);
        p2.setSexo('F');
        p2.setCurso("Sistemas Embarcados");
        //p2.cancelarMatr();
        
        // PEDRO (p3)
        p3.setIdade(29);
        p3.setSexo('M');
        p3.setSetor("Estoque");
        p3.mudarTrabalho();
        
        
        // TEOGENES (p4)
        p4.setIdade(68);
        p4.setSexo('M');
        p4.setSalario(2500.84f);
        p4.receberAum(480);
        p4.setEspecialidade("Matemática");
        
        // STATUS
        p1.statusPessoa();
        
        p2.statusPessoa();
        p2.statusAluno();
        
        p3.statusPessoa();
        p3.statusFuncionario();
        
        p4.statusPessoa();
        p4.statusProfessor();
    }
}
