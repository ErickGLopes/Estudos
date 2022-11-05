/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula05;

/**
 *
 * @author devshi
 */
public class ContaBanco {
        public int numConta;
        protected String tipo;
        private String dono;
        private double saldo;
        private boolean status;
        
        public void dados() {
            System.out.println("N° da conta: " + this.getNumConta());
            System.out.println("Tipo: " + this.getTipo());
            System.out.println("Dono: " + this.getDono());
            System.out.println("Saldo: R$" + this.getSaldo());
            System.out.println("Status: " + this.isStatus());
                    
        }
        
        public ContaBanco() {
            this.status = false;
            this.saldo = 0;
        }
        
        public int gerarNumero() {
            double num[] = new double[10];
            String n = "";
            for (int i = 0; i < 5; i++) {
                num[i] = 1 + Math.random() * (5 - 1);
            }
            for (int i = 0; i < 5; i++) {
                n += Integer.toString((int) num[i]);
            }
            int numFinal = Integer.parseInt(n);
            return numFinal;
        }
        
        public void abrirConta(String nome, String tp) {
            if (this.status != true) {
                this.setStatus(true);
                this.setDono(nome);
                this.setNumConta(gerarNumero());
                this.setTipo(tp);
                if ("CC".equals(tp)) {
                    this.setSaldo(50);
                }
                else if ("CP".equals(tp)) {
                    this.setSaldo(150);
                }
            }
        }
        
        public void fecharConta() {
            if (this.saldo > 0) {
                System.out.println("Erro! Conta com dinheiro");
            }
            else if (this.saldo < 0) {
                System.out.println("Erro! Saldo negativo");
            } else {
                this.status = false;
                System.out.println("Conta encerrada com sucesso");
            }
            
        }
        
        public void depositar(double valor) {
            if (this.isStatus()) {
                this.setSaldo(this.getSaldo() + valor);
                System.out.println(String.format("R$%.2f depositado para %s", valor, this.getDono()));
            } else {
                System.out.println("Erro! Não foi possível realizar a operação");
            }
            
        }
        
        public void sacar(double valor) {
            if (this.isStatus() == true && valor <= this.getSaldo()) {
                this.setSaldo(this.getSaldo() - valor);
                System.out.println(String.format("R$%.2f retirado da conta de %s", valor, this.getDono()));
            } else {
                System.out.println("Erro! Não foi possível realizar a operação");
            }
            
        }
        
        public void pagarMensal() {
            if (this.isStatus() == true && this.getSaldo() > 0) {
                if ("CC".equals(this.getTipo())) {
                    this.setSaldo(this.getSaldo() - 12);
                    System.out.println("Mensalidade de RS12,00 paga com sucesso");
                }
                else if ("CP".equals(this.getTipo())) {
                    this.setSaldo(this.getSaldo() - 20);
                    System.out.println("Mensalidade de RS20,00 paga com sucesso");
                }
            } else {
                System.out.println("Erro! Não foi possível realizar a operação");
            }
        }
        
        public long getNumConta() {
            return this.numConta;
        }
        
        public void setNumConta(int num) {
            this.numConta = num;
        }
        
        public String getTipo() {
            return this.tipo;
        }
        
        public void setTipo(String tp) {
            this.tipo = tp;
        }
        
        public String getDono() {
            return this.dono;
        }
        
        public void setDono(String nome) {
            this.dono = nome;
        }
        
        public double getSaldo() {
            return this.saldo;
        }
        
        public void setSaldo(double valor) {
            this.saldo = valor;
        }
        
        public boolean isStatus() {
            return this.status;
        }
        
        public void setStatus(boolean s) {
            this.status = s;
        }
}
