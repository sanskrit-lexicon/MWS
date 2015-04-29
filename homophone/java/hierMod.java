import java.io.*;
import java.util.*;
import java.util.regex.*;
class hierMod{
    // ejf: all these public static variables are UNUSED
    public static char charUsed[]={'a','A','i','I','u','U','e','E','o',' ','O','M','H','k','K','h','g','G','F','x','X','N','Y','w','W','q','Q','R','T','D','n','c','C','j','J','t','d','p','P','B','b','m','y','r','l','v','z','s','S','f','1','2','3','|','L','\''};
    public static String len2 [] ={"aa","ii","uu",".r",".l","ai","au","kh","gh","ch","jh","~n",".t",".d",".n","th","dh","ph","bh",".s",".m",".h"};
    public static String len3 []= {".rr",".lr",".th",".dh"};
    public static String sl2 [] ={"A","I","U","f","x","E","O","K","G","C","J","Y","w","q","R","T","D","P","B","z","M","H"};
    public static String sl3 []= {"F","x","W","Q"};
    public static int useMW=6953;
    public static int allChars=charUsed.length;
    public static int numState=800000;
    public static int wordsV=104941;
   
    public static void main(String args[])throws Exception{
	int counter=0;
	BufferedReader br=new BufferedReader(new FileReader("accent_logs/monier_pg2.xml"));
	FileWriter fr=new FileWriter("accent_logs/monier_pg2a.xml");
	String mainEnt="a";String enc="";String s="";
	loopO:while((s=br.readLine())!=null){
	    String output=s;
	    if(s.indexOf("<key1>")!=-1){
		String cat=s.substring(1,s.indexOf(">"));
		if((cat.indexOf("A")==-1)&&(!(cat.equals("HPW")))){
		    String keyH=s.substring(s.indexOf("<key1>")+6,s.indexOf("</key1>"));
		    if(cat.length()==2){
			mainEnt=keyH;enc="";
		    }
		    else{
			if(keyH.equals(mainEnt)){
			    output=output.replace(cat+">",cat+"a>");
			}
			else{
			    if(enc.indexOf(keyH+" ")!=-1){
				output=output.replace(cat+">",cat+"a>");
			    }
			    else{
				enc=enc+keyH+" ";
			    }
			}
			
		    }
		}
	    }
	    fr.write(output+"\n");
	}
	br.close();fr.close();
    }

	    
}