/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex02;

public class Ex02 {

    public static void main(String[] args) {
        Garrafa g1 = new Garrafa();
        g1.cor = "Azul claro";
        g1.carga = 80;
        g1.capacidade = 120;
        g1.modelo = "Tupperware";
        g1.encher();
        g1.esvaziar();
        g1.esvaziar();
        g1.esvaziar();
        g1.tampar();
        g1.esvaziar();
        g1.esvaziar();
        g1.esvaziar();
        
        g1.status();
    }
    
}
