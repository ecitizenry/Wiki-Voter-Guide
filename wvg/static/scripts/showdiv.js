function showDiv(num) {
	for (i=1;i<=totaldivs;i++) {
		var name = "showdiv" + i; 		
		var d = document.getElementById(name);
		if (i != num) d.style.visibility = 'hidden';
		else d.style.visibility = 'visible';
	}
	return false;
}
