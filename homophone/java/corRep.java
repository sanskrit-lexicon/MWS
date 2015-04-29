import java.io.*;
import java.util.*;
import java.util.regex.*;
class corRep{
    public static char charUsedH[]={'a','A','i','I','u','U','e','E','o',' ','O','M','H','k','K','h','g','G','F','x','X','N','Y','w','W','q','Q','R','T','D','n','c','C','j','J','t','d','p','P','B','b','m','y','r','l','v','z','s','S','f','1','2','3','|','L','\''};
   
    public static int allCharsH=charUsedH.length;
    public static int numStateH=800000;
    public static boolean isFinalH[]=new boolean[numStateH];
   
    
    public static void main(String args[])throws Exception{
	int counter=0;
	int[][] DFAH=new int[numStateH][allCharsH];
	for(int i=0;i<numStateH;i++){
		for(int j=0;j<allCharsH;j++){
		    DFAH[i][j]=-1;
		}
	    }
	    String allStatesH[]=new String[numStateH];
	    int stateCount=0;
	    allStatesH[stateCount]="";stateCount++;//count=0;
	BufferedReader br=new BufferedReader(new FileReader("accent_logs/keysxml/extract_keys_b.txt"));
	String s="";//br.readLine();
	loopO:while((s=br.readLine())!=null){
	    String tmp[]=s.trim().split("\\s+");
	    String keyH=tmp[0];
	    s=keyH;
	    for(int i=0;i<s.length();i++){
		String st=s.substring(0,i+1);
		boolean isState=false;
		int prevSt=0;int nxtSt=0;
		loopOut:for(int ii=0;ii<st.length();ii++){
		    prevSt=nxtSt;
		    char a=st.charAt(ii);
		    int charIndex=chkCarH(a);
		    if(charIndex==-1){
			System.out.println("...error.this wordH.."+a+"--"+s);
			break loopOut;
		    }
		    else{
			if(DFAH[prevSt][charIndex]!=-1){
			    nxtSt=DFAH[prevSt][charIndex];
			}
			else{
			    nxtSt=-1;
			    break loopOut;
			}
		    }
		}
		if(nxtSt!=-1){
		    isState=true;
		    if(i==s.length()-1){
			isFinalH[nxtSt]=true;
		    }
		}
		if(!isState){
		    allStatesH[stateCount]=st;
		    if(i==s.length()-1){
			isFinalH[stateCount]=true;
		    }
		    int prevStateInd=0;
		    if(st.length()==1){
			prevStateInd=0;
		    }
		    else{
			prevStateInd=prevSt;
		    }
		    char toChk=s.charAt(i);
		    int charIndex=chkCarH(toChk);
		    if(charIndex==-1){
			System.out.println(toChk+"--not included "+s);
		    }
		    else{
			DFAH[prevStateInd][charIndex]=stateCount;
			stateCount++;
		    }
		}
	    }
	}
	br.close();
	br=new BufferedReader(new FileReader("accent_logs/monier_pg3.xml"));
	FileWriter fr=new FileWriter("accent_logs/monier_pg4.xml");
	loopO:while((s=br.readLine())!=null){
	    String output="";
	    String tmp[]=s.trim().split("<s>");
	    if(tmp.length>1){
		output=tmp[0];
		for(int i=1;i<tmp.length;i++){
		    String theWord=tmp[i].substring(0,tmp[i].indexOf("</s>")).replace("-","");
		     String join="<s>";
		     if(theWord.indexOf(" ")!=-1){
			 join ="<s>";
		     }
		     else if((theWord.indexOf("<sr1/>")!=-1)&&((theWord.indexOf("<sr1/>")==0)||(theWord.indexOf("<sr1/>")==theWord.length()-6))){
			     join="<s>";
		     }
		     else{
			 theWord=theWord.replace("/","").replace("<sr1>","").replace("<srs>","").replace("<srs1>","").replace("<root>","").replace("<shortlong>","").replace("<shc>","").replace("<sr>","").replace("<b>","").replace("<p1>","").replace("<p>","");
			 
			 if(theWord.indexOf("<")!=-1){
			     System.out.println(theWord);
			 }
			 if(theWord.length()>0){
			     if(stateDFAH(theWord,DFAH)){
				 join="<s corRep=\""+theWord+"\">";
			     }
			 }
		     }
		    
		    output=output+join+tmp[i];
		}			  
		fr.write(output+"\n");
	    }
	    else{
		fr.write(s+"\n");
	    }
        }
	fr.close();br.close();
    }
    public static boolean stateDFAH(String search,int[][] DFA){
	int prevSt=0;int nxtSt=0;
	loopOut:for(int i=0;i<search.length();i++){
	    prevSt=nxtSt;
	    char a=search.charAt(i);
	    int charIndex=chkCarH(a);
	    if(charIndex==-1){
		//System.out.println("..error2.."+a+"--  "+toUse);
		nxtSt=-1;
		break loopOut;
	    }
	    else{
		nxtSt=DFA[prevSt][charIndex];
		if(nxtSt==-1){
		    //fre.write(toUse+" "+search+"\n");
		    break loopOut;
		}
	    }
	}
	if(nxtSt!=-1){
	    if(!isFinalH[nxtSt]){
		nxtSt=-1;
	    }
	}
	if(nxtSt>=0){
	    return true;
	}
	return false;
    }
    public static int chkCarH(char toChk){
		int out=-1;
		loop3:for(int j=0;j<allCharsH;j++){
			if(charUsedH[j]==toChk){
				out=j;
				break loop3;
			}
		}
		return out;
	}


}