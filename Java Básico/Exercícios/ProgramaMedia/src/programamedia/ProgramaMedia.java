/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package programamedia;

import java.util.Calendar;
import java.util.Scanner;

/**
 *
 * @author devshi
 */
public class ProgramaMedia {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner teclado = new Scanner(System.in);
        int anoAtual =  Calendar.getInstance().get(Calendar.YEAR);
        System.out.print("Ano de nascimento: ");
        int anoNasc = teclado.nextInt();
        int idade = anoAtual - anoNasc;
        if (idade >= 18) {
            System.out.println("Maior de idade");
        } else {
            System.out.println("Menor de idade");
        }
        
        
    }
    
}
