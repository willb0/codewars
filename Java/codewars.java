import java.util.ArrayList;
import java.util.Arrays;

public class PigLatin {
    public static String pigIt(String str) {
        String [] splits= str.split("\\s+");
        for(int i=0;i<splits.length;i++){
            splits[i]=firstToLast(splits[i])+"ay";


        }
    
    }
    public static String firstToLast(String s){
        ArrayList<Character> chars=new ArrayList<Character>(Arrays.asList(s.toCharArray());
        chars.add(chars.get(1));
        chars.remove(1);
        String s="";
        for(Char x:chars){
            s+=x;
        }
    }
}