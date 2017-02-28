var CologneDisplays = {};
CologneDisplays.dictionaries= {
    dictnames:
[['WIL' , 'Wilson Sanskrit-English Dictionary'],
['YAT' , 'Yates Sanskrit-English Dictionary'],
['GST' , 'Goldstücker Sanskrit-English Dictionary'],
['BEN' , 'Benfey Sanskrit-English Dictionary'],
['MW72' , 'Monier-Williams Sanskrit-English Dictionary'],
['AP90' , 'Apte Practical Sanskrit-English Dictionary'],
['CAE' , 'Cappeller Sanskrit-English Dictionary'],
['MD' , 'Macdonell Sanskrit-English Dictionary'],
['MW' , 'Monier-Williams Sanskrit-English Dictionary'],
['SHS' , 'Shabda-Sagara Sanskrit-English Dictionary'],
['BHS' , 'Edgerton Buddhist Hybrid Sanskrit Dictionary'],
['AP' , 'Practical Sanskrit-English Dictionary, revised edition'],
['PD' , 'An Encyclopedic Dictionary of Sanskrit on Historical Principles'],
['MWE' , 'Monier-Williams English-Sanskrit Dictionary'],
['BOR' , 'Borooah English-Sanskrit Dictionary'],
['AE' , 'Apte Student English-Sanskrit Dictionary'],
['BUR' , 'Burnouf Dictionnaire Sanscrit-Français'],
['STC' , 'Stchoupak Dictionnaire Sanscrit-Français'],
['PWG' , 'Böhtlingk and Roth Grosses Petersburger Wörterbuch'],
['GRA' , 'Grassman Wörterbuch zum Rig Veda'],
['PW' , 'Böhtlingk Sanskrit-Wörterbuch in kürzerer Fassung'],
['CCS' , 'Cappeller Sanskrit Wörterbuch'],
['SCH' , 'Schmidt Nachträge zum Sanskrit-Wörterbuch'],
['BOP' , 'Bopp Glossarium Sanscritum'],
['SKD' , 'Sabda-kalpadruma'],
['VCP' , 'Vacaspatyam'],
['INM' , 'Index to the Names in the Mahabharata'],
['VEI' , 'The Vedic Index of Names and Subjects'],
['PUI' , 'The Purana Index'],
['ACC' , 'Aufrecht Catalogus Catalogorum'],
['KRM' , 'Kṛdantarūpamālā'],
['IEG' , 'Indian Epigraphical Glossary'],
['SNP' , 'Meulenbeld Sanskrit Names of Plants'],
['PE' , 'Puranic Encyclopedia'],
['PGN' , 'Personal and Geographical Names in the Gupta Inscriptions'],
['MCI' , 'Mahabharata Cultural Index']
],
    dictshowMake: function() {
	var x = [];
        var i,y,label,value,obj;
        for(i=0;i<this.dictnames.length;i++) {
            var y = this.dictnames[i];
	    obj = {label: y[0]+" " + y[1], value:y[0]};
            x.push(obj);
	}
	return x;
    },
    
};
CologneDisplays.dictionaries.dictshow = CologneDisplays.dictionaries.dictshowMake();
