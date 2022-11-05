package aula09;

public class Aula09 {

    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Erick Lopes", 18, 'M');
        Livro l1 = new Livro("O Peregrino", "John Bunyan", 224, p1);
        l1.abrir();
        l1.folhear(1);
        l1.voltarPag();
        l1.voltarPag();
        l1.detalhes();
    }
    
}
