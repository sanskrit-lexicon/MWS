<?php
 /* Same as list-0.2.html, but accepts some or all inputs as
   $_GET parameters
 */
// Report all errors except E_NOTICE  (also E_WARNING?)
error_reporting(E_ALL & ~E_NOTICE);
/* See phpinit
 $dict = $_GET['dict'];
 $key = $_GET['key'];
 $accent= $_GET['accent'];
 $input = $_GET['input'];
 $output = $_GET['output'];
*/
?>
<!DOCTYPE html> <!-- html5 -->
<html>
<head>
<META charset="UTF-8">
<title>list-0.2 Cologne</title>
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.css">
<!-- links to jquery, using CDNs -->
<script type="text/javascript" src="http://code.jquery.com/jquery-2.1.4.min.js"></script>

<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery-cookie/1.4.1/jquery.cookie.min.js"></script>
<!-- jquery-ui is used -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
<script type="text/javascript" src="http://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/sample/dictnames.js"></script>
<script type="text/javascript" src="http://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/sample/cookieUpdate.js"></script>

<style>
body {
 color: black; background-color:#DBE4ED;
 /*font-size: 14pt; */
}

#dataframe {
 color: black; background-color: white;
 width: 600px;
 height: 600px;
 /* resize doesn't work on Firefox. 
  On Chrome, the size may be increased, but not decreased*/
 resize: both;
 /*overflow: auto; */
}

#accentdiv,#outputdiv,#inputdiv,#dictionary input,label {display:block;}

#preferences {
 position:absolute;
 left:100px;
 top: 15px;
}
#preferences td {
 /*border:1px solid black;*/
 background-color:white;
 padding-left:5px;
 padding-right:5px;
 text-align:center;
}
#citationdiv{
 padding-bottom:5px;
}
#correction {

 padding-left: 130px;
}
</style>
<script> 
 // Jquery
$(document).ready(function() {
 $('#key').keypress(function (e) {
  if(e.which == 13)  // the enter key code
   {e.preventDefault();
    listDisplay();
   }
 }); // end keypress
 $('#input,#output,#dict,#accent').change(function(event) {
  cookieUpdate(true);   
 });
 $('#dict').change(function(event) {
  changeCorrectionHref();
 });
 changeCorrectionHref = function () {
  var dict = $('#dict').val();
  var url = "/php/correction_form.php?dict=" + dict;
  $('#correction').attr('href',url);
 };
 listDisplay = function () {
  var key = $('#key').val();
  var dict = $('#dict').val();
  var input = $('#input').val();
  var output = $('#output').val();
  var accent = $('#accent').val();
  console.log('listDisplay: accent value=',accent);

  // TODO: check for valid inputs before ajax call
  var urlbase="http://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/listview.php";
  var url =  urlbase +  
   "?key=" +escape(key) + 
   "&output=" +escape(output) +
   "&dict=" + escape(dict) +
   "&accent=" + escape(accent) +
   "&input=" + escape(input);
    //jQuery("#disp").html(""); // clear output
  //console.log('list.html. url=',url);
  jQuery("#dataframe").attr("src",url);
    
 }; // listDisplay
 
cookieUpdate = CologneDisplays.dictionaries.cookieUpdate;
cookieUpdate(false);  // for initializing cookie
changeCorrectionHref();  // initialize now that #dict is set.
$("#dict").autocomplete( { 
  source : CologneDisplays.dictionaries.dictshow,
  autoFocus: true,
 }); // end autocomplete dictionary

/* This is based on the example at
https://jqueryui.com/autocomplete/#remote-jsonp
and is required to avoid cross-domain problems.  The server program also
requires some code for this purpose.
*/
$("#key").autocomplete({
  source: function(request,response) {
   $.ajax({
   url:"http://www.sanskrit-lexicon.uni-koeln.de/scans/awork/apidev/getsuggest.php",
   datatype:"jsonp",
   data: {
    //q: request.term
    term: request.term,
    dict: $('#dict').val(),
    input: $('#input').val()
   },
   success: function(data) {
    response(data);  // 'response' is passed in as source argument
   }
   }); // ajax
  },
  delay : 500, // 500 ms delay
  minLength : 2, // user must type at least 2 characters
  select: function(event,ui) {
   if (ui.item) {
   $("#key").val(ui.item.value);
    listDisplay();
   }
  },
  autoFocus: true,
}); //key-autocomplete

 phpinit_helper = function(name,val){
  if (val == ''){return;}
  if (name == 'accent') { //val should be yes or no. Case not important
   val = val.toLowerCase();
  }
  $('#' + name).val(val);
  console.log("phpinit_helper: change #",name,"to",val);
 };
 phpinit = function() {
  var names = ['key','dict','input','output','accent'];
  var phpvals=[ // same order as names
  "<?php echo $_GET['key']?>",
  "<?php echo $_GET['dict']?>",
  "<?php echo $_GET['input']?>",
  "<?php echo $_GET['output']?>",
  "<?php echo $_GET['accent']?>"];
  var i,name,phpval;
  for(i=0;i<names.length;i++) {
   phpinit_helper(names[i],phpvals[i]);
  }
  // If key is provided, generate display for it
  if($('#key').val() != '') {
   listDisplay();
  }
 };
 phpinit();
}); // end ready
 </script>
<script> // see MWScan/2014/web/webtcdev/main_webtc.js
</script>
</head>
<body>
 <div id="logo">
     <a href="http://www.sanskrit-lexicon.uni-koeln.de/">
      <img id="unilogo" src="http://www.sanskrit-lexicon.uni-koeln.de/images/cologne_univ_seal.gif"
           alt="University of Cologne" width="60" height="60" 
           title="Cologne Sanskrit Lexicon"/>
      </a>
 </div>

<table id="preferences">
<tr><td>
 <div id="dictionary">
 <label for="dictcode">dictionary</label>
 <input type="text" name="dictcode" size="4" id="dict" value="" />
 </div>

</td><td>
 <div id="inputdiv">
  <label for="input">input</label>
  <select name="input" id="input">
   <option value='hk' selected='selected'>KH <!--Kyoto-Harvard--></option>
   <option value='slp1'>SLP1</option>
   <option value='itrans'>ITRANS</option>
   <option value='deva'>Devanagari</option>
   <option value='roman'>IAST</option>
  </select>
 </div>
</td><td>
 <div id="outputdiv">
  <label for="output">output</label>
  <select name="output" id="output">
   <option value='deva'>Devanagari</option>
   <option value='hk'>KH <!--Kyoto-Harvard--></option>
   <option value='slp1'>SLP1</option>
   <option value='itrans'>ITRANS</option>
   <option value='roman' selected='selected'>IAST</option>
  </select>
 </div>
</td><td>
 <div id="accentdiv">  <!-- possibly should be per dictionary -->
  <label for="accent">accent?</label>
 <select name="accent" id="accent">
  <option value="yes">Show</option>
  <option value="no" selected="selected">Hide</option>
 </select>
 </div>
</td></tr>
</table> <!-- preferences -->
 <div id="citationdiv">
  citation:&nbsp;
  <input type="text" name="key" size="20" id="key" value="" style="height:1.4em;"/>
  <!--<input type="button" id="correction" value="Corrections" /> -->
  <!-- href is set in change function on #dict -->
  <a id="correction" href="#" target="Corrections">Corrections</a>
 </div>
  
 
 <div id="disp">
  <!-- Requesting data will change the src attribute of this iframe -->
  <iframe id="dataframe">  
   <p>Your browser does not support iframes.</p>
  </iframe>
 </div>
</body>
</html>
