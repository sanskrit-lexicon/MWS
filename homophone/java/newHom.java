import java.io.*;
import java.util.*;
import java.util.regex.*;
//The other way match from MW to Pune
class newHom{
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
    public static String checkHom[]=new String[100000];
    public static String lineHom[]=new String[100000];
    public static String homs[]=new String[100000];
    public static String homNew[]=new String[100000];
    public static String line_repair[]=new String[100000];
    public static String newHom[]=new String[100000];
    public static void main(String args[])throws Exception{
	int counter=0;
	BufferedReader br=new BufferedReader(new FileReader("accent_logs/keysxml/extract_keys_b.txt"));
	String s="";//br.readLine();
	loopO:while((s=br.readLine())!=null){
	    String tmp[]=s.trim().split("\\s+");
	    String keyH=tmp[0];
	    String allEnt=tmp[2];
	    String numEnt[]=allEnt.split(";");
	    if(numEnt.length>1){
		String lineNums="";
		for(int i=0;i<numEnt.length;i++){
		    String entryH[]=numEnt[i].split(",");
		    //if(entryH[0].length()==2){
			lineNums=lineNums+" "+entryH[1];
			//}
		}
		lineNums=lineNums.trim();
		if(lineNums.split(" ").length>1){
		    checkHom[counter]=keyH;
		    lineHom[counter]=lineNums;
		    counter++;
		}
	    }
	}
	System.out.println("Cases to check are .."+counter);
	for(int i=0;i<counter;i++){
	    homs[i]="";
	    lineHom[i]="";
	}
		    
	br=new BufferedReader(new FileReader("accent_logs/monier_pg2a.xml"));
	String mainEnt="a";
	loopO:while((s=br.readLine())!=null){
	    if(s.indexOf("<key1>")!=-1){
		String cat=s.substring(1,s.indexOf(">"));
		if(cat.indexOf("A")==-1){
		    String keyH=s.substring(s.indexOf("<key1>")+6,s.indexOf("</key1>"));
		    if(cat.length()==4){
			continue loopO;
		    }
		    loop1:for(int i=0;i<counter;i++){
			if(keyH.equals(checkHom[i])){
			    String search=s;
			    if(search.indexOf("</key2><hom>")!=-1){
				int indSt=search.indexOf("<hom>",search.indexOf("</key2>"))+5;
				int endSt=search.indexOf("</hom>",indSt);
				String hom_here = s.substring(indSt,endSt);
				homs[i]=homs[i]+hom_here+" ";
			    }
			    else homs[i]=homs[i]+"0 ";
			    lineHom[i]=lineHom[i]+find_line(s)+" ";
			    break loop1;
			}
		    }
		}
	    }
	}
	br.close();
	int toRep=0;int lineRep=0;
	FileWriter fr=new FileWriter("accent_logs/mod_hom.txt");
	for(int i=0;i<counter;i++){
	    System.out.println(checkHom[i]+" "+lineHom[i]+" "+homs[i]);
	    int reqHoms=lineHom[i].trim().split(" ").length;
	    int actHoms=findUniq(homs[i]);
	    if(actHoms<reqHoms){
		int max=findMax(homs[i]);
		String pHom="abcdefghijklmnopqrstuvwxyz";
		homNew[i]="";
		    int totalHom[]=new int[max+1];
		    String allH[]=homs[i].split(" ");
		    for(int j=0;j<allH.length;j++){
			int homH=Integer.parseInt(allH[j]);
			totalHom[homH]++;
		    }
		    //The following lines are needed if you want to find the errors
		    // if(max>0){
		    //	for(int j=1;j<max+1;j++){
		    //	    if(totalHom[j]==0){
		    //		System.out.println(checkHom[i]+" "+lineHom[i]+" "+homs[i]);
		    //	    }
		    //	}
		    //}
		    int numHom[]=new int[max+1];
		    String lines[]=lineHom[i].split(" ");
		    for(int j=0;j<allH.length;j++){
			int homH=Integer.parseInt(allH[j]);
			String repl=allH[j];
			if(homH==0){
			    repl=pHom.charAt(numHom[homH])+"";numHom[homH]++;
			}
			else{
			    if(totalHom[homH]>1){
				repl=homH+""+pHom.charAt(numHom[homH]);numHom[homH]++;
			    }
			}
			if(!(repl.equals(allH[j]))){
			    line_repair[lineRep]=lines[j];
			    newHom[lineRep]=repl;
			    lineRep++;
			    fr.write(lines[j]+" "+repl+"\n");
			}
			homNew[i]=homNew[i]+repl+" ";
		    }
		    System.out.println(checkHom[i]+" "+lineHom[i]+" "+homs[i]+"-----"+homNew[i].trim());
		toRep++;
	    }
	}
	fr.close();
	
	br=new BufferedReader(new FileReader("accent_logs/monier_pg2a.xml"));
	fr=new FileWriter("accent_logs/monier_pg3.xml");
	loopO:while((s=br.readLine())!=null){
	    String output=s;
	     if(s.indexOf("<key1>")!=-1){
		 String cat=s.substring(1,s.indexOf(">"));
		 if(cat.indexOf("A")==-1){
		     String lineH=s.substring(s.indexOf(">",s.lastIndexOf("<L"))+1,s.lastIndexOf("</L>"));
		     loop1:for(int i=0;i<lineRep;i++){
			 if(lineH.equals(line_repair[i])){
			     String hom_insert=newHom[i];
			     if(newHom[i].length()==1){
				 output=s.replace("</key2>","</key2><hom>"+hom_insert+"</hom>");
			     }
			     else{
				 String actual=hom_insert.substring(0,1);
				 output=s.replace("</key2><hom>"+actual+"</hom>","</key2><hom>"+hom_insert+"</hom>");
			     }
			     break loop1;
			 }
		     }
		 }
	     }
	    fr.write(output+"\n");
	}
	br.close();fr.close();
	//	System.out.println("Cases to repair are .."+toRep);
    }
    public static int findUniq(String hom_st){
	String allHom[]=hom_st.split(" ");
	String alr[]=new String[allHom.length];
	int counter=0;
	for(int i=0;i<allHom.length;i++){
	    if(!(allHom[i].equals("0"))){
		if(counter==0){
		    alr[counter]=allHom[i];counter++;
		}
		else{
		    boolean isPres=false;
		    loopi:for(int j=0;j<counter;j++){
			if(alr[j].equals(allHom[i])){
			    isPres=true;break loopi;
			}
		    }
		    if(!isPres){
			alr[counter]=allHom[i];counter++;
		    }
		}
	    }
	}
	return counter;
    }
     public static int findMax(String hom_st){
	String allHom[]=hom_st.split(" ");
	String alr[]=new String[allHom.length];
	int max=0;
	for(int i=0;i<allHom.length;i++){
	    if(!(allHom[i].equals("0"))){
		int homH=Integer.parseInt(allHom[i]);
		if(homH>max){
		    max=homH;
		}
	    }
	}
	return max;
    }
public static String find_line(String data){
      String $hom="";
      Pattern pattern = Pattern.compile("<L>(.*?)</L>");
      Matcher m = pattern.matcher(data);
      if(m.find()){
          $hom=m.group(1);
      }
      else{
	  int startInd=data.indexOf(">",data.indexOf("<L")+1)+1;
	  int endInd=data.indexOf("</L>");
	  $hom= data.substring(startInd,endInd);
      }
    return $hom.trim();
  }
	    
}