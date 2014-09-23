<?php error_reporting (E_ALL ^ E_NOTICE); ?>
<?php
// Sep 24, 2012 ejf modified for sanskrit1d
// Jan 25, 2010
// Jim Funderburk recoding into php of Java code developed by
// Ralph Bunker.
// This software is made available under the Creative Commons
// Creative Commons Attribution Non-Commercial Share Alike license available in full at <ptr target="http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode"/>, and summarized at <ptr target="http://creativecommons.org/licenses/by-nc-sa/3.0/"/>.  Permission is granted to build upon this work non-commercially, as long as credit is explicitly acknowledged exactly as described herein and derivative work is distributed under the same license.
// Assume transcoder xml files are in directory ../data/transcoder,
// relative to the directory containing this transcoder.php file
// Aug 5, 2012.  embedded spaces are improperly rendered in slp1_deva.
// Solution:  split a string using spaces; transcode the pieces; then rejoin
//  This is a change in transcoder_processString
// Dec 5, 2013.  Add transcoder_set_htmlentities(True) so output of unicode
// will be as html entities.  This facilitates debugging.
// 
global $transcoder_dir,$transcoder_fsmarr;
global $transcoder_htmlentities;
$transcoder_htmlentities = False;
$transcoder_dir=dirname(__FILE__); //use php magic constant
//$transcoder_dir =dirname($transcoder_dir); // go up one level
//$transcoder_dir .= "/data/transcoder";
$transcoder_dir .="/transcoder";
//echo "transcoder_dir = " . $transcoder_dir . "\n"; //dbg
$transcoder_fsmarr = array();
function transcoder_fsm($from,$to) {
// Uses xml file from_to.xml (in transcoder_dir) to initialize a
// finite state machine (variable $fsm). This finite state machine
// is saved in the global hash variable $transcoder_fsmarr under name
// from_to; transcoder_fsmarr[from_to] already exists, its value is
// returned, so the xml file does not have to be re-parsed.
 global $transcoder_dir,$transcoder_fsmarr;
 $fromto = $from . "_" . $to;
 if ($transcoder_fsmarr[$fromto]) {
  return;
 }
 $filein = $transcoder_dir . "/" . $fromto . ".xml";
 //echo "transcoder debug: filein = $filein\n";
 if (!file_exists($filein)) {return;}
 // The php routine simplexml_load_file  parses the xml file.
 // It was discovered that unicode values expressed as html entities
 // '&#xHHHH;' are converted to unicode!
 $xml = simplexml_load_file($filein);
 //$xml = simplexml_load_file($filein,NULL,LIBXML_NOENT);
 $entries = $xml->xpath('*');
 $n = count($entries);
 $start = (string) $xml['start'];
 $fsm=array();
 $fsm['start']=$start;
 $fsmentries = array();
 foreach($entries as $e) {
  $x = $e->xpath('in');
  $inval=(string)$x[0];
  $conlook=FALSE;
  if (preg_match(':^([^/]+)/\^:',$inval,$matches)) {
   // In transcoding from slp1 to devanagari, it is necessary to do a
   // 'look-ahead' when deciding how to code a consonant.  If the 
   // consonant is not followed by a vowel, then a vigraha has to be emitted.
   // The input codes $inval in such cases as:
   // k/^([^aAiIuUfFxXeEoO^/\\])
   // Which is to be intepreted as: starting at the next character,
   //    check if the input string does NOT match the regular expression
   //    [^aAiIuUfFxXeEoO^/\\].
   //    Note that the last 3 elements '^', '/', and '\' are present only
   //    because of accents. 
   if ( ($fromto != 'slp1_deva') && ($fromto != 'slp1_deva1')&& 
        ($fromto != 'hkt_tamil')&&
        ($fromto != 'deva_slp1')) {continue;}
   $inval = $matches[1];
   $conlook=$fromto;
  }
  $x = $e -> xpath('s');
  $sval = (string) $x[0];
  $x = $e->xpath('out');
  $outval=(string) $x[0];
  $x = $e->xpath('next');
  if ($x) {$nextval=(string) $x[0];} else {$nextval = '';}

  $startStates = preg_split('/,/',$sval,-1, PREG_SPLIT_NO_EMPTY);
  if ($nextval == '') {
   $nextval = $startStates[0];
  }
  $nextState = $nextval;
  // convert $inval, $outval to utf, if appropriate
  $newinval = transcoder_unicode_parse($inval);
  $newoutval = transcoder_unicode_parse($outval);
  $fsmentry=array();
  $fsmentry['starts']=$startStates;
  $fsmentry['in']=$newinval;
  if ($conlook) {
//    $fsmentry['regex']=$to;
     $fsmentry['regex']=$fromto;
    //otherwise, regex is undefined
  }
  $fsmentry['out']=$newoutval;
  $fsmentry['next']=$nextState;
  // Dec 5, 2013 save 'raw' inval/outval
  $fsmentry['inraw']=$inval;
  $fsmentry['outraw']=$outval;
  $fsmentries[]=$fsmentry;
 }
 $fsm['fsm']=$fsmentries;
// make associative array $states, whose keys are characters,
// and whose value at a key is an array of subscripts into $fsmentries.
//  $i is a subscript for a key provided that the $fsmentries[$i]['in'] = 
//  first character of $key
 $states=array();
 foreach($fsmentries as $i => $fsmentry) {
  $in = $fsmentry['in'];
  $c = $in[0];
  $state=$states[$c];
  if ($state) {
    $state[]=$i;
    $states[$c]=$state;
  }else {
   $state = array();
   $state[]=$i;
   $states[$c]=$state;
  }
 }
 $fsm['states']=$states;
 $transcoder_fsmarr[$fromto]=$fsm;
} 
function unichr($dec) {
  if ($dec < 128) {
    $utf = chr($dec);
  } else if ($dec < 2048) {
    $utf = chr(192 + (($dec - ($dec % 64)) / 64));
    $utf .= chr(128 + ($dec % 64));
  } else {
    $utf = chr(224 + (($dec - ($dec % 4096)) / 4096));
    $utf .= chr(128 + ((($dec % 4096) - ($dec % 64)) / 64));
    $utf .= chr(128 + ($dec % 64));
  }
  return $utf;
}
function unichr_alt($u) {
    return mb_convert_encoding('&#' . intval($u) . ';', 'UTF-8', 'HTML-ENTITIES');
}

