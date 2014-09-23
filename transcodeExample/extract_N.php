<?php
/* Usage: php extract_N.php <mw.xml> extract_N.txt
   Sep 22, 2014
*/
$filein = $argv[1];
$fileout = $argv[2];
require_once("transcoder.php");
transcoder_set_dir(".");
$fp = fopen($filein,"r") or die("Cannot open $filein\n");
$fpout = fopen($fileout,"w") or die("Cannot open $fileout\n");

$n=0;

$max = 1000000;
$more = 1;
$nout = 0;
$nskip = 0; //parenthetical headwords, skipped
$nhpw = 0;
$key0='';

while(($more == 1) and (!feof($fp))) {
  $line = fgets($fp);
  $x = trim($line);
  $n++;
  if(!preg_match('|<(H.*?)>.*<key1>(.*?)</key1>.*<L.*?>(.*?)</L>|',$x,$matches)){
   continue;
  }
  $type = $matches[1];
  $key = $matches[2];
  $L = $matches[3];
  if(!preg_match('|<ab>N.</ab>|',$x,$matches)) {
   continue;
  }
  // convert 'key' from slp1 to Roman
  $keyroman = transcoder_processString($key,"slp1","roman");
  // Try uppercase
  $keyromanUpper = my_ucfirst($keyroman);
  fwrite($fpout,"$key $keyroman $keyromanUpper\n");
  $nout = $nout + 1;
  if ($nout > $max) {$more=0;}
}
fclose($fp);
fclose($fpout);
echo "$n records in, $nout records written\n";
exit(0);
// I found this example at http://php.net/manual/en/function.ucfirst.php
// It seems to do the trick!
   /** 
     * ucfirst UTF-8 aware function 
     * 
     * @param string $string 
     * @return string 
     * @see http://ca.php.net/ucfirst 
     */ 

    function my_ucfirst($string, $e ='utf-8') { 
        if (function_exists('mb_strtoupper') && function_exists('mb_substr') && !empty($string)) { 
            $string = mb_strtolower($string, $e); 
            $upper = mb_strtoupper($string, $e); 
            preg_match('#(.)#us', $upper, $matches); 
            $string = $matches[1] . mb_substr($string, 1, mb_strlen($string, $e), $e); 
        } else { 
            $string = ucfirst($string); 
        } 
        return $string; 
    } 

?>
