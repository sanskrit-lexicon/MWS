/* Uses js-cookie (Cookies global) — H1523 migrate from jquery.cookie */
CologneDisplays.dictionaries.cookieUpdate = function(flag) {
 // Cookie for holding input, output, accent, dict values;
 // When flag is true, update cookies from corresponding dom values
 // When flag is false, initialize dom values from cookie values,
 //  but use default values if cookie values not present.
 var cookieNames = ['input','output','accent','dict'];
 var domids = ['#input','#output','#accent','#dict'];
 var cookieOptions = {expires: 365, path:'/', sameSite: 'Lax'}; // 365 days
 var i,cookieName,cookieValue,domid;
 var cookieDefaultValues = ['hk','deva','no','mw'];
 if (flag) { // set values of cookies acc. to 'value' of corresponding ids
  for(i=0;i<cookieNames.length;i++) {
   cookieName=cookieNames[i];
   domid=domids[i];
   cookieValue=$(domid).val();
   if ((cookieValue === undefined) || (cookieValue === 'null') || (cookieValue === null) || (cookieValue === '')) {
    cookieValue = cookieDefaultValues[i];
    Cookies.set(cookieName, cookieValue, cookieOptions);
    $(domid).val(cookieValue);
   } else {
    Cookies.set(cookieName, cookieValue, cookieOptions);
   }
  }
  return;
 }
 // When flag is false. For initializing (a) cookies, and (b) dom values
 for(i=0;i<cookieNames.length;i++) {
  cookieName=cookieNames[i];
  domid=domids[i];
  cookieValue = Cookies.get(cookieName); // old value of cookie
  // When not defined, cookieValue may be string 'null', not JS null.
  if ((cookieValue === undefined) || (cookieValue === 'null') || (cookieValue === null) || (cookieValue === '')) {
   cookieValue= cookieDefaultValues[i]; // Use default value
   Cookies.set(cookieName, cookieValue, cookieOptions); // and set cook
  }
  // set dom value
  $(domid).val(cookieValue);
 }
};
