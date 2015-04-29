import java.io.*;
import java.util.*;
import java.util.regex.*;
class removeHom{
    public static char charUsed[]={'a','A','i','I','u','U','e','E','o',' ','O','M','H','k','K','h','g','G','F','x','X','N','Y','w','W','q','Q','R','T','D','n','c','C','j','J','t','d','p','P','B','b','m','y','r','l','v','z','s','S','f','1','2','3','|','L','\''};
    public static String len2 [] ={"aa","ii","uu",".r",".l","ai","au","kh","gh","ch","jh","~n",".t",".d",".n","th","dh","ph","bh",".s",".m",".h"};
    public static String len3 []= {".rr",".lr",".th",".dh"};
    public static String sl2 [] ={"A","I","U","f","x","E","O","K","G","C","J","Y","w","q","R","T","D","P","B","z","M","H"};
    public static String sl3 []= {"F","x","W","Q"};
    public static int useMW=6953;
    public static int allChars=charUsed.length;
    public static int numState=800000;
    public static int wordsV=104941;
    public static boolean isFinal[]=new boolean[numState];
    public static String allHom[]=new String[numState];
    public static void main(String args[])throws Exception{
	BufferedReader br=new BufferedReader(new FileReader("accent_logs/monier_pg.xml"));
	FileWriter fr=new FileWriter("accent_logs/monier_pg2.xml");
	String s="";//br.readLine();
	loopO:while((s=br.readLine())!=null){
	    String search=s;
	    String output=s;
	    Pattern patt = Pattern.compile("^<H[1234][ABC]><h>");
	    Matcher  m = patt.matcher(search);
		    if(m.find()){
			
			if(search.indexOf("</key2><hom>")!=-1){
			    // System.out.println(search);
			    int indSt=search.indexOf("<hom>",search.indexOf("</key2>"));
			    int endSt=search.indexOf("</hom>",indSt)+6;
			    output=s.substring(0,indSt)+s.substring(endSt);
			    //System.out.println(output);break loopO;
			}
		
		    }
		    fr.write(output+"\n");
	}
	br.close();fr.close();
    }
}