package aula09;

public class Pessoa implements InterfacePessoa {
    
    // MÉTODO CONSTRUTOR
    public Pessoa(String n, int i, char s) {
        this.setNome(n);
        this.setIdade(i);
        this.setSexo(s);
    }
    
    // ATRIBUTOS
    private String nome;
    private int idade;
    private char sexo;
    
    // MÉTODOS SETTERS
    private void setNome(String nome) {
        this.nome = nome;
    }
    private void setIdade(int idade) {
        this.idade = idade;
    }
    private void setSexo(char sexo) {
        this.sexo = sexo;
    }
    
    // MÉTODOS GETTERS
    public String getNome() {
        return this.nome;
    }
    private int getIdade() {
        return this.idade;
    }
    private char getSexo() {
        return this.sexo;
    }
    
    // MÉTODO IMPLEMENTADO DA INTERFACE
    @Override
    public void fazerAniversario() {
        this.setIdade(this.getIdade() + 1);
    }
    
}
