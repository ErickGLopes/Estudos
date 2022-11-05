/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula05;

public class ProjetoContaBanco {
    
    public static void linha1() {
            System.out.println("\n============================\n");
        }
    
    public static void linha2() {
            System.out.println("\n----------------------------\n");
        }
    
    public static void main(String[] args) {
        
        ContaBanco contaJ = new ContaBanco();
        
        contaJ.abrirConta("Jubileu", "CC");
        contaJ.depositar(300);
        
        ContaBanco contaC = new ContaBanco();
        
        contaC.abrirConta("Creuza", "CP");
        contaC.depositar(500);
        contaC.sacar(100);
        linha1();
        contaJ.dados();
        linha2();
        contaC.dados();
    }
    
}
