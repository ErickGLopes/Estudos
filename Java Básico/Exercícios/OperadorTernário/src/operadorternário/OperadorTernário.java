/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package operadorternário;

import java.util.Scanner;
/**
 *
 * @author devshi
 */
public class OperadorTernário {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String nome1 = "Erick";
        String nome2 = "Erick";
        String nome3 = new String("Erick");
        /* nome 1 e 2 são de mesma estrutura, logo são igual, mas ambos são 
         * diferentes de nome3, pois se diferem na estrutura. Se eu quiser com-
         * parar o conteúdo de nome3 com alguma das duas, terei de usar o méto-
         * do equals() e isso será possível porque são objetos e não variáveis. 
         */
        String res = (nome3.equals(nome1))?"igual":"diferente";
        System.out.println(res);
        // Operador Ternário => String res = (n1>n2)?"n1 é maior":"n2 é maior";
    }
    
}