function transcoder_unicode_parse_alt($val) {
  $utf="";
  $vals=array();
  $u1 = $val;
  while ($u1 != '') {
   if (preg_match('/^\\\\u([0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f])/',
        $u1,$matches)) {
    $u1 = substr($u1,6);
    $u = $matches[1];
    $hex="&#x" . $u . ";";
    $vals[]=$hex;
   }else { // not unicode. just take nbext char
    $vals[]=substr($u1,0,1);
    $u1 = substr($u1,1);
   }
  }
   $newinval = implode('',$vals);
   return $newinval;
}
function transcoder_unicode_parse($val){
  $utf="";
  $vals=array();
  $u1 = $val;
  while ($u1 != '') {
   if (preg_match('/^\\\\u([0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f])/',
        $u1,$matches)) {
    $u1 = substr($u1,6);
    $u = $matches[1];
    $utf=unichr(hexdec($u));
    $vals[]=$utf;
   }else { // not unicode. just take next char
    $vals[]=substr($u1,0,1);
    $u1 = substr($u1,1);
   }
  }
   $newinval = implode('',$vals);
   return $newinval;
}
function transcoder_unicode_parse_old($val) {
  $utf="";
  $vals=array();
  $u1 = $val;
  if (substr($u1,0,2) == '\u') {    
    $us=preg_split('/\\\\u/',$u1,-1, PREG_SPLIT_NO_EMPTY);
    $v='';
    foreach($us as $u) {
     $v=unichr(hexdec($u));
     $utf .= $v;
    }
    $vals[]=$utf;
   }else {
    $vals[]=$u1;
   }
   $newinval = implode('',$vals);
   return $newinval;
}
function transcoder_processString_main($line,$fsm) {
 // This routine transforms the string in variable $line, according to
 // the finite state machine in variable $fsm, and returns the result
 // Dec 5, 2013: allow results to be expressed as html entities.
global $transcoder_htmlentities;
 $currentState=$fsm['start'];
 $fsmentries = $fsm['fsm'];
 $states = $fsm['states'];
 $n=0; // current character position in $line
 $result=''; // returned value
 $m=strlen($line);
 while ($n < $m) {
  $c = $line[$n];
  $isubs = $states[$c];
  if (! $isubs) {
   $result .= $c;
   $currentState=$fsm['start'];
   $n++;
   continue;
  }
  $best="";
  $nbest=0;
  $bestFE = NULL;
  foreach($isubs as $isub) {
   $fsmentry=$fsmentries[$isub];
   $startStates=$fsmentry['starts'];
   $k=-1;
   $nstartStates=count($startStates);
   for($j=0;$j<$nstartStates;$j++) {
    if ($startStates[$j] == $currentState) {
     $k=$j;
     $j=$nstartStates;
    }
   }
   if ($k == -1) {continue;}
   $match = transcoder_processString_match($line,$n,$m,$fsmentry);
   $nmatch=strlen($match);
//   echo "chk2: n=$n, c='$c', nmatch=$nmatch<br>\n";
   if ($nmatch > $nbest) {
    $best = $match;
    $nbest=$nmatch;
    $bestFE=$fsmentry;
   }
  }
  if ($bestFE) {
   if ($transcoder_htmlentities) {
    //For debugging
    $temp = $bestFE['outraw'];
    $temp1 = transcoder_unicode_parse_alt($temp);
    $result .= $temp1;
   }else { 
    // Usual, non-debugging.
    $result .= $bestFE['out'];
   }
   $n += $nbest;
   $currentState=$bestFE['next'];
  }else {
   // Default condition. emit the character and change state to start
   $result .= $c;
   $currentState=$fsm['start'];
   $n++;
  }
 }
 return $result;
}
function transcoder_processString($line,$from,$to) {
 global $transcoder_dir,$transcoder_fsmarr;
 if ($from == $to) {return $line;}
 $fromto = $from . "_" . $to;
 $fsm = $transcoder_fsmarr[$fromto];
 if (!$fsm) {
  transcoder_fsm($from,$to);
  $fsm = $transcoder_fsmarr[$fromto];
  if (!$fsm) {
//   echo "could not find fsm\n";
   return $line;
  }
 }
 $ps = preg_split('| +|',$line);
 $qs = array();
 foreach($ps as $p) {
  $q = transcoder_processString_main($p,$fsm);
  $qs[]=$q;
 }
 $ans = join(' ',$qs);
 //transcoder_dbg($line,$from,$to,$ans);
 return $ans;
}
function transcoder_dbg($line,$from,$to,$ans) {
 $dir = dirname(__FILE__); //use php magic constant
 $fileout="$dir/tempout";
 $fp = fopen($fileout,"a");
 if ($fp) {
 fwrite($fp,"$from,$to,$line,$ans\n");
 fclose($fp);
 }
}
function transcoder_processString_match($line,$n,$m,$fsmentry) {
  $match=""; // value returned
  $edge = $fsmentry['in'];
  $nedge=strlen($edge);
  $j=$n;
  $k=0;
  $b=TRUE;
  while ( ($j < $m) && ($k < $nedge) && $b) {
   if($line[$j] == $edge[$k]) {
    $j++;
    $k++;
   }else {
    $b=FALSE;
   }
  }
  if (!$b) { return $match;}
  if ($k != $nedge)  { return $match;}
  $match=$edge;
  if (!$fsmentry['regex']) {
   return $match;
  }
  //  additional logic when $fsmentry['regex'] is DEVA or TAMIL
  //  see discussion of 'regex' in transcoder_fsm
  //  This logic only works with slp1_deva xml file.
  //  Also, it ignores the use of '/^\' as vowel accents.
  $nmatch=strlen($match);
  $n1=$n+$nmatch;
  if ($n1 == $m) {return $match;} 
  $d = $line[$n1];
  if (($fsmentry['regex'] == 'slp1_deva') || 
     ($fsmentry['regex'] == 'slp1_deva1')) {
   if (preg_match('/[^aAiIuUfFxXeEoO^\/\\\\]/',$d)) {return $match;}
   return "";
  }
  if ($fsmentry['regex'] == 'hkt_tamil') {
   if (preg_match('/[^aAiIuUeEoO]/',$d)) {return $match;}
   return "";
  }
  if (($fsmentry['regex'] == 'deva_slp1') || 
     ($fsmentry['regex'] == 'slp1_deva1')) {
   // u094d is virama, the rest are vowel signs
   $vowel_signs = array('\u094d','\u093e','\u093f','\u0940','\u0941','\u0942','\u0943','\u0944','\u0962','\u0963','\u0947','\u0948','\u094b','\u094c');
   foreach ($vowel_signs as $vowel_sign) {
    $vowel_sign1 = transcoder_unicode_parse($vowel_sign);
    $vowel_sign_len = strlen($vowel_sign1);
    $found=TRUE;
    for($j=0;$j<$vowel_sign_len;$j++) {
     $k = $n1 + $j;
     if ($k >= $m) {
      $found=FALSE;
      continue;
     }
     if($vowel_sign1[$j] != $line[$k]){
      $found=FALSE;
      continue;
     }
    }
    if($found) {
     // the consonant is followed by $vowel_sign.
     // return empty string to indicate rule failure.
     // This program logic cannot distinguish between 
     // a mismatch, and an empty string.
     // In particular, we don't handle virama properly otherwise,
     // so we do this special test to correct the problem
 //    if ($j == 0) {return $match;} // case of virama
     return "";  // case of a vowel sign
    }
   }
   // the consonant is not followed by either virama or a vowel sign. 
   // Return $match
   return $match;
  }
  return "";
}
function transcoder_processElements($line,$from,$to,$tagname){
 global $transcoder_from,$transcoder_to;
 $transcoder_from = $from;
 $transcoder_to = $to;
 // Assume parts of $line to be converted are marked in an xml way.
 // For example, if $tagname = <SA>:
 //  and $line = 'The word <SA>rAma</SA> refers to a person',
 // returned would be 'The word XXX refers to a person',
 // where XXX is the transformation of the the string 'rAma' acc. to $from,$to

// $ans = preg_replace("/<$tagname>(.*?)<\/$tagname>/e",
//         "transcoder_processString('\\1','$from','$to')",$line);
 $ans = preg_replace_callback("/<$tagname>(.*?)<\/$tagname>/ ",
         "transcoder_processElements_callback",$line);
 return $ans;
}
function transcoder_processElements_callback($matches) {
 global $transcoder_from,$transcoder_to;
 return transcoder_processString($matches[1],$transcoder_from,$transcoder_to);
}
function transcoder_standardize_filter($filter) {
 // standardizes a 'filter' into a transcoder standard.
 $standard_hash=array(
  "SKTDEVAUNICODE"=>"deva",
  "SKTROMANUNICODE"=>"roman",
  "SLP2SLP"=>"slp1",
  "SLP2HK" =>"hk",
  "HK2SLP" =>"hk",
  "SLP2ITRANS" => "itrans",
  "ITRANS2SLP" => "itrans",
  "HK" =>"hk",
  "ITRANS" => "itrans",
  "IT" => "itrans",
  "HKT" => "hkt",
  "HKT2HKT" => "hkt",
  "TAMIL" => "tamil",
  "ROMAN" => "roman",
  "DEVA" => "deva"
 );
$filter = strtoupper($filter);
$result=$standard_hash[$filter];
if (!$result) {$result="slp1";}
return $result;
}
function transcoder_set_htmlentities($flag) {
global $transcoder_htmlentities;
if ($flag) {
 $transcoder_htmlentities = True;
}else {
 $transcoder_htmlentities = False;
}
}
function transcoder_set_dir($dir) {
 // may return FALSE if string $dir is improper in some way
 global $transcoder_dir;
 $newdir = realpath($dir);
 if (! file_exists($newdir)) {
  echo "transcoder_set_dir ERROR: \ndir = $dir\nnewdir = $newdir\n";
  return;
 }
  echo "transcoder_set_dir change: \ndir = $dir\nold = $transcoder_dir\nnewdir = $newdir\n";
 $transcoder_dir=$newdir;
 return $transcoder_dir;
}
function old_transcoder_set_dir($dir) {
 // may return FALSE if string $dir is improper in some way
 global $transcoder_dir;
 $transcoder_dir=realpath($dir);
 if (! file_exists($transcoder_dir)) {
  $transcoder_dir=FALSE;
 }
 return $transcoder_dir;
}
function transcoder_get_dir() {
 global $transcoder_dir;
 return $transcoder_dir;
}
?>