/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.vectoress;

import java.util.ArrayList;
import java.util.Collections;

/**
 *
 * @author USUARIO
 */
public class Vectoress {

    public static void main(String[] args) {
         //paso 1 
       
      ArrayList<String> listavacia = new ArrayList();  
      
       //paso 2
       
       ArrayList<String> jugadores = new ArrayList(); 
       jugadores.add("messi");
       jugadores.add("suarez");
       jugadores.add("neymar");
       jugadores.add("iniesta");
       jugadores.add("alves");
       jugadores.add("puyol");
       jugadores.add("mascherano");
       
       //paso 3 
               
       System.out.println("El tamaño de la lista vacia es: " +listavacia.size());
       System.out.println("El tamaño de la lista jugadores es: " + jugadores.size());
       
       //paso 4
       
       System.out.println(" Primer Jugador: " +jugadores.get(0));
       System.out.println(" Jugador central: " +jugadores.get(jugadores.size()/2));
       System.out.println(" Ultimo Jugador: " + jugadores.get(jugadores.size()-1));
       
        //paso 5
        
       ArrayList<String> Datos_personales = new ArrayList(); 
       Datos_personales.add("santiago");
       Datos_personales.add("18");
       Datos_personales.add("1.77");
       Datos_personales.add("soltero");
       Datos_personales.add("13 de junio");
       System.out.println("Datos personales: " + Datos_personales);
       
        //paso 6
        
        ArrayList<String> it_companies = new ArrayList();
        it_companies.add("Facebook");
        it_companies.add("Google");
        it_companies.add("Microsoft");
        it_companies.add("Apple");
        it_companies.add("IBM");
        it_companies.add("Oracle");
        it_companies.add("Amazon");
        
        //paso 7
        
        it_companies.add(3,"garena");
        System.out.println("Lista con nuevo elemento: " + it_companies);
        
        //paso 8
     
        System.out.println("veracidad de la existencia del elemento: "+ it_companies.contains("IBM"));
        
        //paso 9
        
        Collections.sort(it_companies);
        System.out.println("Lista ordenada: "+ it_companies);
        
        //paso 10
        
        Collections.reverse(it_companies);
        System.out.println("Lista invertida: " + it_companies);
        
        //paso 11
        
        it_companies.remove(1); // Se especifica el index a eliminar
        System.out.println("Imprimiendo Lista despues de eliminacion: " + it_companies);
        
        //paso 12
        
        it_companies.clear();
        System.out.println("Imprimiendo Lista despues de vaciada: " + it_companies);
    }
}
