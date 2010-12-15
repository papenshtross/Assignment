// Create layer for progress dialog
document.write("<span id=\"progress\" class=\"hide\">");
document.write("<FORM name=dialog id=dialog>");
document.write("<TABLE border=2  bgcolor=\"#FFFFCC\">");
document.write("<TR><TD ALIGN=\"center\">");
document.write("Progress<BR>");
document.write("<input type=text name=\"bar\" id=\"bar\" size=\"" + _progressWidth/2 + "\"");
if(document.all||document.getElementById)
    document.write(" bar.style=\"color:navy;\">");
else
    document.write(">");
document.write("</TD></TR>");
document.write("</TABLE>");
document.write("</FORM>");
document.write("</span>");
ProgressDestroy();	// Hides
