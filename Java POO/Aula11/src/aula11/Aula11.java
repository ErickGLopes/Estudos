package aula11;

public class Aula11 {

    public static void main(String[] args) {
        // Pessoa p1 = new Pessoa();
        /*Visitante v1 = new Visitante();
        v1.setNome("Jevenal");
        v1.setIdade(22);
        v1.setSexo('M');
        System.out.println(v1.toString());*/
        
        /*Aluno a1 = new Aluno();
        a1.setNome("Osvaldo");
        a1.setIdade(17);
        a1.setSexo('M');
        a1.setMatricula(1111);
        a1.setCurso("Enfermagem");
        a1.pagarMensalidade();
        System.out.println(a1.toString());*/
        
        Bolsista b1 = new Bolsista();
        b1.setNome("Eliabe");
        b1.setSexo('M');
        b1.setIdade(27);
        b1.setCurso("ADS");
        b1.setMatricula(2222);
        b1.setBolsa(12.5f);
        b1.pagarMensalidade();  
        b1.renovarBolsa();
        System.out.println(b1.toString());
    }
    
}
