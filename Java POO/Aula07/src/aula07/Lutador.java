/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula07;

/**
 *
 * @author devshi
 */
public class Lutador implements InterfaceLutadores {
    private String nome, nacionalidade, categoria;
    private int idade, vitorias, derrotas, empates;
    private float altura, peso;
    
    public Lutador(String no, String na, int id, float al, float pe, int vi, int de, int em) { // Construtor
        this.nome = no;
        this.nacionalidade = na;
        this.idade = id;
        this.altura = al;
        this.setPeso(pe);
        this.vitorias= vi;
        this.derrotas = de;
        this.empates = em;
    }
    
    public String getNome() {
        return this.nome;
    }
    
    private String getNacionalidade() {
        return this.nacionalidade;
    }
    
    private int getIdade() {
        return this.idade;
    }
    
    private float getAltura() {
        return this.altura;
    }
    
    private float getPeso() {
        return this.peso;
    }
    
    public String getCategoria() {
        return this.categoria;
    }
    
    private int getVitorias() {
        return this.vitorias;
    }
    
    private int getDerrotas() {
        return this.derrotas;
    }
    
    private int getEmpates() {
        return this.empates;
    }

    private void setNome(String nome) {
        this.nome = nome;
    }

    private void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    private void setIdade(int idade) {
        this.idade = idade;
    }

    private void setAltura(float altura) {
        this.altura = altura;
    }

    private void setPeso(float peso) {
        this.peso = peso;
        this.setCategoria();
    }

    private void setCategoria() {
        if (this.getPeso() < 52.2) {
            this.categoria = "Inválido";
        } 
        else if (this.getPeso() <= 70.3) {
            this.categoria = "Leve";
        } 
        else if (this.getPeso() <= 83.9) {
            this.categoria = "Médio";
        } 
        else if (this.getPeso() <= 120.2) {
            this.categoria = "Pesado";
        } else {
            this.categoria = "Inválido";
          }
    }

    private void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    private void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    private void setEmpates(int empates) {
        this.empates = empates;
    }

    @Override
    public void apresentar() {
        System.out.println("Lutador: " + this.getNome());
        System.out.println("Origem: " + this.getNacionalidade());
        System.out.println(this.getIdade() + " anos");
        System.out.println(this.getAltura() + "m de altura");
        System.out.println("Pesando: " + this.getPeso() + "Kg");
        System.out.println("Ganhou: " + this.getVitorias() + " vezes");
        System.out.println("Perdeu: " + this.getDerrotas() + " vezes");
        System.out.println("Empatou: " + this.getEmpates() + " vezes");
        System.out.println("\n=-=-=-=-=-=-=-=-=-=-=\n");
    }

    @Override
    public void status() {
        System.out.print(this.getNome());
        System.out.println(" é um peso " + this.getCategoria());
        System.out.println(this.getVitorias() + " vitórias");
        System.out.println(this.getDerrotas() + " derrotas");
        System.out.println(this.getEmpates() + " empates");
    }

    @Override
    public void ganharLuta() {
        this.setVitorias(this.getVitorias() + 1);
    }

    @Override
    public void perderLuta() {
        this.setDerrotas(this.getDerrotas() + 1);
    }

    @Override
    public void empatarLuta() {
        this.setEmpates(this.getEmpates() + 1);
    }
    
    
}
    
    
