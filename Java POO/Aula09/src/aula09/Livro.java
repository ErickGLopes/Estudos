package aula09;

public class Livro implements Publicacao {
    
    // MÉTODO CONSTRUTOR
    public Livro(String t, String a, int tot, Pessoa p) {
        this.setTitulo(t);
        this.setAutor(a);
        this.setPagAtual(0);
        this.setTotPaginas(tot);
        this.setAberto(false);
        this.setLeitor(p);
    }
    
    // ATRIBUTOS
    private String titulo, autor;
    private int totPaginas, pagAtual;
    private boolean aberto;
    private Pessoa leitor;
    
    // MÉTODOS SETTERS
    private void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    private void setAutor(String autor) {
        this.autor = autor;
    }
    private void setTotPaginas(int totPaginas) {
        this.totPaginas = totPaginas;
    }
    private void setPagAtual(int pagAtual) {
        this.pagAtual = pagAtual;
    }
    private void setAberto(boolean aberto) {
        this.aberto = aberto;
    }
    private void setLeitor(Pessoa leitor) {
        this.leitor = leitor;
    }


    // MÉTODOS GETTERS
    private String  getTitulo() {
        return this.titulo;
    }
    private String getAutor() {
        return this.autor;
    }
    private int getTotPaginas() {
        return this.totPaginas;
    }
    private int getPagAtual() {
        return this.pagAtual;
    }
    private boolean getAberto() {
        return this.aberto;
    }
    private Pessoa getLeitor() {
        return this.leitor;
    }
    
    
    // MÉTODO AVULSO
    public void detalhes() {
        System.out.println("Título do livro: " + this.getTitulo());
        System.out.println("Autor: " + this.getAutor());
        System.out.println("Número de páginas: " + this.getTotPaginas());
        System.out.println("Página atual: " + this.getPagAtual());
        String estado = this.getAberto()?"aberto":"fechado";
        System.out.println("Estado do livro: " + estado);
        System.out.println("Nome do leitor: " + this.getLeitor().getNome());
    }
    
    // IMPLEMENTAÇÃO DE Publicacao
    @Override
    public void abrir() {
        this.setAberto(true);
    }
    
    @Override
    public void fechar() {
        this.setAberto(false);
    }
    
    @Override
    public void folhear(int pag) {
        if (this.getAberto() && pag <= this.getTotPaginas()) {    
            this.setPagAtual(pag);
        }
    }
    
    @Override
    public void avancarPag() {
        if (this.getAberto() && this.getPagAtual() < this.getTotPaginas()) {
            this.setPagAtual(this.getPagAtual() + 1);
        }
    }
    
    @Override
    public void voltarPag() {
        if (this.getAberto() && this.getPagAtual() > 0) {
            this.setPagAtual(this.getPagAtual() - 1);
        }
    }    
}
