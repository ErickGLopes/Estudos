package aula10;
 
public class Pessoa implements InterfacePessoa {
    private String nome;
    private int idade;
    private char sexo;


    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public char getSexo() {
        return sexo;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
    }
    
    public void statusPessoa() {
        String n = this.getNome().toUpperCase();
        System.out.println(String.format("\n======= DADOS DO(A) %s =======", n));
        System.out.println("Idade: " + this.getIdade() + " anos");
        System.out.println("Sexo: " + this.getSexo());
        if ("MARCOS".equals(this.getNome())) {
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
    
    @Override
    public void fazerAniversario() {
        this.setIdade(this.getIdade() + 1);
    }
}
